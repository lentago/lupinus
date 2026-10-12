#!/usr/bin/env python3
"""product-list check: the guide's product tables agree with one canonical list.

The canonical list is the parts table in guide/stories/README.md, between the
`<!-- parts:start -->` and `<!-- parts:end -->` markers. Each row names a part
and links to where it lives; the link is the part's identity.

Three guide pages enumerate products. Each is checked against the list:

  guide/picker.md         every product it names is on the list
  guide/runbook-index.md  every product it names is on the list (a subset by design)
  guide/tiers.md          the above, and every part has a row, except the
                          guide's own spine rows, which are not tiered

support/README.md is not checked: `support/` is the adopter's to edit, and a
copy of this guide must not fail its own CI over rows its owner trimmed.

A product is "named" by the lentago links in one column of a page's table (the
column header is configured below). A row names no product on the list when
none of its links in that column resolves to a part: that is the error.

Usage:
  check_product_list.py [--root DIR]

Exit status is 0 only when every page agrees with the list; all disagreements
are listed in one run.
"""
import argparse
import os
import re
import sys

CANONICAL = "guide/stories/README.md"
START, END = "<!-- parts:start -->", "<!-- parts:end -->"
SPINE = "The guide (spine)"

# page -> (column header holding the product link, which parts must appear)
#   "none"     closed world only: whatever is named must be on the list
#   "promises" every part under a promise must appear (spine rows optional)
#   "all"      every part on the list must appear
PAGES = {
    "guide/picker.md": ("Adopt", "none"),
    "guide/runbook-index.md": ("Runbook", "none"),
    "guide/tiers.md": ("Product", "promises"),
}

LINK_RE = re.compile(r"\]\((https://github\.com/lentago/[^)\s]+)\)")


def part_key(url):
    """Reduce a lentago URL to the identity of the part it points at.

    `lentago/<repo>/...` is the repo. Parts that live inside the org's
    `.github` repo are identified by their folder, e.g.
    `.github/fleet-reports/lock-in`; a bare `.github` link identifies nothing.
    """
    path = url.split("github.com/lentago/", 1)[1].split("#", 1)[0].rstrip("/")
    parts = path.split("/")
    if parts[0] != ".github":
        return parts[0]
    if len(parts) >= 4 and parts[1] in ("tree", "blob"):
        return ".github/" + "/".join(parts[3:])
    return None


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tables(lines):
    """Yield (header_cells, [row_cells, ...]) for each pipe table."""
    i = 0
    while i < len(lines):
        if (lines[i].lstrip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1])):
            header = split_row(lines[i])
            rows = []
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            yield header, rows
        else:
            i += 1


def load_canonical(root):
    with open(os.path.join(root, CANONICAL), encoding="utf-8") as fh:
        text = fh.read()
    if START not in text or END not in text:
        raise SystemExit(f"product-list: {CANONICAL} is missing the "
                         f"{START} / {END} markers")
    block = text.split(START, 1)[1].split(END, 1)[0].splitlines()
    parts = {}  # key -> (name, promise)
    for header, rows in tables(block):
        col = {h: n for n, h in enumerate(header)}
        for cells in rows:
            links = LINK_RE.findall(cells[col["Where it lives"]])
            key = part_key(links[0]) if links else None
            if not key:
                raise SystemExit(f"product-list: canonical row {cells[col['Part']]!r} "
                                 "has no lentago link identifying it")
            parts[key] = (cells[col["Part"]], cells[col["Promise"]])
    if not parts:
        raise SystemExit(f"product-list: no parts table found in {CANONICAL}")
    return parts


def check_page(root, page, column, require, parts, failures):
    with open(os.path.join(root, page), encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    found = False
    seen = set()
    for header, rows in tables(lines):
        if column not in header:
            continue
        found = True
        idx = header.index(column)
        for cells in rows:
            cell = cells[idx] if idx < len(cells) else ""
            keys = {part_key(u) for u in LINK_RE.findall(cell)} - {None}
            named = keys & parts.keys()
            if not named:
                failures.append(f"{page}: row {cells[0][:60]!r} names no product "
                                f"on the canonical list in {CANONICAL}")
            seen |= named
    if not found:
        failures.append(f"{page}: no table with a {column!r} column")
        return
    if require == "none":
        return
    for key, (name, promise) in sorted(parts.items()):
        if require == "promises" and promise == SPINE:
            continue
        if key not in seen:
            failures.append(f"{page}: no row for {name!r} ({key}), which is on "
                            f"the canonical list in {CANONICAL}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check product tables against the canonical list.")
    ap.add_argument("--root", default=".", help="Repo root (default: .)")
    args = ap.parse_args(argv)

    parts = load_canonical(args.root)
    failures = []
    for page, (column, require) in PAGES.items():
        check_page(args.root, page, column, require, parts, failures)

    print(f"product-list: {len(parts)} part(s) on the canonical list, "
          f"{len(PAGES)} page(s) checked")
    if failures:
        print(f"\n{len(failures)} disagreement(s):\n", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        print(f"\nA new product starts on the list in {CANONICAL}; then give it "
              "its rows.", file=sys.stderr)
        return 1
    print("every product table agrees with the canonical list")
    return 0


if __name__ == "__main__":
    sys.exit(main())
