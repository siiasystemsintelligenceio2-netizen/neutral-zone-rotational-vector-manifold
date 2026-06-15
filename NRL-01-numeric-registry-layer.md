# NRL-01: Numeric Register Layer

## Purpose

The Numeric Register Layer converts handwritten strings into measurable symbolic objects.

```text
handwritten text -> tokens -> digit vector -> feature table -> matrix/state map
```

## Register sequence

A handwritten string such as:

```text
76760760716776
```

is converted into:

```math
R = (7,6,7,6,0,7,6,0,7,1,6,7,7,6)
```

## Digit frequency

```math
f_k(R) = \frac{\#\{r_i = k\}}{|R|}
```

## Transition count

```math
T_{ab}(R) = \#\{r_i = a, r_{i+1}=b\}
```

## Oscillation score

```math
O(R) = \sum_{i=1}^{n-1}|r_{i+1}-r_i|
```

## Symmetry score

```math
S(R) = 1 - \frac{d_H(R, reverse(R))}{n}
```

## Arrow maps

A handwritten arrow chain like:

```text
↔24→20→0840→V040
```

is encoded as:

```math
\mathcal{T}_{24}: 24 \mapsto 20 \mapsto \Theta_{0840} \mapsto V_{040}
```

## Multiplicity of six

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

## Practical role

NRL-01 does not prove the physics. It gives the project a repeatable way to preserve and process handwritten numbers without losing structure.