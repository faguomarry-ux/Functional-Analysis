#!/usr/bin/env bash
# Unix equivalent of build-book.ps1; always build the complete book.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
command -v xelatex >/dev/null || { echo 'XeLaTeX is required.' >&2; exit 1; }
mkdir -p output/pdf/books/yosida
for pass in 1 2 3; do
  echo "[BUILD] main.tex, pass ${pass}/3"
  xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -synctex=1 -output-directory=output/pdf main.tex
done
test -s output/pdf/main.pdf
echo '[OK] output/pdf/main.pdf'
