# PROJECT_SIGNATURE.md

**Master Reference Document**

---

## Project Identity

**Prepared for:** AMERICAN EAGLESTAR LLC

**Project:** NZ-RVM + NRL-01

**Signature marker:** AE-NZRVM-NRL01-ΔPΩ-0001

This is a project identifier for internal research organization and authorship tracking. It is not a statement of legal trademark registration, patent grant, or regulatory certification.

---

## Document Structure

This project maintains a unified documentation system. All related files follow the `PROJECT_SIGNATURE` naming convention with underscores (`_`).

### Core Technical Specifications

#### 1. [NRL-01: Numeric Register Layer](#nrl-01-numeric-register-layer)
Converts handwritten strings into measurable symbolic objects.

#### 2. [Mathematical Formalization](#mathematical-formalization)  
State vectors, control models, and core physics references.

#### 3. [Symbol Dictionary](#symbol-dictionary)
Complete lexicon of symbols, abbreviations, and working expressions.

---

## NRL-01: Numeric Register Layer

**Reference:** `PROJECT_SIGNATURE.md#nrl-01-numeric-register-layer`

**Full Spec:** See [Archive Reference](#related-file-deprecation--consolidation) for legacy documents.

### Purpose

The Numeric Register Layer converts handwritten strings into measurable symbolic objects.

```text
handwritten text -> tokens -> digit vector -> feature table -> matrix/state map
```

### Register Sequence

A handwritten string such as:

```text
76760760716776
```

is converted into:

```math
R = (7,6,7,6,0,7,6,0,7,1,6,7,7,6)
```

### Digit Frequency

```math
f_k(R) = \frac{\#\{r_i = k\}}{|R|}
```

### Transition Count

```math
T_{ab}(R) = \#\{r_i = a, r_{i+1}=b\}
```

### Oscillation Score

```math
O(R) = \sum_{i=1}^{n-1}|r_{i+1}-r_i|
```

### Symmetry Score

```math
S(R) = 1 - \frac{d_H(R, reverse(R))}{n}
```

### Arrow Maps

A handwritten arrow chain like:

```text
↔24→20→0840→V040
```

is encoded as:

```math
\mathcal{T}_{24}: 24 \mapsto 20 \mapsto \Theta_{0840} \mapsto V_{040}
```

### Multiplicity of Six

A row like:

```text
4 6's / 6666
```

is represented as:

```math
m_6 = 4
```

and optionally as:

```math
N_6=(6,6,6,6)
```

### Practical Role

NRL-01 does not prove the physics. It gives the project a repeatable way to preserve and process handwritten numbers without losing structure.

---

## Mathematical Formalization

**Reference:** `PROJECT_SIGNATURE.md#mathematical-formalization`

**Full Spec:** See [Archive Reference](#related-file-deprecation--consolidation) for legacy documents.

### 1. Physical State Vector

The neutral-zone rotational system is represented by a state vector:

```math
x_t =
\begin{bmatrix}
\omega_t \\
\theta_t \\
\tau_t \\
F_t \\
P_t \\
T_t \\
V_t \\
N_t
\end{bmatrix}
```

| State | Meaning |
|---|---|
| `\omega_t` | angular velocity |
| `\theta_t` | rotation angle |
| `\tau_t` | torque |
| `F_t` | force / thrust |
| `P_t` | pressure |
| `T_t` | temperature |
| `V_t` | velocity vector |
| `N_t` | neutral-zone stability value |

### 2. Control/Register Vector

The numeric register layer contributes a control vector:

```math
c_t =
\begin{bmatrix}
24 \\
20 \\
0840 \\
040 \\
2.16 \\
m_6
\end{bmatrix}
```

This is not a claim that those values are universal constants. They are preserved as handwritten register values for indexing, comparison, and hypothesis generation.

### 3. State Transition Model

```math
x_{t+1} = A(c_t)x_t + B(c_t)u_t + \epsilon_t
```

Where:

- `A(c_t)` is the register-conditioned internal dynamics matrix.
- `B(c_t)` is the register-conditioned control matrix.
- `u_t` is the external input vector.
- `\epsilon_t` is noise, measurement error, or anomaly residual.

### 4. Neutral-Zone Condition

```math
\left\|F_{thrust} + F_{return} + F_{drag} + F_{pressure}\right\| \leq \epsilon_F
```

```math
\left\|\tau_{rotation} + \tau_{return} + \tau_{imbalance}\right\| \leq \epsilon_\tau
```

A system is inside the neutral zone when net force and net torque remain inside tolerance.

### 5. Rotational Advantage

```math
RA = \frac{\|V_{out}\|}{\|\tau_{in}\| + \epsilon} \cdot S_N
```

```math
S_N = e^{-\left(\frac{\|F_{net}\|}{F_{max}} + \frac{\|\tau_{net}\|}{\tau_{max}}\right)}
```

Interpretation: rotational advantage improves when output velocity is high, input torque is low, and neutral-zone stability is high.

### 6. Core Physics References Used Internally

**Torque:**

```math
\tau = r \times F
```

**Angular momentum:**

```math
L = I\omega
```

**Thrust from flow:**

```math
F = \dot{m}v_e + (p_e - p_a)A_e
```

### 7. Numeric-Register Transformation Pipeline

Each handwritten page is treated as:

```math
H_i \rightarrow R_i \rightarrow X_i \rightarrow \mathcal{T}_i \rightarrow N_i \rightarrow RA_i
```

| Object | Meaning |
|---|---|
| `H_i` | handwritten page |
| `R_i` | digit/register sequence |
| `X_i` | matrix form of that page |
| `\mathcal{T}_i` | transformation represented by arrows |
| `N_i` | neutral-zone state |
| `RA_i` | rotational advantage index |

---

## Symbol Dictionary

**Reference:** `PROJECT_SIGNATURE.md#symbol-dictionary`

**Full Spec:** See [Archive Reference](#related-file-deprecation--consolidation) for legacy documents.

| Symbol | Name | Meaning |
|---|---|---|
| `NZ-RVM` | Neutral-Zone Rotational Vector Manifold | Main physical model. |
| `NRL-01` | Numeric Register Layer | Mathematical translation layer for handwritten codes. |
| `N_0` | Neutral Zone Input | Starting state where forces/flows are balanced. |
| `A` | Advantage Axis / Point A | Reference point or tilted axis used for vector redirection. |
| `R_1` | Primary Rotational Chamber | Central circular/rotational structure. |
| `D_r` | Direction of Rotation | Rotation direction around the chamber. |
| `V_o` | Output Velocity Vector | Measurable output direction and speed. |
| `S/S` | Speed-Space Output Region | Region where directional motion/output is represented. |
| `L_r` | Recirculation Loop | Return path or feedback loop. |
| `Z_n` | Neutral Stability Boundary | Envelope that bounds acceptable neutral-zone behavior. |
| `T_v` | Thrust Vector | Directional output force vector. |
| `\tau_r` | Rotational Torque | Torque generated by rotation. |
| `F_b` | Balance Force | Force that keeps the system near neutral balance. |
| `\Delta P` | Pressure Differential | Pressure difference across a chamber, duct, or outlet. |
| `\Omega` | Angular Velocity Field | Spatial field of angular velocity. |
| `\lambda` | Scale Constant | Calibration factor; current working value from notes: `2.16`. |
| `m_6` | Multiplicity of 6 | Count of digit 6 in a register or sub-register. |
| `\Delta_i` | Reduction Operation | Difference/subtraction transformation from handwritten rows. |
| `RA` | Rotational Advantage | Output velocity normalized by input torque and neutral stability. |
| `S_N` | Neutral Stability Score | Exponential score that rewards low net force and torque. |

### Working Expression from Notes

```math
k_6(A^2 \cdot RD)
```

**Interpretation:**

- `k_6`: six-based calibration or count factor.
- `A^2`: squared advantage-axis magnitude or second-order axis effect.
- `RD`: rotational direction / rotational displacement / register direction, depending on context.

**Proposed formal placeholder:**

```math
K_{6,A,RD} = k_6 A^2 RD
```

This is a symbolic feature, not yet a validated physical law.

---

## Cross-Reference Index

- **NRL-01 Numeric Register Layer** → [Section 1](#nrl-01-numeric-register-layer)
- **Mathematical Formalization** → [Section 2](#mathematical-formalization)
- **Symbol Dictionary** → [Section 3](#symbol-dictionary)
- **Arrow Maps & Transformations** → NRL-01 [Arrow Maps](#arrow-maps), Mathematical Formalization [Section 7](#7-numeric-register-transformation-pipeline)
- **Rotational Advantage (RA)** → Symbol Dictionary [Symbol Table](#symbol-dictionary), Mathematical Formalization [Section 5](#5-rotational-advantage)
- **State Vectors & Control Vectors** → Mathematical Formalization [Sections 1–3](#1-physical-state-vector)

---

## Related File Deprecation & Consolidation

The following files are archived and consolidated into this `PROJECT_SIGNATURE.md` document. All content has been integrated below; legacy files are retained for backward reference only.

| Legacy File | Status | Purpose | Linked To | Notes |
|---|---|---|---|---|
| `NRL-01-numeric-registry-layer.md` | **Archived** | Original NRL-01 specification | [NRL-01 Section](#nrl-01-numeric-register-layer) | Hyphenated naming; see unified underscore version |
| `numeric-register-layer.md` | **Archived** | Duplicate of NRL-01 specification | [NRL-01 Section](#nrl-01-numeric-register-layer) | Hyphenated naming; content merged |
| `math-formalization.md` | **Archived** | Original mathematical models | [Mathematical Formalization Section](#mathematical-formalization) | Hyphenated naming; all formulas consolidated |
| `symbol-dictionary.md` | **Archived** | Original symbol reference | [Symbol Dictionary Section](#symbol-dictionary) | Hyphenated naming; complete table integrated |

**Naming Convention:** All PROJECT_SIGNATURE-related files use underscores (`_`), not hyphens (`-`). This document is the canonical reference. Legacy hyphenated files remain in the repository for historical reference but should not be updated.

---

## Unified File Structure

```
neutral-zone-rotational-vector-manifold/
├── PROJECT_SIGNATURE.md (← CANONICAL MASTER DOCUMENT - THIS FILE)
├── [Archived] NRL-01-numeric-registry-layer.md (reference only)
├── [Archived] numeric-register-layer.md (reference only)
├── [Archived] math-formalization.md (reference only)
├── [Archived] symbol-dictionary.md (reference only)
├── README.md (project overview)
├── DEPRECATED_FILES_MANIFEST.md (tracks legacy files)
├── hand-written-transcription-log.md (handwritten input records)
├── symbol-dictionary.md (legacy)
├── matrices.py (implementation)
├── neutral_zone.py (implementation)
├── registers.py (implementation)
├── tokenizer.py (implementation)
└── [other implementation files]
```

---

## How to Navigate & Reference

**For new work:** Always reference `PROJECT_SIGNATURE.md#<section>` using anchor links.

**For specifications:**
- State vectors and control models → [Mathematical Formalization](#mathematical-formalization)
- Numeric register definitions → [NRL-01](#nrl-01-numeric-register-layer)
- Symbol meanings → [Symbol Dictionary](#symbol-dictionary)

**For legacy files:**
If you find external references to `NRL-01-numeric-registry-layer.md`, `numeric-register-layer.md`, `math-formalization.md`, or `symbol-dictionary.md`, redirect to this document using the anchor links above.

---

## Version & Attribution

| Field | Value |
|---|---|
| Document | PROJECT_SIGNATURE.md |
| Version | 1.2 (Fully Consolidated & Unified Structure) |
| Date | 2026-06-16 |
| Organization | AMERICAN EAGLESTAR LLC |
| Signature | AE-NZRVM-NRL01-ΔPΩ-0001 |
| Status | **PRIMARY MASTER REFERENCE**; all legacy files consolidated |
| Naming Convention | Underscores (`_`) required; hyphens (`-`) for legacy files only |

---

**Note:** This document consolidates the content of:
- `NRL-01-numeric-registry-layer.md`
- `numeric-register-layer.md`
- `math-formalization.md`
- `symbol-dictionary.md`

All sections are cross-referenced and anchored for unified navigation. Use the **Cross-Reference Index** and **Symbol Dictionary** to locate specific topics. Legacy files remain archived but are no longer the canonical source.
