# Numerical-Analysis
## Project Description
This repository provides a custom-built Python class designed to solve root-finding problems for standard mathematical functions. It does not utilize any external numerical libraries, achieving its logic strictly through standard Python and the `cmath` module.

## Implemented Methods
1. Bisection Method
2. Fixed-point iteration
3. Newton's method
4. Secant method
5. Method of false position (Regular Falsi)
6. Horner's method
7. Muller's method
8. Steffensen's method

## Algorithm Details and Solutions
* **Bisection & False Position**: Iteratively brackets the root by dividing an interval in half or drawing a secant line between interval bounds until an accurate midpoint/intercept is found.
* **Newton, Secant, & Steffensen**: Open methods that use tangency, sequential secant lines, or functional transformations to quickly converge on a single starting point or pairs of points.
* **Fixed-Point**: Transforms the function into a `x = g(x)` format to zero in on the intercept through looping evaluation.
* **Horner's Method**: Evaluates polynomials optimally through a synthetic division looping structure inside a solver interface.
* **Muller's Method**: Fits a parabola using three distinct points to handle and find complex roots utilizing the `cmath` package.

## File Structure
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
print(root)cd "c:\Users\HSC\Desktop\Tech Learning\My Project\Numerical_Analysis\Root_FInding_project"
git init
