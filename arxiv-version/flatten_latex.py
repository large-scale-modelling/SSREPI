#!/usr/bin/env python3
"""
Flatten a LaTeX file: inline \\input{}/\\include{} recursively, and copy
every image referenced via \\includegraphics{} into the same folder as the
output .tex file, rewriting the paths to match.

Usage:
    python flatten_latex.py miracle-specification-full.tex
    python flatten_latex.py miracle-specification-full.tex -o build\\main-flat.tex

What it does:
  1. Recursively resolves \\input{name} and \\include{name}, pulling their
     contents directly into the main document (adds ".tex" if the name has
     no extension, matching LaTeX's own behaviour).
  2. Finds every \\includegraphics[...]{path} reference (this also matches
     the pandoc-generated \\pandocbounded{\\includegraphics[...]{path}} form,
     since it only looks for the \\includegraphics part), resolves the image
     on disk relative to the MAIN .tex file's folder, copies it next to the
     output .tex file, and rewrites the reference to the bare filename.
  3. If two different source images would collide on the same filename, the
     second one is renamed (name-2.ext, name-3.ext, ...) so nothing is
     overwritten, and the reference is updated to match.
  4. Missing images are reported at the end but don't stop the script; their
     references are left unchanged so you can find and fix them by hand.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

INCLUDE_RE = re.compile(r'\\(input|include)\{([^}]+)\}')
IMG_RE = re.compile(r'\\includegraphics(\[[^\]]*\])?\{([^}]+)\}')


def resolve_tex_path(raw_name: str, relative_to: Path) -> Path:
    candidate = Path(raw_name)
    if not candidate.is_absolute():
        candidate = relative_to / candidate
    if not candidate.exists() and candidate.suffix.lower() != '.tex':
        candidate = candidate.with_name(candidate.name + '.tex')
    return candidate


def expand_includes(file_path: Path, visited: set) -> str:
    file_path = file_path.resolve()
    if file_path in visited:
        print(f"  WARNING: skipping already-included file (would loop): {file_path}", file=sys.stderr)
        return ""
    visited.add(file_path)

    directory = file_path.parent
    content = file_path.read_text(encoding='utf-8')

    def replace(match: re.Match) -> str:
        directive = match.group(1)
        raw_name = match.group(2)
        target = resolve_tex_path(raw_name, directory)
        if target.exists():
            print(f"  Inlining \\{directive}{{{raw_name}}}")
            return expand_includes(target, visited)
        else:
            print(f"  WARNING: could not find included file '{raw_name}' "
                  f"(looked for '{target}') - leaving line as-is", file=sys.stderr)
            return match.group(0)

    return INCLUDE_RE.sub(replace, content)


def collect_images(content: str, tex_dir: Path, output_dir: Path):
    copied_map = {}   # dest filename -> resolved source Path
    missing = []
    copied_count = 0

    def replace(match: re.Match) -> str:
        nonlocal copied_count
        opts = match.group(1) or ''
        raw_path = match.group(2)

        src_candidate = Path(raw_path)
        if not src_candidate.is_absolute():
            src_candidate = tex_dir / src_candidate

        if not src_candidate.exists():
            print(f"  WARNING: image not found, leaving reference unchanged: {raw_path}", file=sys.stderr)
            missing.append(raw_path)
            return match.group(0)

        src_full = src_candidate.resolve()
        file_name = src_full.name

        dest_name = file_name
        if dest_name in copied_map and copied_map[dest_name] != src_full:
            stem, ext = src_full.stem, src_full.suffix
            n = 2
            while dest_name in copied_map and copied_map[dest_name] != src_full:
                dest_name = f"{stem}-{n}{ext}"
                n += 1

        dest_full = output_dir / dest_name
        if not dest_full.exists():
            shutil.copy2(src_full, dest_full)
            print(f"  Copied: {src_full} -> {dest_full}")
            copied_count += 1
        copied_map[dest_name] = src_full

        return f"\\includegraphics{opts}{{{dest_name}}}"

    new_content = IMG_RE.sub(replace, content)
    return new_content, copied_count, missing


def main():
    parser = argparse.ArgumentParser(description="Flatten a LaTeX file and collect its images.")
    parser.add_argument("tex_path", help="Path to the main .tex file")
    parser.add_argument("-o", "--output", help="Path for the flattened .tex output "
                                                 "(default: <name>-flat.tex next to the input)")
    args = parser.parse_args()

    tex_path = Path(args.tex_path).resolve()
    if not tex_path.exists():
        sys.exit(f"ERROR: input file not found: {tex_path}")
    tex_dir = tex_path.parent

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = tex_dir / f"{tex_path.stem}-flat.tex"
    output_dir = output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Main file : {tex_path}")
    print(f"Output    : {output_path}\n")

    print("Step 1: inlining \\input / \\include ...")
    flattened = expand_includes(tex_path, set())
    print()

    print("Step 2: collecting images referenced by \\includegraphics ...")
    flattened, copied_count, missing = collect_images(flattened, tex_dir, output_dir)

    output_path.write_text(flattened, encoding='utf-8')

    print("\nDone.")
    print(f"  Flattened .tex written to : {output_path}")
    print(f"  Images copied             : {copied_count}")
    if missing:
        print("  Images NOT found (left unchanged in output):")
        for m in missing:
            print(f"    - {m}")


if __name__ == "__main__":
    main()
