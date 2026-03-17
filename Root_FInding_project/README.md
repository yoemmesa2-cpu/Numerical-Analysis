# Root-Finding Toolbox

A pure-Python numerical root-finding library that solves **f(x) = 0** using seven classical algorithms.  
No external libraries — only the Python standard library and `cmath`.

---

## File Structure

```
root-finding-project/
├── main.py           ← Run this to start
├── root_finding.py   ← RootFindingProblem class (all algorithms)
├── examples.py       ← All method demonstrations
└── README.md         ← This file
```

---

## How to Run

```bash
python main.py
```

---

## Implemented Methods

| # | Method | Key Arguments |
|---|--------|---------------|
| 1 | Bisection | `a`, `b` |
| 2 | Fixed-Point Iteration | `x0` |
| 3 | Newton's Method | `x0` |
| 4 | Secant Method | `x0`, `x1` |
| 5 | False Position (Regula Falsi) | `a`, `b` |
| 6 | Horner's Method (polynomial) | `coeffs`, `x0` |
| 7 | Muller's Method (complex roots) | `x0`, `x1`, `x2` |

---

## Algorithm Descriptions

### 1. Bisection
Requires a bracket `[a, b]` where `f(a)` and `f(b)` have opposite signs. Repeatedly halves the interval by evaluating f at the midpoint and keeping the half that contains the sign change. **Convergence: linear.**

### 2. Fixed-Point Iteration
Rewrites the equation as `x = g(x)` and iterates `x_{n+1} = g(x_n)`. Converges when `|g'(x)| < 1` near the root.

### 3. Newton's Method
Uses the tangent line at each iterate: `x_{n+1} = x_n - f(x_n) / f'(x_n)`. Requires both `f` and `df`. **Convergence: quadratic.**

### 4. Secant Method
Approximates the derivative with a finite difference using two previous points — no `df` needed. **Convergence: order ≈ 1.618.**

### 5. False Position (Regula Falsi)
Like bisection but picks the new point via linear interpolation between `(a, f(a))` and `(b, f(b))` instead of the midpoint.

### 6. Horner's Method
Evaluates `p(x) = a_n x^n + ... + a_0` via nested multiplication. Also computes `p'(x)` in the same pass, enabling Newton iterations on polynomials without symbolic derivatives.

### 7. Muller's Method
Fits a parabola through three points and uses one of its roots as the next iterate. Uses `cmath.sqrt` to naturally handle **complex roots**. **Convergence: order ≈ 1.84.**

---

## Quick Code Example

```python
from root_finding import RootFindingProblem
import math

f  = lambda x: math.cos(x) - x
df = lambda x: -math.sin(x) - 1
g  = lambda x: math.cos(x)

p = RootFindingProblem(f=f, df=df, g=g)

p.solve("bisection",     a=0, b=1)
p.solve("fixed_point",   x0=0.5)
p.solve("newton",        x0=0.5)
p.solve("secant",        x0=0, x1=1)
p.solve("false_position",a=0, b=1)

# Polynomial  x³ - 6x² + 11x - 6 = 0
p2 = RootFindingProblem()
p2.solve("horner", coeffs=[1, -6, 11, -6], x0=2.5)

# Complex root of x² + 1 = 0
p3 = RootFindingProblem(f=lambda x: x**2 + 1)
p3.solve("muller", x0=0, x1=1, x2=2)
```

---

## Error Handling

| Situation | Exception |
|-----------|-----------|
| Same-sign bracket in bisection / false position | `ValueError` |
| `df` not supplied to Newton | `ValueError` |
| `g` not supplied to Fixed-Point | `ValueError` |
| Derivative or denominator equals zero | `ZeroDivisionError` |
| No convergence within `max_iter` | `RuntimeError` |
