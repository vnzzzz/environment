"""
This type stub file was generated by pyright.
"""

"""
ltisys -- a collection of functions to convert linear time invariant systems
from one representation to another.
"""
__all__ = ['tf2ss', 'abcd_normalize', 'ss2tf', 'zpk2ss', 'ss2zpk', 'cont2discrete']
def tf2ss(num, den):
    r"""Transfer function to state-space representation.

    Parameters
    ----------
    num, den : array_like
        Sequences representing the coefficients of the numerator and
        denominator polynomials, in order of descending degree. The
        denominator needs to be at least as long as the numerator.

    Returns
    -------
    A, B, C, D : ndarray
        State space representation of the system, in controller canonical
        form.

    Examples
    --------
    Convert the transfer function:

    .. math:: H(s) = \frac{s^2 + 3s + 3}{s^2 + 2s + 1}

    >>> num = [1, 3, 3]
    >>> den = [1, 2, 1]

    to the state-space representation:

    .. math::

        \dot{\textbf{x}}(t) =
        \begin{bmatrix} -2 & -1 \\ 1 & 0 \end{bmatrix} \textbf{x}(t) +
        \begin{bmatrix} 1 \\ 0 \end{bmatrix} \textbf{u}(t) \\

        \textbf{y}(t) = \begin{bmatrix} 1 & 2 \end{bmatrix} \textbf{x}(t) +
        \begin{bmatrix} 1 \end{bmatrix} \textbf{u}(t)

    >>> from scipy.signal import tf2ss
    >>> A, B, C, D = tf2ss(num, den)
    >>> A
    array([[-2., -1.],
           [ 1.,  0.]])
    >>> B
    array([[ 1.],
           [ 0.]])
    >>> C
    array([[ 1.,  2.]])
    >>> D
    array([[ 1.]])
    """
    ...

def abcd_normalize(A=..., B=..., C=..., D=...): # -> tuple[NDArray[float64] | Unknown, NDArray[float64] | Unknown, NDArray[float64] | Unknown, NDArray[float64] | Unknown]:
    """Check state-space matrices and ensure they are 2-D.

    If enough information on the system is provided, that is, enough
    properly-shaped arrays are passed to the function, the missing ones
    are built from this information, ensuring the correct number of
    rows and columns. Otherwise a ValueError is raised.

    Parameters
    ----------
    A, B, C, D : array_like, optional
        State-space matrices. All of them are None (missing) by default.
        See `ss2tf` for format.

    Returns
    -------
    A, B, C, D : array
        Properly shaped state-space matrices.

    Raises
    ------
    ValueError
        If not enough information on the system was provided.

    """
    ...

def ss2tf(A, B, C, D, input=...):
    r"""State-space to transfer function.

    A, B, C, D defines a linear state-space system with `p` inputs,
    `q` outputs, and `n` state variables.

    Parameters
    ----------
    A : array_like
        State (or system) matrix of shape ``(n, n)``
    B : array_like
        Input matrix of shape ``(n, p)``
    C : array_like
        Output matrix of shape ``(q, n)``
    D : array_like
        Feedthrough (or feedforward) matrix of shape ``(q, p)``
    input : int, optional
        For multiple-input systems, the index of the input to use.

    Returns
    -------
    num : 2-D ndarray
        Numerator(s) of the resulting transfer function(s). `num` has one row
        for each of the system's outputs. Each row is a sequence representation
        of the numerator polynomial.
    den : 1-D ndarray
        Denominator of the resulting transfer function(s). `den` is a sequence
        representation of the denominator polynomial.

    Examples
    --------
    Convert the state-space representation:

    .. math::

        \dot{\textbf{x}}(t) =
        \begin{bmatrix} -2 & -1 \\ 1 & 0 \end{bmatrix} \textbf{x}(t) +
        \begin{bmatrix} 1 \\ 0 \end{bmatrix} \textbf{u}(t) \\

        \textbf{y}(t) = \begin{bmatrix} 1 & 2 \end{bmatrix} \textbf{x}(t) +
        \begin{bmatrix} 1 \end{bmatrix} \textbf{u}(t)

    >>> A = [[-2, -1], [1, 0]]
    >>> B = [[1], [0]]  # 2-D column vector
    >>> C = [[1, 2]]    # 2-D row vector
    >>> D = 1

    to the transfer function:

    .. math:: H(s) = \frac{s^2 + 3s + 3}{s^2 + 2s + 1}

    >>> from scipy.signal import ss2tf
    >>> ss2tf(A, B, C, D)
    (array([[1., 3., 3.]]), array([ 1.,  2.,  1.]))
    """
    ...

def zpk2ss(z, p, k):
    """Zero-pole-gain representation to state-space representation

    Parameters
    ----------
    z, p : sequence
        Zeros and poles.
    k : float
        System gain.

    Returns
    -------
    A, B, C, D : ndarray
        State space representation of the system, in controller canonical
        form.

    """
    ...

def ss2zpk(A, B, C, D, input=...): # -> tuple[NDArray[complexfloating[Any, Any]] | NDArray[floating[Any]], NDArray[complexfloating[Any, Any]] | NDArray[floating[Any]], Any]:
    """State-space representation to zero-pole-gain representation.

    A, B, C, D defines a linear state-space system with `p` inputs,
    `q` outputs, and `n` state variables.

    Parameters
    ----------
    A : array_like
        State (or system) matrix of shape ``(n, n)``
    B : array_like
        Input matrix of shape ``(n, p)``
    C : array_like
        Output matrix of shape ``(q, n)``
    D : array_like
        Feedthrough (or feedforward) matrix of shape ``(q, p)``
    input : int, optional
        For multiple-input systems, the index of the input to use.

    Returns
    -------
    z, p : sequence
        Zeros and poles.
    k : float
        System gain.

    """
    ...

def cont2discrete(system, dt, method=..., alpha=...):
    """
    Transform a continuous to a discrete state-space system.

    Parameters
    ----------
    system : a tuple describing the system or an instance of `lti`
        The following gives the number of elements in the tuple and
        the interpretation:

            * 1: (instance of `lti`)
            * 2: (num, den)
            * 3: (zeros, poles, gain)
            * 4: (A, B, C, D)

    dt : float
        The discretization time step.
    method : str, optional
        Which method to use:

            * gbt: generalized bilinear transformation
            * bilinear: Tustin's approximation ("gbt" with alpha=0.5)
            * euler: Euler (or forward differencing) method ("gbt" with alpha=0)
            * backward_diff: Backwards differencing ("gbt" with alpha=1.0)
            * zoh: zero-order hold (default)
            * foh: first-order hold (*versionadded: 1.3.0*)
            * impulse: equivalent impulse response (*versionadded: 1.3.0*)

    alpha : float within [0, 1], optional
        The generalized bilinear transformation weighting parameter, which
        should only be specified with method="gbt", and is ignored otherwise

    Returns
    -------
    sysd : tuple containing the discrete system
        Based on the input type, the output will be of the form

        * (num, den, dt)   for transfer function input
        * (zeros, poles, gain, dt)   for zeros-poles-gain input
        * (A, B, C, D, dt) for state-space system input

    Notes
    -----
    By default, the routine uses a Zero-Order Hold (zoh) method to perform
    the transformation. Alternatively, a generalized bilinear transformation
    may be used, which includes the common Tustin's bilinear approximation,
    an Euler's method technique, or a backwards differencing technique.

    The Zero-Order Hold (zoh) method is based on [1]_, the generalized bilinear
    approximation is based on [2]_ and [3]_, the First-Order Hold (foh) method
    is based on [4]_.

    Examples
    --------
    We can transform a continuous state-space system to a discrete one:

    >>> import matplotlib.pyplot as plt
    >>> from scipy.signal import cont2discrete, lti, dlti, dstep

    Define a continuous state-space system.

    >>> A = np.array([[0, 1],[-10., -3]])
    >>> B = np.array([[0],[10.]])
    >>> C = np.array([[1., 0]])
    >>> D = np.array([[0.]])
    >>> l_system = lti(A, B, C, D)
    >>> t, x = l_system.step(T=np.linspace(0, 5, 100))
    >>> fig, ax = plt.subplots()
    >>> ax.plot(t, x, label='Continuous', linewidth=3)

    Transform it to a discrete state-space system using several methods.

    >>> dt = 0.1
    >>> for method in ['zoh', 'bilinear', 'euler', 'backward_diff', 'foh', 'impulse']:
    ...    d_system = cont2discrete((A, B, C, D), dt, method=method)
    ...    s, x_d = dstep(d_system)
    ...    ax.step(s, np.squeeze(x_d), label=method, where='post')
    >>> ax.axis([t[0], t[-1], x[0], 1.4])
    >>> ax.legend(loc='best')
    >>> fig.tight_layout()
    >>> plt.show()

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Discretization#Discretization_of_linear_state_space_models

    .. [2] http://techteach.no/publications/discretetime_signals_systems/discrete.pdf

    .. [3] G. Zhang, X. Chen, and T. Chen, Digital redesign via the generalized
        bilinear transformation, Int. J. Control, vol. 82, no. 4, pp. 741-754,
        2009.
        (https://www.mypolyuweb.hk/~magzhang/Research/ZCC09_IJC.pdf)

    .. [4] G. F. Franklin, J. D. Powell, and M. L. Workman, Digital control
        of dynamic systems, 3rd ed. Menlo Park, Calif: Addison-Wesley,
        pp. 204-206, 1998.

    """
    ...

