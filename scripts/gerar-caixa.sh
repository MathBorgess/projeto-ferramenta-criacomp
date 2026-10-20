#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON:-python3}"
# Resolve relative interpreter paths before entering python/.
python_bin="$(command -v "$python_bin")"
case "$python_bin" in
  /*) ;;
  *) python_bin="$PWD/$python_bin" ;;
esac

"$python_bin" "$repo_dir/scripts/validar-caixa.py"
(
  cd "$repo_dir/python"
  "$python_bin" text_to_morph.py
)
mkdir -p "$repo_dir/output/pdf"
cp "$repo_dir/python/output.pdf" "$repo_dir/output/pdf/caixa-morfologica.pdf"

if command -v pdftoppm >/dev/null 2>&1; then
  pdftoppm -singlefile -scale-to 1800 -png \
    "$repo_dir/output/pdf/caixa-morfologica.pdf" \
    "$repo_dir/output/pdf/caixa-morfologica"
fi

printf '%s\n' 'Caixa gerada em output/pdf/caixa-morfologica.pdf'
