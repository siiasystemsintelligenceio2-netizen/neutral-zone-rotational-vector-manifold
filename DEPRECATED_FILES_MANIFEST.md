# Deprecated Files Manifest

**Date:** 2026-06-16

This document tracks files that have been consolidated into `PROJECT_SIGNATURE.md`.

## Superseded Files

All content from the following files has been integrated into `PROJECT_SIGNATURE.md`:

### 1. NRL-01-numeric-registry-layer.md
- **Status:** Deprecated (content merged)
- **Reason:** Integrated into PROJECT_SIGNATURE.md Section: "NRL-01: Numeric Register Layer"
- **Contents:** Numeric register layer specifications, digit frequency, transition counts, oscillation/symmetry scores, arrow maps, multiplicity calculations

### 2. numeric-register-layer.md
- **Status:** Deprecated (duplicate/alias, content merged)
- **Reason:** Duplicate of NRL-01-numeric-registry-layer.md; integrated into PROJECT_SIGNATURE.md
- **Contents:** Same as NRL-01-numeric-registry-layer.md

### 3. math-formalization.md
- **Status:** Deprecated (content merged)
- **Reason:** Integrated into PROJECT_SIGNATURE.md Section: "Mathematical Formalization"
- **Contents:** Physical state vector, control/register vector, state transition model, neutral-zone condition, rotational advantage, physics references, numeric-register transformation pipeline

### 4. symbol-dictionary.md
- **Status:** Deprecated (content merged)
- **Reason:** Integrated into PROJECT_SIGNATURE.md Section: "Symbol Dictionary"
- **Contents:** Complete symbol glossary with 18 key terms, working expressions, and formal placeholders

## Naming Convention Update

**Old:** Files used hyphens (`-`) for multi-word names
- Example: `NRL-01-numeric-registry-layer.md`

**New:** All PROJECT-related documentation uses underscores (`_`)
- Example: `PROJECT_SIGNATURE.md`

## Recommendation

These deprecated files are kept in the repository for historical reference. When starting new work:

1. Reference only `PROJECT_SIGNATURE.md`
2. Use underscore naming for all new documentation files
3. Archive or remove deprecated files in future cleanup

## Single Source of Truth

**Master Document:** `PROJECT_SIGNATURE.md`

All technical specifications, register layers, mathematical formalizations, and symbol definitions are now maintained in one unified location.
