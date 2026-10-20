"""Check PF0 coverage and text fit against the unchanged upstream renderer."""

import json
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth


def main():
    root = Path(__file__).resolve().parents[1]
    categories = {}
    for number, line in enumerate(
        (root / "python/input.txt").read_text(encoding="utf-8").splitlines(), 1
    ):
        if line.count(":") != 1:
            raise ValueError(f"Linha {number}: use um único ':'")
        category, raw_values = line.split(":")
        category = category.strip()
        values = [value.strip() for value in raw_values.split(",")]
        if not category or category in categories:
            raise ValueError(f"Linha {number}: categoria vazia ou repetida")
        if len(values) < 2 or any(not value for value in values):
            raise ValueError(f"Linha {number}: alternativas insuficientes ou vazias")
        if len(set(values)) != len(values):
            raise ValueError(f"Linha {number}: alternativa repetida")
        categories[category] = values

    if len(categories) < 7:
        raise ValueError("PF0 exige ao menos sete categorias")

    width = A4[1] - 20 * mm
    title_width = max(stringWidth(key, "Helvetica-Bold", 10) for key in categories) + 10
    for category, values in categories.items():
        cell_width = (width - title_width) / len(values)
        for value in values:
            if stringWidth(value, "Helvetica", 10) > cell_width - 10:
                raise ValueError(f"Texto ultrapassa a célula: {category}: {value}")

    paths = json.loads((root / "data/caminhos.json").read_text(encoding="utf-8"))
    if len(paths) != 3 or len({path["id"] for path in paths}) != 3:
        raise ValueError("PF0 precisa de três caminhos identificáveis")
    signatures = set()
    for path in paths:
        choices = path["escolhas"]
        if set(choices) != set(categories):
            raise ValueError(f"{path['id']}: categorias ausentes ou extras")
        for category, value in choices.items():
            if value not in categories[category]:
                raise ValueError(f"{path['id']}: alternativa inválida em {category}")
        signatures.add(tuple(choices[category] for category in categories))
    if len(signatures) != 3:
        raise ValueError("Os três caminhos devem ser distintos")

    print(f"OK: {len(categories)} categorias; 3 caminhos completos e distintos; textos cabem nas células.")


if __name__ == "__main__":
    main()
