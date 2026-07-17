"""检查显式指定的 PDF，并按 MinerU 精准解析的 200 页限制切分。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from pypdf import PdfReader, PdfWriter


PAGE_LIMIT = 200


def parse_args() -> argparse.Namespace:
    """解析唯一必需的 PDF 路径及可选输出目录。"""
    parser = argparse.ArgumentParser(
        description="检查 PDF 页数，并在超过 200 页时生成连续分卷。"
    )
    parser.add_argument("--pdf", required=True, help="用户显式指定的 PDF 路径")
    parser.add_argument(
        "--output-root",
        help="分卷输出目录；默认在源文件旁创建 <文件名>-mineru-parts",
    )
    return parser.parse_args()


def normalize_pdf_path(raw_path: str) -> Path:
    """验证输入是存在的 PDF 文件，并返回绝对路径。"""
    pdf_path = Path(raw_path).expanduser().resolve()
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF 文件不存在：{pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"仅支持 PDF 文件：{pdf_path}")
    return pdf_path


def copy_metadata(reader: PdfReader, writer: PdfWriter) -> None:
    """以字符串形式复制可用元数据，避免异常值破坏分卷写入。"""
    if not reader.metadata:
        return

    # pypdf 的元数据写入器只接受字符串键值，因此过滤空值并统一转换。
    metadata = {
        str(key): str(value)
        for key, value in reader.metadata.items()
        if value is not None
    }
    if metadata:
        writer.add_metadata(metadata)


def build_part(
    reader: PdfReader,
    output_path: Path,
    start_index: int,
    end_index: int,
) -> None:
    """写入一个左闭右开的连续 PDF 页区间。"""
    writer = PdfWriter()
    copy_metadata(reader, writer)

    # 严格按源 PDF 顺序加入页面，保证分卷之间无重叠、无遗漏。
    for page_index in range(start_index, end_index):
        writer.add_page(reader.pages[page_index])

    with output_path.open("wb") as output_file:
        writer.write(output_file)


def prepare_pdf(pdf_path: Path, output_root: str | None) -> dict[str, Any]:
    """返回 MinerU 提交清单；仅在页数超限时创建分卷文件。"""
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    if total_pages < 1:
        raise ValueError(f"PDF 没有可处理页面：{pdf_path}")

    if total_pages <= PAGE_LIMIT:
        return {
            "source": str(pdf_path),
            "source_pages": total_pages,
            "page_limit": PAGE_LIMIT,
            "split": False,
            "part_count": 1,
            "parts": [
                {
                    "part": 1,
                    "path": str(pdf_path),
                    "page_start": 1,
                    "page_end": total_pages,
                    "pages": total_pages,
                }
            ],
        }

    parts_dir = (
        Path(output_root).expanduser().resolve()
        if output_root
        else pdf_path.parent / f"{pdf_path.stem}-mineru-parts"
    )
    parts_dir.mkdir(parents=True, exist_ok=True)
    parts: list[dict[str, Any]] = []

    # 每个分卷最多包含 PAGE_LIMIT 页，末卷保留实际剩余页数。
    for part_number, start_index in enumerate(
        range(0, total_pages, PAGE_LIMIT), start=1
    ):
        end_index = min(start_index + PAGE_LIMIT, total_pages)
        output_path = parts_dir / (
            f"{pdf_path.stem}.pages-{start_index + 1:03d}-{end_index:03d}.pdf"
        )
        build_part(reader, output_path, start_index, end_index)
        parts.append(
            {
                "part": part_number,
                "path": str(output_path.resolve()),
                "page_start": start_index + 1,
                "page_end": end_index,
                "pages": end_index - start_index,
            }
        )

    return {
        "source": str(pdf_path),
        "source_pages": total_pages,
        "page_limit": PAGE_LIMIT,
        "split": True,
        "part_count": len(parts),
        "parts_dir": str(parts_dir.resolve()),
        "parts": parts,
    }


def main() -> int:
    """执行检查和切分，并将机器可读清单输出到标准输出。"""
    args = parse_args()
    try:
        pdf_path = normalize_pdf_path(args.pdf)
        manifest = prepare_pdf(pdf_path, args.output_root)
    except Exception as exc:  # 将 PDF 解析错误转换为简洁、可操作的 CLI 错误。
        print(f"prepare_pdf failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
