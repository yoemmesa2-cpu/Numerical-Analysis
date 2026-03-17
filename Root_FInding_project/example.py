from root_finding import RootFindingProblem

# Functions for testing
def f(x): return x**3 - x - 2
def df(x): return 3*x**2 - 1
def g(x): return (x + 2)**(1/3)
def f_complex(x): return x**2 + 1

def run_demos():
    print("--- Root Finding Demos ---")
    p = RootFindingProblem(f=f, df=df, g=g)

    # 1. Real functions [cite: 73, 74, 75, 76, 77]
    print(f"Bisection: {p.solve('bisection', a=1, b=2)}")
    print(f"Newton: {p.solve('newton', x0=1.5)}")
    print(f"Fixed-Point: {p.solve('fixed_point', x0=1.5)}")
    print(f"Secant: {p.solve('secant', x0=1, x1=2)}")
    print(f"False Position: {p.solve('false_position', a=1, b=2)}")

    # 2. Polynomial with Horner [cite: 78]
    p_poly = RootFindingProblem()
    print(f"Horner Evaluation (x^2 - 4 at x=3): {p_poly.solve('horner', coeffs=[1, 0, -4], x=3)}")

    # 3. Complex root with Muller [cite: 79]
    p_cmplx = RootFindingProblem(f=f_complex)
    print(f"Muller (Complex Root): {p_cmplx.solve('muller', x0=-1, x1=0, x2=1)}")

if __name__ == "__main__":
    run_demos()