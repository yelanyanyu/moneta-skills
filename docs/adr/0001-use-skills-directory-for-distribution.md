# Use `skills/` as the distribution boundary

Moneta Skills will align with the skills.sh-oriented repository shape early: bundled skills live under `skills/<skill-name>/SKILL.md`, while scripts and examples stay outside that distribution tree. This makes the publishable package shape visible from the first version and avoids treating later path migration as cleanup after users have already installed the package.
