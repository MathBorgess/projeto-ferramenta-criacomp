"""Sorteie números de 1 a 4 por linha, preservando tentativas e escolhas."""

import argparse
import hashlib
import json
import math
import random
import secrets
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_box(path):
    categories = []
    names = set()
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        if line.count(":") != 1:
            raise ValueError(f"Linha {number}: use um único ':'")
        name, raw = line.split(":")
        name = name.strip()
        values = [value.strip() for value in raw.split(",")]
        if not name or name in names:
            raise ValueError(f"Linha {number}: categoria vazia ou repetida")
        if not 1 <= len(values) <= 4 or any(not value for value in values):
            raise ValueError(f"Linha {number}: informe de uma a quatro opções válidas")
        if len(set(values)) != len(values):
            raise ValueError(f"Linha {number}: opção repetida")
        categories.append((name, values))
        names.add(name)
    if not categories:
        raise ValueError("Caixa vazia")
    return categories


def draw_sequences(categories, seed, count=3):
    capacity = math.prod(len(values) for _, values in categories)
    if not categories or count < 1 or count > capacity:
        raise ValueError("Quantidade incompatível com o número de combinações distintas")
    rng = random.Random(seed)
    accepted, duplicates, seen = [], [], set()
    while len(accepted) < count:
        choices = []
        for category, values in categories:
            attempts = []
            while True:
                number = rng.randint(1, 4)
                attempts.append(number)
                if number <= len(values):
                    break
            choices.append({
                "categoria": category,
                "numero": number,
                "item": values[number - 1],
                "tentativas": attempts,
            })
        numbers = tuple(choice["numero"] for choice in choices)
        record = {"numeros": list(numbers), "escolhas": choices}
        if numbers in seen:
            duplicates.append(record)
        else:
            seen.add(numbers)
            record["id"] = f"proposta-{len(accepted) + 1:02}"
            accepted.append(record)
    return {"sequencias": accepted, "duplicatas_descartadas": duplicates}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "python/input.txt")
    parser.add_argument("--output", type=Path, required=True, help="Novo JSON; recusa sobrescrever")
    parser.add_argument("--seed", type=int, help="Repete as escolhas de uma execução anterior")
    parser.add_argument("--count", type=int, default=3)
    args = parser.parse_args()
    try:
        categories = load_box(args.input)
        seed = args.seed if args.seed is not None else secrets.randbits(64)
        result = {
            "schema_version": 1,
            "gerado_em_utc": datetime.now(timezone.utc).isoformat(),
            "seed": str(seed),
            "gerador": "Python random.Random / randint(1, 4)",
            "entrada_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
            "regra": "Repetir apenas números sem opção e sequências duplicadas; sem filtro semântico.",
            "caixa": [{"categoria": name, "opcoes": values} for name, values in categories],
            **draw_sequences(categories, seed, args.count),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Seed: {seed}")
    for sequence in result["sequencias"]:
        print(sequence["id"] + ": " + " - ".join(map(str, sequence["numeros"])))
    print(f"Registro: {args.output}")


if __name__ == "__main__":
    main()
