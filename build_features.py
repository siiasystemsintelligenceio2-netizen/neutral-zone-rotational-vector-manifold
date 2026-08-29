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


def _should_process_row(row: dict) -> bool:
    """Determine if a row should be processed based on type."""
    row_type = row.get("type", "")
    return "register" in row_type or row_type in {
        "multiplicity",
        "difference",
        "matrix_row",
        "matrix_row_uncertain",
    }


def _transform_row(row: dict) -> dict:
    """Transform a single CSV row to output format."""
    features = analyze_register(row["raw_text"])
    return {
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
        "transitions_json": json.dumps(
            {f"{a}->{b}": n for (a, b), n in features.transitions.items()},
            sort_keys=True,
        ),
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    fieldnames = [
        "page_id",
        "line_id",
        "type",
        "raw_text",
        "digits",
        "length",
        "digit_sum",
        "multiplicity_6",
        "oscillation",
        "symmetry",
        "frequency_json",
        "transitions_json",
    ]
    
    total_rows = 0
    batch_size = 1000
    out_rows = []
    
    with INPUT.open("r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        
        with OUTPUT.open("w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                if _should_process_row(row):
                    out_rows.append(_transform_row(row))
                    total_rows += 1
                    
                    # Flush batch when threshold reached
                    if len(out_rows) >= batch_size:
                        writer.writerows(out_rows)
                        out_rows = []
            
            # Write remaining rows
            if out_rows:
                writer.writerows(out_rows)
    
    print(f"Wrote {total_rows} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
