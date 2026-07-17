"""按页码顺序合并 MinerU Markdown，并安全备份已有结果。"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4


PART_PATTERN = re.compile(r"\.pages-(\d+)-(\d+)\.md$")
BACKUP_PATTERN = re.compile(r"^.+\.\d{8}T\d{6}\.\d{6}Z\.bak\.md$")


def parse_args() -> argparse.Namespace:
    """读取命令行参数，并提供稳定的默认备份策略。"""
    parser = argparse.ArgumentParser(
        description="校验并合并 MinerU 分卷 Markdown，覆盖前备份旧文件。"
    )
    parser.add_argument("--parts-dir", required=True, type=Path, help="分卷 Markdown 目录")
    parser.add_argument("--output", required=True, type=Path, help="完整 Markdown 输出路径")
    parser.add_argument("--backup-dir", required=True, type=Path, help="旧文件备份目录")
    parser.add_argument("--retention-days", type=int, default=30, help="过期天数，默认 30")
    parser.add_argument("--minimum-backups", type=int, default=3, help="至少保留的最近备份数")
    return parser.parse_args()


def load_parts(parts_dir: Path) -> tuple[list[Path], list[tuple[int, int]], list[str]]:
    """读取分卷，验证命名、UTF-8、内容和连续页码。"""
    if not parts_dir.is_dir():
        raise ValueError(f"分卷目录不存在：{parts_dir}")

    candidates: list[tuple[int, int, Path]] = []
    for path in parts_dir.glob("*.pages-*-*.md"):
        match = PART_PATTERN.search(path.name)
        if match:
            start, end = (int(match.group(1)), int(match.group(2)))
            if start < 1 or end < start:
                raise ValueError(f"页码范围无效：{path.name}")
            candidates.append((start, end, path))

    if not candidates:
        raise ValueError(f"未找到符合 *.pages-起始页-结束页.md 的分卷：{parts_dir}")

    candidates.sort(key=lambda item: (item[0], item[1], item[2].name))
    paths: list[Path] = []
    ranges: list[tuple[int, int]] = []
    contents: list[str] = []
    expected_start = 1

    # 合并前逐份检查，避免缺卷、重卷或损坏文本污染最终文件。
    for start, end, path in candidates:
        if start != expected_start:
            raise ValueError(
                f"页码不连续：期待从第 {expected_start} 页开始，实际为 {path.name}"
            )
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            raise ValueError(f"分卷内容为空：{path.name}")
        if "\ufffd" in text:
            raise ValueError(f"发现 Unicode 替换字符，可能存在乱码：{path.name}")
        paths.append(path.resolve())
        ranges.append((start, end))
        contents.append(text.rstrip("\n"))
        expected_start = end + 1

    return paths, ranges, contents


def create_backup(output: Path, backup_dir: Path) -> Path | None:
    """若完整文件已经存在，在覆盖前复制一份带 UTC 时间戳的备份。"""
    if not output.exists():
        return None
    if not output.is_file():
        raise ValueError(f"输出路径不是普通文件：{output}")

    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    backup = backup_dir / f"{output.stem}.{timestamp}.bak.md"
    shutil.copy2(output, backup)
    return backup.resolve()


def write_verified(output: Path, merged: str) -> tuple[int, str]:
    """在同目录临时写入并复核，随后原子替换目标文件。"""
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.parent / f".{output.name}.{uuid4().hex}.tmp"
    try:
        temporary.write_text(merged, encoding="utf-8", newline="\n")
        written = temporary.read_text(encoding="utf-8")
        if written != merged or "\ufffd" in written:
            raise ValueError("临时文件复核失败，未覆盖原文件")
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()

    final_bytes = output.read_bytes()
    final_text = final_bytes.decode("utf-8")
    if final_text != merged:
        raise ValueError("最终文件复核失败")
    return len(final_bytes), hashlib.sha256(final_bytes).hexdigest()


def prune_backups(backup_dir: Path, retention_days: int, minimum_backups: int) -> list[Path]:
    """删除过期备份，同时无条件保留最近若干份。"""
    if retention_days < 0 or minimum_backups < 0:
        raise ValueError("备份保留参数不能为负数")
    if not backup_dir.is_dir():
        return []

    resolved_dir = backup_dir.resolve()
    backups = sorted(
        (
            path
            for path in backup_dir.glob("*.bak.md")
            if path.is_file() and BACKUP_PATTERN.match(path.name)
        ),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)
    deleted: list[Path] = []

    # 只清理指定备份目录内、命名符合本脚本规则且不在保留名单中的文件。
    for path in backups[minimum_backups:]:
        modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        if modified < cutoff and path.resolve().parent == resolved_dir:
            deleted.append(path.resolve())
            path.unlink()
    return deleted


def main() -> int:
    """执行完整的校验、备份、合并、复核和过期清理流程。"""
    args = parse_args()
    try:
        paths, ranges, contents = load_parts(args.parts_dir.resolve())
        merged = "\n\n".join(contents) + "\n"

        # 所有输入校验通过后才备份和写入，失败时尽量保持旧文件不变。
        backup = create_backup(args.output.resolve(), args.backup_dir.resolve())
        byte_count, digest = write_verified(args.output.resolve(), merged)
        deleted = prune_backups(
            args.backup_dir.resolve(), args.retention_days, args.minimum_backups
        )
        result = {
            "status": "success",
            "output": str(args.output.resolve()),
            "parts": [str(path) for path in paths],
            "page_ranges": [{"start": start, "end": end} for start, end in ranges],
            "characters": len(merged),
            "bytes": byte_count,
            "sha256": digest,
            "unicode_replacement_characters": merged.count("\ufffd"),
            "backup_created": str(backup) if backup else None,
            "backups_deleted": [str(path) for path in deleted],
            "backup_policy": {
                "retention_days": args.retention_days,
                "minimum_backups": args.minimum_backups,
            },
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
