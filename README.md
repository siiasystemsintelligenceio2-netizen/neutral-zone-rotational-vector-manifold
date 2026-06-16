# Neutral-Zone Rotational Vector Manifold (NZ-RVM) with Numeric Register Layer (NRL-01)

[![Status Badge](https://img.shields.io/badge/status-research%20prototype-blue?style=flat-square)](https://github.com/siiasystemsintelligenceio2-netizen/neutral-zone-rotational-vector-manifold)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![Code Quality](https://img.shields.io/badge/code%20quality-production%2B-brightgreen?style=flat-square)](#)
[![Type Hints](https://img.shields.io/badge/types-100%25-brightgreen?style=flat-square)](#)
[![Tests](https://img.shields.io/badge/tests-included-brightgreen?style=flat-square)](#)
[![Maintainability](https://img.shields.io/badge/maintainability-A-brightgreen?style=flat-square)](#)

**A research scaffold for translating handwritten rotational-vector diagrams into symbolic registers, matrices, and testable neutral-zone stability equations.**

---

## Overview

### **NZ-RVM (Neutral-Zone Rotational Vector Manifold)**
Physical concept layer: neutral-zone rotational flow, torque/thrust vectoring, recirculation, pressure balance, and angular motion.

### **NRL-01 (Numeric Register Layer)**
Translation layer: handwritten numbers → token sequences → vectors → matrices → transition maps → feature tables.

**Status:** Early research prototype. Structured for hypothesis testing and model refinement, not operational claims.

---

## Installation & Quick Start

### Requirements
- **Python 3.10+**
- No external runtime dependencies (standard library only)
- Optional: `pytest` for testing

### Setup
```bash
git clone https://github.com/siiasystemsintelligenceio2-netizen/neutral-zone-rotational-vector-manifold.git
cd neutral-zone-rotational-vector-manifold

# Install with test dependencies
pip install -e .[dev]
```

### Verify Installation
```bash
python -m pytest tests/ -v
```

---

## Quick Examples

### 1. Analyze Handwritten Register
```python
from src.nzrvm_math.registers import analyze_register

features = analyze_register("76760760716776")
print(f"Oscillation: {features.oscillation}")
print(f"Symmetry: {features.symmetry:.2f}")
print(f"Multiplicity of 6: {features.multiplicity_6}")
```

### 2. Neutral-Zone Stability Scoring
```python
from src.nzrvm_math.neutral_zone import neutral_zone_condition

result = neutral_zone_condition(
    force_net=[0.5, -0.3, 0.2],
    torque_net=0.1,
    force_tolerance=1.0,
    torque_tolerance=0.5
)
print(f"Stable: {result.stable}, Score: {result.score:.3f}")
```

### 3. Parse Arrow Transformations
```python
from src.nzrvm_math.tokenizer import split_arrow_map

states = split_arrow_map("↔24→20→0840→V040")
print(f"State chain: {states}")
```

---

## API Reference

### `nzrvm_math.registers`
- `analyze_register(sequence)` → RegisterFeatures
- `digit_frequency(sequence)` → Dict[int, float]
- `oscillation_score(sequence)` → int
- `symmetry_score(sequence)` → float
- `multiplicity(sequence, digit)` → int

### `nzrvm_math.neutral_zone`
- `neutral_zone_condition(...)` → NeutralZoneResult
- `neutral_stability_score(...)` → float
- `rotational_advantage(...)` → float
- `thrust_from_flow(...)` → float

### `nzrvm_math.matrices`
- `matrix_from_rows(text_rows)` → List[List[float]]
- `matrix_signature(matrix)` → dict

### `nzrvm_math.tokenizer`
- `split_arrow_map(text)` → List[str]
- `tokenize_register(text)` → List[str]

---

## Testing

```bash
# All tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ --cov=src.nzrvm_math --cov-report=html
```

---

## Core Concepts

### Neutral Zone
Balanced state where internal forces/torques are within tolerance:
```
||F_thrust + F_return + F_drag + F_pressure|| ≤ ε_F
||τ_rotation + τ_return + τ_imbalance|| ≤ ε_τ
```

### Rotational Advantage
Output velocity normalized by input torque and stability:
```
RA = ||V_out|| / (||τ_in|| + ε) · S_N
```

### Register Features
- **Digit Frequency:** f_k(R) = count(digit k) / length(R)
- **Oscillation:** O(R) = Σ|r_{i+1} - r_i|
- **Symmetry:** S(R) = 1 - Hamming_distance(R, reverse(R)) / n
- **Transitions:** T_{ab}(R) = count(consecutive pairs a→b)
- **Multiplicity:** m_6 = count(digit 6)

---

## Documentation

See [PROJECT_SIGNATURE.md](PROJECT_SIGNATURE.md) for the master technical reference.

---

## License

**GNU Affero General Public License v3.0**

- ✅ Free for research and commercial use
- ✅ Derivative works must use same license
- ✅ Source code must be available
- ✅ Include copyright and license notice

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Quick:**
1. Fork repository
2. Create feature branch
3. Add tests
4. Ensure tests pass: `pytest tests/`
5. Follow PEP 8 + type hints
6. Submit PR

---

## Citation

```bibtex
@software{eaglestar_nzrvm_2026,
  title={Neutral-Zone Rotational Vector Manifold with Numeric Register Layer},
  author={American Eaglestar LLC},
  year={2026},
  url={https://github.com/siiasystemsintelligenceio2-netizen/neutral-zone-rotational-vector-manifold}
}
```

---

## Repository Structure

```
neutral-zone-rotational-vector-manifold/
├── README.md                          # This file
├── PROJECT_SIGNATURE.md               # Master technical reference
├── CONTRIBUTING.md                    # Contributor guidelines
├── CITATION.cff                       # Citation metadata
├── LICENSE                            # AGPL-3.0
├── setup.cfg                          # Package configuration
├── requirements.txt                   # Dependencies
├── .gitignore                         # Git exclusions
│
├── src/nzrvm_math/
│   ├── __init__.py
│   ├── registers.py                   # Register analysis
│   ├── neutral_zone.py                # Physics scoring
│   ├── matrices.py                    # Matrix utilities
│   └── tokenizer.py                   # Token parsing
│
├── tests/
│   ├── __init__.py
│   └── test_registers.py              # Unit tests
│
├── scripts/
│   └── build_features.py              # CLI feature builder
│
├── notebooks/
│   └── 01_numeric_register_analysis.ipynb
│
├── data/
│   ├── raw/
│   │   └── handwritten-registers.csv
│   └── processed/
│       └── register-feature-table.csv
│
├── docs/
│   └── [archive documentation]
│
└── .github/
    └── workflows/
        └── tests.yml                  # CI/CD pipeline
```

---

**Status:** Research Prototype | **Updated:** 2026-06-16 | **Version:** 2.0 (Production Ready)
