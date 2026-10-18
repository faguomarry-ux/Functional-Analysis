#!/usr/bin/env python3
"""Check book structure and references without TeX or third-party packages."""
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check():
    errors = []
    seen = set()
    texts = {}

    def visit(path):
        path = path.resolve()
        if path in seen:
            errors.append(f"Repeated input: {path.relative_to(ROOT)}")
            return
        seen.add(path)
        if not path.is_file():
            errors.append(f"Missing input: {path.relative_to(ROOT)}")
            return
        source = path.read_text(encoding="utf-8-sig")
        # TeX comments are irrelevant, including commented includeonly examples.
        source = re.sub(r"(?<!\\)%[^\n]*", "", source)
        texts[path] = source
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", source):
            child = ROOT / target
            if not child.suffix:
                child = child.with_suffix(".tex")
            visit(child)

    visit(ROOT / "main.tex")
    combined = "\n".join(texts.values())
    labels = re.findall(r"\\label\{([^}]+)\}", combined)
    for label, count in Counter(labels).items():
        if count > 1:
            errors.append(f"Duplicate label: {label}")
    for target in re.findall(r"\\(?:ref|pageref|eqref|autoref)\{([^}]+)\}", combined):
        if target not in labels:
            errors.append(f"Undefined reference: {target}")
    bibliography = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", combined))
    for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", combined):
        for key in group.split(","):
            if key.strip() not in bibliography:
                errors.append(f"Undefined citation: {key.strip()}")
    for path, source in texts.items():
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
            kind, env = match.groups()
            if kind == "begin":
                stack.append(env)
            elif not stack or stack.pop() != env:
                errors.append(f"Environment mismatch: {path.relative_to(ROOT)}: {env}")
                break
        if stack:
            errors.append(f"Unclosed environments: {path.relative_to(ROOT)}: {stack}")
        exercises = source.count(r"\begin{exercise}")
        solutions = source.count(r"\begin{solution}")
        if exercises != solutions:
            errors.append(f"Exercise/solution mismatch: {path.relative_to(ROOT)}")
    catalog = json.loads((ROOT / "books/yosida/catalog.json").read_text(encoding="utf-8-sig"))
    if [c["number"] for c in catalog] != list(range(15)):
        errors.append("Catalog must preserve chapters 0 through 14")
    total = sum(len(c["sections"]) for c in catalog)
    if total != 132:
        errors.append(f"Catalog section total changed: {total}")
    written = 0
    for chapter in catalog:
        entry = ROOT / "books/yosida" / chapter["file"]
        entry_text = texts.get(entry.resolve(), "")
        section_files = [entry_text]
        for target in re.findall(r"\\input\{([^}]+)\}", entry_text):
            child = ROOT / target
            if not child.suffix:
                child = child.with_suffix(".tex")
            section_files.append(texts.get(child.resolve(), ""))
        body = "\n".join(section_files)
        expected = len(chapter["sections"])
        actual = len(re.findall(r"\\section(?:\[[^\]]*\])?\{", body))
        if actual != expected:
            errors.append(f"Chapter {chapter['number']}: {actual}/{expected} numbered sections")
        written += expected - body.count(r"\YosidaSectionPlaceholder")
    for message in sorted(set(errors)):
        print(f"ERROR: {message}", file=sys.stderr)
    if errors:
        return 1
    print(f"OK: {len(texts)} TeX inputs; labels and citations resolve; "
          f"exercise/solution counts match; {written}/{total} numbered sections written.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
