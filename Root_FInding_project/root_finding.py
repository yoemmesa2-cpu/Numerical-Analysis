import cmath

class RootFindingProblem:
    def __init__(self, f=None, df=None, g=None):
        self.f = f
        self.df = df
        self.g = g

    def solve(self, method, **kwargs):
        method = method.lower()
        if method == "bisection":
            return self._bisection(**kwargs)
        elif method == "fixed_point":
            return self._fixed_point(**kwargs)
        elif method == "newton":
            return self._newton(**kwargs)
        elif method == "secant":
            return self._secant(**kwargs)
        elif method == "false_position":
            return self._false_position(**kwargs)
        elif method == "steffensen":
            return self._steffensen(**kwargs)
        elif method == "horner":
            return self._horner(**kwargs)
        elif method == "muller":
            return self._muller(**kwargs)
        else:
            raise ValueError("Unknown method.")

    def _bisection(self, a, b, tol=1e-6, max_iter=100):
        if self.f is None: raise ValueError("Function f missing.")
        if self.f(a) * self.f(b) >= 0:
            raise ValueError("Invalid interval: f(a) and f(b) must have opposite signs.")
        for _ in range(max_iter):
            c = (a + b) / 2.0
            if abs(self.f(c)) < tol or (b - a) / 2.0 < tol: return c
            if self.f(c) * self.f(a) < 0: b = c
            else: a = c
        raise RuntimeError("No convergence after max_iter.")

    def _newton(self, x0, tol=1e-6, max_iter=100):
        if self.f is None: raise ValueError("Function f missing.")
        if self.df is None: raise ValueError("Missing derivative in Newton.")
        for _ in range(max_iter):
            dfx = self.df(x0)
            if dfx == 0: raise ZeroDivisionError("Division by zero in iterations.")
            x1 = x0 - self.f(x0) / dfx
            if abs(x1 - x0) < tol: return x1
            x0 = x1
        raise RuntimeError("No convergence after max_iter.")

    def _fixed_point(self, x0, tol=1e-6, max_iter=100):
        if self.g is None: raise ValueError("Missing fixed-point function.")
        for _ in range(max_iter):
            x1 = self.g(x0)
            if abs(x1 - x0) < tol: return x1
            x0 = x1
        raise RuntimeError("No convergence.")

    def _secant(self, x0, x1, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            fx0, fx1 = self.f(x0), self.f(x1)
            if fx1 - fx0 == 0: raise ZeroDivisionError("Division by zero.")
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            if abs(x2 - x1) < tol: return x2
            x0, x1 = x1, x2
        raise RuntimeError("No convergence.")

    def _false_position(self, a, b, tol=1e-6, max_iter=100):
        if self.f(a) * self.f(b) >= 0: raise ValueError("Invalid interval.")
        for _ in range(max_iter):
            fa, fb = self.f(a), self.f(b)
            c = b - fb * (b - a) / (fb - fa)
            if abs(self.f(c)) < tol: return c
            if self.f(a) * self.f(c) < 0: b = c
            else: a = c
        raise RuntimeError("No convergence.")

    def _steffensen(self, x0, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            fx = self.f(x0)
            denom = self.f(x0 + fx) - fx
            if denom == 0: raise ZeroDivisionError("Division by zero.")
            x1 = x0 - (fx**2) / denom
            if abs(x1 - x0) < tol: return x1
            x0 = x1
        raise RuntimeError("No convergence.")

    def _horner(self, coeffs, x):
        res = coeffs[0]
        for i in range(1, len(coeffs)):
            res = res * x + coeffs[i]
        return res

    def _muller(self, x0, x1, x2, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            f0, f1, f2 = self.f(x0), self.f(x1), self.f(x2)
            h1, h2 = x1 - x0, x2 - x1
            d1, d2 = (f1 - f0) / h1, (f2 - f1) / h2
            a = (d2 - d1) / (h2 + h1)
            b = a * h2 + d2
            c = f2
            disc = cmath.sqrt(b**2 - 4*a*c)
            den = b + disc if abs(b + disc) > abs(b - disc) else b - disc
            dx = -2 * c / den
            x3 = x2 + dx
            if abs(dx) < tol: return x3
            x0, x1, x2 = x1, x2, x3
        raise RuntimeError("No convergence.")