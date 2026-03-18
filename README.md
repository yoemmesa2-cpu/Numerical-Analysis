# Root-Finding Problem

A pure-Python numerical root-finding library that solves **f(x) = 0** using seven classical algorithms.  
No external libraries are required — only the Python standard library and `cmath`.

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)

---

## Implemented Methods

| # | Method | Function |
|---|--------|----------|
| 1 | Bisection | `_bisection` |
| 2 | Fixed-Point Iteration | `_fixed_point` |
| 3 | Newton's Method (Newton-Raphson) | `_newton` |
| 4 | Secant Method | `_secant` |
| 5 | False Position (Regula Falsi) | `_false_position` |
| 6 | Horner's Method (polynomial solver) | `_horner` / `_horner_solve` |
| 7 | Muller's Method (complex roots) | `_muller` |

---

## Algorithm Descriptions

### 1. Bisection Method
Requires a bracket `[a, b]` where `f(a)` and `f(b)` have opposite signs.  
The interval is repeatedly halved by evaluating `f` at the midpoint and keeping the sub-interval that still contains the sign change.  
**Convergence:** linear — the error halves each iteration.

### 2. Fixed-Point Iteration
Rewrites the equation as `x = g(x)` and iterates `x_{n+1} = g(x_n)` from an initial guess `x0`.  
Converges when `|g'(x)| < 1` near the root.

### 3. Newton's Method (Newton-Raphson)
Uses the tangent line to the curve at each iterate:
```
x_{n+1} = x_n - f(x_n) / f'(x_n)
```
Requires both `f` and its derivative `df`.  
**Convergence:** quadratic near a simple root.

### 4. Secant Method
Approximates the derivative with a finite difference using two previous iterates:
```
x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
```
Does **not** require `df`.  
**Convergence:** super-linear (order ≈ 1.618).

### 5. False Position (Regula Falsi)
Like bisection, maintains a bracket `[a, b]` with opposite signs, but the new point is chosen by linear interpolation between `(a, f(a))` and `(b, f(b))` rather than the midpoint.

### 6. Horner's Method
Evaluates a polynomial `p(x) = a_n x^n + ... + a_0` efficiently using nested multiplication:
```
p(x) = ((...((a_n · x + a_{n-1}) · x + a_{n-2}) · ...) · x + a_0)
```
Also computes `p'(x)` in the same pass, enabling Newton iterations entirely through Horner evaluation.

### 7. Muller's Method
Fits a quadratic (parabola) through three points `(x0, f(x0))`, `(x1, f(x1))`, `(x2, f(x2))` and uses one of its roots as the next iterate. By using `cmath.sqrt` for the discriminant, the method naturally finds **complex roots**.  
**Convergence:** order ≈ 1.84.

---

## File Structure

```
root-finding-project/
├── root_finding.py   # RootFindingProblem class (all algorithms)
├── examples.py       # Demonstrations of every method
└── README.md         # This file
```

---

## Requirements

- Python 3.7+
- Standard library only (`cmath`, `math`)

---

## How to Run the Examples

```bash
# Clone or download the repository, then:
python examples.py
```

All seven methods are exercised and results are printed to the terminal.

---

## Quick Code Example

```python
from root_finding import RootFindingProblem
import cmath

# Define the function and its derivative
f  = lambda x: math.cos(x) - x
df = lambda x: -math.sin(x) - 1
g  = lambda x: math.cos(x)          # fixed-point form

p = RootFindingProblem(f=f, df=df, g=g)

# Bisection
print(p.solve("bisection",    a=0, b=1))

# Fixed-point iteration
print(p.solve("fixed_point",  x0=0.5))

# Newton's method
print(p.solve("newton",       x0=0.5))

# Secant method
print(p.solve("secant",       x0=0, x1=1))

# False position
print(p.solve("false_position", a=0, b=1))

# Horner's method on x³ - 6x² + 11x - 6 = 0  (roots: 1, 2, 3)
print(p.solve("horner", coeffs=[1, -6, 11, -6], x0=0.5))

# Muller's method — finds complex root of x² + 1 = 0
p2 = RootFindingProblem(f=lambda x: x**2 + 1)
print(p2.solve("muller", x0=0, x1=1, x2=2))
```

---

## Error Handling

The class raises descriptive exceptions for common misuse:

| Situation | Exception |
|-----------|-----------|
| `f(a)` and `f(b)` have the same sign | `ValueError` |
| `df` not supplied to Newton | `ValueError` |
| `g` not supplied to Fixed-Point | `ValueError` |
| Derivative (or denominator) is zero | `ZeroDivisionError` |
| Algorithm exceeds `max_iter` | `RuntimeError` |
* `root_finding.py`: Contains the `RootFindingProblem` class and all core algorithmic logic.
* `examples.py`: A demonstration script verifying functionality across real functions, polynomials, and complex roots.
* `README.md`: This descriptive file.

## How to Run
Navigate to the directory housing the repository files using your terminal and execute:
`python examples.py`

## Code Example
```python
from root_finding import RootFindingProblem

def f(x): return x**3 - x - 2
def df(x): return 3*x**2 - 1

problem = RootFindingProblem(f=f, df=df)
root = problem.solve("newton", x0=1.5)
print(root)
