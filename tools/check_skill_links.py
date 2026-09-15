#!/usr/bin/env python3
"""Report broken relative links and unknown skill names in skill docs, CLAUDE.md and README.md."""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKILL_RE = re.compile(r"`(centroid-[a-z0-9-]+)`")
EXTERNAL = ("http://", "https://", "mailto:")


def _doc_files(root):
    files = sorted((root / ".claude" / "skills").glob("**/*.md"))
    files += [p for p in (root / "CLAUDE.md", root / "README.md") if p.is_file()]
    return files


def check_tree(root):
    root = Path(root)
    skills_dir = root / ".claude" / "skills"
    known = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
    misses = []
    for path in _doc_files(root):
        rel_path = path.relative_to(root).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in LINK_RE.findall(line):
                if target.startswith(EXTERNAL):
                    continue
                file_part = target.split("#", 1)[0]
                if file_part and not (path.parent / file_part).exists():
                    misses.append(f"{rel_path}:{lineno}: broken link {target}")
            for name in SKILL_RE.findall(line):
                if name not in known:
                    misses.append(f"{rel_path}:{lineno}: unknown skill {name}")
    return misses


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    misses = check_tree(root)
    for miss in misses:
        print(miss)
    if misses:
        return 1
    print(f"OK: {len(_doc_files(root))} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
