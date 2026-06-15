# Mathematical Formalization

## 1. Physical state vector

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

## 2. Control/register vector

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

## 3. State transition model

```math
x_{t+1} = A(c_t)x_t + B(c_t)u_t + \epsilon_t
```

Where:

- `A(c_t)` is the register-conditioned internal dynamics matrix.
- `B(c_t)` is the register-conditioned control matrix.
- `u_t` is the external input vector.
- `\epsilon_t` is noise, measurement error, or anomaly residual.

## 4. Neutral-zone condition

```math
\left\|F_{thrust} + F_{return} + F_{drag} + F_{pressure}\right\| \leq \epsilon_F
```

```math
\left\|\tau_{rotation} + \tau_{return} + \tau_{imbalance}\right\| \leq \epsilon_\tau
```

A system is inside the neutral zone when net force and net torque remain inside tolerance.

## 5. Rotational advantage

```math
RA = \frac{\|V_{out}\|}{\|\tau_{in}\| + \epsilon} \cdot S_N
```

```math
S_N = e^{-\left(\frac{\|F_{net}\|}{F_{max}} + \frac{\|\tau_{net}\|}{\tau_{max}}\right)}
```

Interpretation: rotational advantage improves when output velocity is high, input torque is low, and neutral-zone stability is high.

## 6. Core physics references used internally by the model

Torque:

```math
\tau = r \times F
```

Angular momentum:

```math
L = I\omega
```

Thrust from flow:

```math
F = \dot{m}v_e + (p_e - p_a)A_e
```

## 7. Numeric-register transformation

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