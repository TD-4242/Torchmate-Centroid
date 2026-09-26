#!/usr/bin/env python3
"""Report broken relative links and unknown skill names in skill docs, CLAUDE.md and README.md."""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKILL_RE = re.compile(r"`(centroid-[a-z0-9-]+)`")
EXTERNAL = ("http://", "https://", "mailto:")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def _doc_files(root):
    files = sorted((root / ".claude" / "skills").glob("**/*.md"))
    files += [p for p in (root / "CLAUDE.md", root / "README.md") if p.is_file()]
    return files


def _slug(heading):
    # GitHub's rule: link text only, lowercase, drop punctuation but - and _, spaces to -.
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.replace(" ", "-")


def _anchors(path, cache):
    if path not in cache:
        seen, anchors, in_fence = {}, set(), False
        for line in path.read_text(encoding="utf-8").splitlines():
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            match = None if in_fence else HEADING_RE.match(line)
            if match:
                slug = _slug(match.group(1))
                count = seen.get(slug, 0)
                seen[slug] = count + 1
                anchors.add(slug if count == 0 else f"{slug}-{count}")
        cache[path] = anchors
    return cache[path]


def check_tree(root):
    root = Path(root)
    skills_dir = root / ".claude" / "skills"
    known = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
    misses = []
    anchor_cache = {}
    for path in _doc_files(root):
        rel_path = path.relative_to(root).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in LINK_RE.findall(line):
                if target.startswith(EXTERNAL):
                    continue
                file_part, _, anchor = target.partition("#")
                linked = (path.parent / file_part) if file_part else path
                if not linked.exists():
                    misses.append(f"{rel_path}:{lineno}: broken link {target}")
                elif anchor and linked.suffix == ".md" and anchor not in _anchors(linked, anchor_cache):
                    misses.append(f"{rel_path}:{lineno}: broken anchor {target}")
            for name in SKILL_RE.findall(line):
                if name not in known:
                    misses.append(f"{rel_path}:{lineno}: unknown skill {name}")
    return misses


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    files = _doc_files(root)
    if not files:
        print(f"error: {root} has no Markdown files to check "
              "(.claude/skills/**/*.md, CLAUDE.md, README.md)", file=sys.stderr)
        return 2
    misses = check_tree(root)
    for miss in misses:
        print(miss)
    if misses:
        return 1
    print(f"OK: {len(files)} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
