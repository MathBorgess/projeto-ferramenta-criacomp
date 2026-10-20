import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/sortear-caminhos.py"
spec = importlib.util.spec_from_file_location("sorteio", SCRIPT)
sorteio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sorteio)


class SorteioTest(unittest.TestCase):
    def test_same_seed_replays_draws_and_choices(self):
        box = [("Artefato", ["A", "B", "C", "D"]), ("IA", ["S", "G", "H"])]
        first = sorteio.draw_sequences(box, seed=42, count=3)
        self.assertEqual(first, sorteio.draw_sequences(box, seed=42, count=3))
        self.assertEqual(3, len({tuple(item["numeros"]) for item in first["sequencias"]}))
        for sequence in first["sequencias"]:
            for (category, values), choice in zip(box, sequence["escolhas"]):
                self.assertEqual(category, choice["categoria"])
                self.assertEqual(values[choice["numero"] - 1], choice["item"])
                self.assertTrue(all(1 <= draw <= 4 for draw in choice["tentativas"]))

    def test_missing_fourth_option_is_rejected_and_logged(self):
        result = sorteio.draw_sequences([("IA", ["S", "G", "H"])], seed=0, count=1)
        choice = result["sequencias"][0]["escolhas"][0]
        self.assertEqual([4, 4, 1], choice["tentativas"])
        self.assertEqual(1, choice["numero"])
        self.assertEqual("S", choice["item"])

    def test_duplicate_sequences_are_logged_and_not_returned(self):
        result = sorteio.draw_sequences([("A", ["a", "b"])], seed=2, count=2)
        self.assertEqual({(1,), (2,)}, {tuple(item["numeros"]) for item in result["sequencias"]})
        self.assertGreater(len(result["duplicatas_descartadas"]), 0)

    def test_impossible_count_fails_instead_of_looping(self):
        with self.assertRaises(ValueError):
            sorteio.draw_sequences([("A", ["a"])], seed=0, count=3)

    def test_input_rejects_unsupported_or_ambiguous_rows(self):
        for content in ["A: a,b,c,d,e", "A: a,b\nA: c,d", "A: a,,b", "A a,b", ""]:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / "input.txt"
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(ValueError):
                    sorteio.load_box(path)

    def test_cli_preserves_an_existing_run(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.txt"
            source.write_text("A: a,b,c,d", encoding="utf-8")
            output = Path(folder) / "registro.json"
            output.write_text("registro anterior", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--input", str(source),
                 "--output", str(output), "--seed", "1"],
                capture_output=True, text=True, cwd=folder,
            )
            self.assertEqual(2, completed.returncode)
            self.assertEqual("registro anterior", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
