"""
This type stub file was generated by pyright.
"""

"""Bounded-variable least-squares algorithm."""
def compute_kkt_optimality(g, on_bound):
    """Compute the maximum violation of KKT conditions."""
    ...

def bvls(A, b, x_lsq, lb, ub, tol, max_iter, verbose, rcond=...):
    ...
