"""Build register feature table from data/raw/handwritten-registers.csv."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nzrvm_math.registers import analyze_register  # type: ignore  # noqa: E402

INPUT = ROOT / "data" / "raw" / "handwritten-registers.csv"
OUTPUT = ROOT / "data" / "processed" / "register-feature-table.csv"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with INPUT.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    out_rows = []
    for row in rows:
        if "register" in row["type"] or row["type"] in {"multiplicity", "difference", "matrix_row", "matrix_row_uncertain"}:
            features = analyze_register(row["raw_text"])
            out_rows.append({
                "page_id": row["page_id"],
                "line_id": row["line_id"],
                "type": row["type"],
                "raw_text": row["raw_text"],
                "digits": " ".join(str(d) for d in features.digits),
                "length": features.length,
                "digit_sum": features.digit_sum,
                "multiplicity_6": features.multiplicity_6,
                "oscillation": features.oscillation,
                "symmetry": round(features.symmetry, 6),
                "frequency_json": json.dumps(features.frequency, sort_keys=True),
                "transitions_json": json.dumps({f"{a}->{b}": n for (a, b), n in features.transitions.items()}, sort_keys=True),
            })

    with OUTPUT.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "page_id", "line_id", "type", "raw_text", "digits", "length", "digit_sum",
            "multiplicity_6", "oscillation", "symmetry", "frequency_json", "transitions_json",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
