"""
This type stub file was generated by pyright.
"""

TERMINATION_MESSAGES = ...
class HessianLinearOperator:
    """Build LinearOperator from hessp"""
    def __init__(self, hessp, n) -> None:
        ...
    
    def __call__(self, x, *args): # -> LinearOperator:
        ...
    


class LagrangianHessian:
    """The Hessian of the Lagrangian as LinearOperator.

    The Lagrangian is computed as the objective function plus all the
    constraints multiplied with some numbers (Lagrange multipliers).
    """
    def __init__(self, n, objective_hess, constraints_hess) -> None:
        ...
    
    def __call__(self, x, v_eq=..., v_ineq=...): # -> LinearOperator:
        ...
    


def update_state_sqp(state, x, last_iteration_failed, objective, prepared_constraints, start_time, tr_radius, constr_penalty, cg_info):
    ...

def update_state_ip(state, x, last_iteration_failed, objective, prepared_constraints, start_time, tr_radius, constr_penalty, cg_info, barrier_parameter, barrier_tolerance):
    ...

