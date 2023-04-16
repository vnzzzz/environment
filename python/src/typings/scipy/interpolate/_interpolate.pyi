"""
This type stub file was generated by pyright.
"""

from ._polyint import _Interpolator1D

__all__ = ['interp1d', 'interp2d', 'lagrange', 'PPoly', 'BPoly', 'NdPPoly']
def lagrange(x, w): # -> poly1d:
    r"""
    Return a Lagrange interpolating polynomial.

    Given two 1-D arrays `x` and `w,` returns the Lagrange interpolating
    polynomial through the points ``(x, w)``.

    Warning: This implementation is numerically unstable. Do not expect to
    be able to use more than about 20 points even if they are chosen optimally.

    Parameters
    ----------
    x : array_like
        `x` represents the x-coordinates of a set of datapoints.
    w : array_like
        `w` represents the y-coordinates of a set of datapoints, i.e., f(`x`).

    Returns
    -------
    lagrange : `numpy.poly1d` instance
        The Lagrange interpolating polynomial.

    Examples
    --------
    Interpolate :math:`f(x) = x^3` by 3 points.

    >>> from scipy.interpolate import lagrange
    >>> x = np.array([0, 1, 2])
    >>> y = x**3
    >>> poly = lagrange(x, y)

    Since there are only 3 points, Lagrange polynomial has degree 2. Explicitly,
    it is given by

    .. math::

        \begin{aligned}
            L(x) &= 1\times \frac{x (x - 2)}{-1} + 8\times \frac{x (x-1)}{2} \\
                 &= x (-2 + 3x)
        \end{aligned}

    >>> from numpy.polynomial.polynomial import Polynomial
    >>> Polynomial(poly.coef[::-1]).coef
    array([ 0., -2.,  3.])

    >>> import matplotlib.pyplot as plt
    >>> x_new = np.arange(0, 2.1, 0.1)
    >>> plt.scatter(x, y, label='data')
    >>> plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), label='Polynomial')
    >>> plt.plot(x_new, 3*x_new**2 - 2*x_new + 0*x_new,
    ...          label=r"$3 x^2 - 2 x$", linestyle='-.')
    >>> plt.legend()
    >>> plt.show()

    """
    ...

class interp2d:
    """
    interp2d(x, y, z, kind='linear', copy=True, bounds_error=False,
             fill_value=None)

    Interpolate over a 2-D grid.

    `x`, `y` and `z` are arrays of values used to approximate some function
    f: ``z = f(x, y)`` which returns a scalar value `z`. This class returns a
    function whose call method uses spline interpolation to find the value
    of new points.

    If `x` and `y` represent a regular grid, consider using
    `RectBivariateSpline`.

    If `z` is a vector value, consider using `interpn`.

    Note that calling `interp2d` with NaNs present in input values results in
    undefined behaviour.

    Methods
    -------
    __call__

    Parameters
    ----------
    x, y : array_like
        Arrays defining the data point coordinates.

        If the points lie on a regular grid, `x` can specify the column
        coordinates and `y` the row coordinates, for example::

          >>> x = [0,1,2];  y = [0,3]; z = [[1,2,3], [4,5,6]]

        Otherwise, `x` and `y` must specify the full coordinates for each
        point, for example::

          >>> x = [0,1,2,0,1,2];  y = [0,0,0,3,3,3]; z = [1,4,2,5,3,6]

        If `x` and `y` are multidimensional, they are flattened before use.
    z : array_like
        The values of the function to interpolate at the data points. If
        `z` is a multidimensional array, it is flattened before use assuming
        Fortran-ordering (order='F').  The length of a flattened `z` array
        is either len(`x`)*len(`y`) if `x` and `y` specify the column and
        row coordinates or ``len(z) == len(x) == len(y)`` if `x` and `y`
        specify coordinates for each point.
    kind : {'linear', 'cubic', 'quintic'}, optional
        The kind of spline interpolation to use. Default is 'linear'.
    copy : bool, optional
        If True, the class makes internal copies of x, y and z.
        If False, references may be used. The default is to copy.
    bounds_error : bool, optional
        If True, when interpolated values are requested outside of the
        domain of the input data (x,y), a ValueError is raised.
        If False, then `fill_value` is used.
    fill_value : number, optional
        If provided, the value to use for points outside of the
        interpolation domain. If omitted (None), values outside
        the domain are extrapolated via nearest-neighbor extrapolation.

    See Also
    --------
    RectBivariateSpline :
        Much faster 2-D interpolation if your input data is on a grid
    bisplrep, bisplev :
        Spline interpolation based on FITPACK
    BivariateSpline : a more recent wrapper of the FITPACK routines
    interp1d : 1-D version of this function

    Notes
    -----
    The minimum number of data points required along the interpolation
    axis is ``(k+1)**2``, with k=1 for linear, k=3 for cubic and k=5 for
    quintic interpolation.

    The interpolator is constructed by `bisplrep`, with a smoothing factor
    of 0. If more control over smoothing is needed, `bisplrep` should be
    used directly.

    Examples
    --------
    Construct a 2-D grid and interpolate on it:

    >>> from scipy import interpolate
    >>> x = np.arange(-5.01, 5.01, 0.25)
    >>> y = np.arange(-5.01, 5.01, 0.25)
    >>> xx, yy = np.meshgrid(x, y)
    >>> z = np.sin(xx**2+yy**2)
    >>> f = interpolate.interp2d(x, y, z, kind='cubic')

    Now use the obtained interpolation function and plot the result:

    >>> import matplotlib.pyplot as plt
    >>> xnew = np.arange(-5.01, 5.01, 1e-2)
    >>> ynew = np.arange(-5.01, 5.01, 1e-2)
    >>> znew = f(xnew, ynew)
    >>> plt.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
    >>> plt.show()
    """
    def __init__(self, x, y, z, kind=..., copy=..., bounds_error=..., fill_value=...) -> None:
        ...
    
    def __call__(self, x, y, dx=..., dy=..., assume_sorted=...):
        """Interpolate the function.

        Parameters
        ----------
        x : 1-D array
            x-coordinates of the mesh on which to interpolate.
        y : 1-D array
            y-coordinates of the mesh on which to interpolate.
        dx : int >= 0, < kx
            Order of partial derivatives in x.
        dy : int >= 0, < ky
            Order of partial derivatives in y.
        assume_sorted : bool, optional
            If False, values of `x` and `y` can be in any order and they are
            sorted first.
            If True, `x` and `y` have to be arrays of monotonically
            increasing values.

        Returns
        -------
        z : 2-D array with shape (len(y), len(x))
            The interpolated values.
        """
        ...
    


class interp1d(_Interpolator1D):
    """
    Interpolate a 1-D function.

    `x` and `y` are arrays of values used to approximate some function f:
    ``y = f(x)``. This class returns a function whose call method uses
    interpolation to find the value of new points.

    Parameters
    ----------
    x : (N,) array_like
        A 1-D array of real values.
    y : (...,N,...) array_like
        A N-D array of real values. The length of `y` along the interpolation
        axis must be equal to the length of `x`.
    kind : str or int, optional
        Specifies the kind of interpolation as a string or as an integer
        specifying the order of the spline interpolator to use.
        The string has to be one of 'linear', 'nearest', 'nearest-up', 'zero',
        'slinear', 'quadratic', 'cubic', 'previous', or 'next'. 'zero',
        'slinear', 'quadratic' and 'cubic' refer to a spline interpolation of
        zeroth, first, second or third order; 'previous' and 'next' simply
        return the previous or next value of the point; 'nearest-up' and
        'nearest' differ when interpolating half-integers (e.g. 0.5, 1.5)
        in that 'nearest-up' rounds up and 'nearest' rounds down. Default
        is 'linear'.
    axis : int, optional
        Specifies the axis of `y` along which to interpolate.
        Interpolation defaults to the last axis of `y`.
    copy : bool, optional
        If True, the class makes internal copies of x and y.
        If False, references to `x` and `y` are used. The default is to copy.
    bounds_error : bool, optional
        If True, a ValueError is raised any time interpolation is attempted on
        a value outside of the range of x (where extrapolation is
        necessary). If False, out of bounds values are assigned `fill_value`.
        By default, an error is raised unless ``fill_value="extrapolate"``.
    fill_value : array-like or (array-like, array_like) or "extrapolate", optional
        - if a ndarray (or float), this value will be used to fill in for
          requested points outside of the data range. If not provided, then
          the default is NaN. The array-like must broadcast properly to the
          dimensions of the non-interpolation axes.
        - If a two-element tuple, then the first element is used as a
          fill value for ``x_new < x[0]`` and the second element is used for
          ``x_new > x[-1]``. Anything that is not a 2-element tuple (e.g.,
          list or ndarray, regardless of shape) is taken to be a single
          array-like argument meant to be used for both bounds as
          ``below, above = fill_value, fill_value``. Using a two-element tuple
          or ndarray requires ``bounds_error=False``.

          .. versionadded:: 0.17.0
        - If "extrapolate", then points outside the data range will be
          extrapolated.

          .. versionadded:: 0.17.0
    assume_sorted : bool, optional
        If False, values of `x` can be in any order and they are sorted first.
        If True, `x` has to be an array of monotonically increasing values.

    Attributes
    ----------
    fill_value

    Methods
    -------
    __call__

    See Also
    --------
    splrep, splev
        Spline interpolation/smoothing based on FITPACK.
    UnivariateSpline : An object-oriented wrapper of the FITPACK routines.
    interp2d : 2-D interpolation

    Notes
    -----
    Calling `interp1d` with NaNs present in input values results in
    undefined behaviour.

    Input values `x` and `y` must be convertible to `float` values like
    `int` or `float`.

    If the values in `x` are not unique, the resulting behavior is
    undefined and specific to the choice of `kind`, i.e., changing
    `kind` will change the behavior for duplicates.


    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from scipy import interpolate
    >>> x = np.arange(0, 10)
    >>> y = np.exp(-x/3.0)
    >>> f = interpolate.interp1d(x, y)

    >>> xnew = np.arange(0, 9, 0.1)
    >>> ynew = f(xnew)   # use interpolation function returned by `interp1d`
    >>> plt.plot(x, y, 'o', xnew, ynew, '-')
    >>> plt.show()
    """
    def __init__(self, x, y, kind=..., axis=..., copy=..., bounds_error=..., fill_value=..., assume_sorted=...) -> None:
        """ Initialize a 1-D linear interpolation class."""
        ...
    
    @property
    def fill_value(self): # -> tuple[Unknown, ...] | NDArray[Unknown]:
        """The fill value."""
        ...
    
    @fill_value.setter
    def fill_value(self, fill_value): # -> None:
        ...
    


class _PPolyBase:
    """Base class for piecewise polynomials."""
    __slots__ = ...
    def __init__(self, c, x, extrapolate=..., axis=...) -> None:
        ...
    
    @classmethod
    def construct_fast(cls, c, x, extrapolate=..., axis=...): # -> Self@_PPolyBase:
        """
        Construct the piecewise polynomial without making checks.

        Takes the same parameters as the constructor. Input arguments
        ``c`` and ``x`` must be arrays of the correct shape and type. The
        ``c`` array can only be of dtypes float and complex, and ``x``
        array must have dtype float.
        """
        ...
    
    def extend(self, c, x):
        """
        Add additional breakpoints and coefficients to the polynomial.

        Parameters
        ----------
        c : ndarray, size (k, m, ...)
            Additional coefficients for polynomials in intervals. Note that
            the first additional interval will be formed using one of the
            ``self.x`` end points.
        x : ndarray, size (m,)
            Additional breakpoints. Must be sorted in the same order as
            ``self.x`` and either to the right or to the left of the current
            breakpoints.
        """
        ...
    
    def __call__(self, x, nu=..., extrapolate=...): # -> ndarray[Any, dtype[complex_ | float_]]:
        """
        Evaluate the piecewise polynomial or its derivative.

        Parameters
        ----------
        x : array_like
            Points to evaluate the interpolant at.
        nu : int, optional
            Order of derivative to evaluate. Must be non-negative.
        extrapolate : {bool, 'periodic', None}, optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used.
            If None (default), use `self.extrapolate`.

        Returns
        -------
        y : array_like
            Interpolated values. Shape is determined by replacing
            the interpolation axis in the original array with the shape of x.

        Notes
        -----
        Derivatives are evaluated piecewise for each polynomial
        segment, even if the polynomial is not differentiable at the
        breakpoints. The polynomial intervals are considered half-open,
        ``[a, b)``, except for the last interval which is closed
        ``[a, b]``.
        """
        ...
    


class PPoly(_PPolyBase):
    """
    Piecewise polynomial in terms of coefficients and breakpoints

    The polynomial between ``x[i]`` and ``x[i + 1]`` is written in the
    local power basis::

        S = sum(c[m, i] * (xp - x[i])**(k-m) for m in range(k+1))

    where ``k`` is the degree of the polynomial.

    Parameters
    ----------
    c : ndarray, shape (k, m, ...)
        Polynomial coefficients, order `k` and `m` intervals.
    x : ndarray, shape (m+1,)
        Polynomial breakpoints. Must be sorted in either increasing or
        decreasing order.
    extrapolate : bool or 'periodic', optional
        If bool, determines whether to extrapolate to out-of-bounds points
        based on first and last intervals, or to return NaNs. If 'periodic',
        periodic extrapolation is used. Default is True.
    axis : int, optional
        Interpolation axis. Default is zero.

    Attributes
    ----------
    x : ndarray
        Breakpoints.
    c : ndarray
        Coefficients of the polynomials. They are reshaped
        to a 3-D array with the last dimension representing
        the trailing dimensions of the original coefficient array.
    axis : int
        Interpolation axis.

    Methods
    -------
    __call__
    derivative
    antiderivative
    integrate
    solve
    roots
    extend
    from_spline
    from_bernstein_basis
    construct_fast

    See also
    --------
    BPoly : piecewise polynomials in the Bernstein basis

    Notes
    -----
    High-order polynomials in the power basis can be numerically
    unstable. Precision problems can start to appear for orders
    larger than 20-30.
    """
    def derivative(self, nu=...): # -> Self@PPoly:
        """
        Construct a new piecewise polynomial representing the derivative.

        Parameters
        ----------
        nu : int, optional
            Order of derivative to evaluate. Default is 1, i.e., compute the
            first derivative. If negative, the antiderivative is returned.

        Returns
        -------
        pp : PPoly
            Piecewise polynomial of order k2 = k - n representing the derivative
            of this polynomial.

        Notes
        -----
        Derivatives are evaluated piecewise for each polynomial
        segment, even if the polynomial is not differentiable at the
        breakpoints. The polynomial intervals are considered half-open,
        ``[a, b)``, except for the last interval which is closed
        ``[a, b]``.
        """
        ...
    
    def antiderivative(self, nu=...): # -> Self@PPoly:
        """
        Construct a new piecewise polynomial representing the antiderivative.

        Antiderivative is also the indefinite integral of the function,
        and derivative is its inverse operation.

        Parameters
        ----------
        nu : int, optional
            Order of antiderivative to evaluate. Default is 1, i.e., compute
            the first integral. If negative, the derivative is returned.

        Returns
        -------
        pp : PPoly
            Piecewise polynomial of order k2 = k + n representing
            the antiderivative of this polynomial.

        Notes
        -----
        The antiderivative returned by this function is continuous and
        continuously differentiable to order n-1, up to floating point
        rounding error.

        If antiderivative is computed and ``self.extrapolate='periodic'``,
        it will be set to False for the returned instance. This is done because
        the antiderivative is no longer periodic and its correct evaluation
        outside of the initially given x interval is difficult.
        """
        ...
    
    def integrate(self, a, b, extrapolate=...):
        """
        Compute a definite integral over a piecewise polynomial.

        Parameters
        ----------
        a : float
            Lower integration bound
        b : float
            Upper integration bound
        extrapolate : {bool, 'periodic', None}, optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used.
            If None (default), use `self.extrapolate`.

        Returns
        -------
        ig : array_like
            Definite integral of the piecewise polynomial over [a, b]
        """
        ...
    
    def solve(self, y=..., discontinuity=..., extrapolate=...): # -> ndarray[Any, dtype[Any]]:
        """
        Find real solutions of the equation ``pp(x) == y``.

        Parameters
        ----------
        y : float, optional
            Right-hand side. Default is zero.
        discontinuity : bool, optional
            Whether to report sign changes across discontinuities at
            breakpoints as roots.
        extrapolate : {bool, 'periodic', None}, optional
            If bool, determines whether to return roots from the polynomial
            extrapolated based on first and last intervals, 'periodic' works
            the same as False. If None (default), use `self.extrapolate`.

        Returns
        -------
        roots : ndarray
            Roots of the polynomial(s).

            If the PPoly object describes multiple polynomials, the
            return value is an object array whose each element is an
            ndarray containing the roots.

        Notes
        -----
        This routine works only on real-valued polynomials.

        If the piecewise polynomial contains sections that are
        identically zero, the root list will contain the start point
        of the corresponding interval, followed by a ``nan`` value.

        If the polynomial is discontinuous across a breakpoint, and
        there is a sign change across the breakpoint, this is reported
        if the `discont` parameter is True.

        Examples
        --------

        Finding roots of ``[x**2 - 1, (x - 1)**2]`` defined on intervals
        ``[-2, 1], [1, 2]``:

        >>> from scipy.interpolate import PPoly
        >>> pp = PPoly(np.array([[1, -4, 3], [1, 0, 0]]).T, [-2, 1, 2])
        >>> pp.solve()
        array([-1.,  1.])
        """
        ...
    
    def roots(self, discontinuity=..., extrapolate=...): # -> ndarray[Any, dtype[Any]]:
        """
        Find real roots of the piecewise polynomial.

        Parameters
        ----------
        discontinuity : bool, optional
            Whether to report sign changes across discontinuities at
            breakpoints as roots.
        extrapolate : {bool, 'periodic', None}, optional
            If bool, determines whether to return roots from the polynomial
            extrapolated based on first and last intervals, 'periodic' works
            the same as False. If None (default), use `self.extrapolate`.

        Returns
        -------
        roots : ndarray
            Roots of the polynomial(s).

            If the PPoly object describes multiple polynomials, the
            return value is an object array whose each element is an
            ndarray containing the roots.

        See Also
        --------
        PPoly.solve
        """
        ...
    
    @classmethod
    def from_spline(cls, tck, extrapolate=...): # -> Self@PPoly:
        """
        Construct a piecewise polynomial from a spline

        Parameters
        ----------
        tck
            A spline, as returned by `splrep` or a BSpline object.
        extrapolate : bool or 'periodic', optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used. Default is True.
        """
        ...
    
    @classmethod
    def from_bernstein_basis(cls, bp, extrapolate=...): # -> Self@PPoly:
        """
        Construct a piecewise polynomial in the power basis
        from a polynomial in Bernstein basis.

        Parameters
        ----------
        bp : BPoly
            A Bernstein basis polynomial, as created by BPoly
        extrapolate : bool or 'periodic', optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used. Default is True.
        """
        ...
    


class BPoly(_PPolyBase):
    """Piecewise polynomial in terms of coefficients and breakpoints.

    The polynomial between ``x[i]`` and ``x[i + 1]`` is written in the
    Bernstein polynomial basis::

        S = sum(c[a, i] * b(a, k; x) for a in range(k+1)),

    where ``k`` is the degree of the polynomial, and::

        b(a, k; x) = binom(k, a) * t**a * (1 - t)**(k - a),

    with ``t = (x - x[i]) / (x[i+1] - x[i])`` and ``binom`` is the binomial
    coefficient.

    Parameters
    ----------
    c : ndarray, shape (k, m, ...)
        Polynomial coefficients, order `k` and `m` intervals
    x : ndarray, shape (m+1,)
        Polynomial breakpoints. Must be sorted in either increasing or
        decreasing order.
    extrapolate : bool, optional
        If bool, determines whether to extrapolate to out-of-bounds points
        based on first and last intervals, or to return NaNs. If 'periodic',
        periodic extrapolation is used. Default is True.
    axis : int, optional
        Interpolation axis. Default is zero.

    Attributes
    ----------
    x : ndarray
        Breakpoints.
    c : ndarray
        Coefficients of the polynomials. They are reshaped
        to a 3-D array with the last dimension representing
        the trailing dimensions of the original coefficient array.
    axis : int
        Interpolation axis.

    Methods
    -------
    __call__
    extend
    derivative
    antiderivative
    integrate
    construct_fast
    from_power_basis
    from_derivatives

    See also
    --------
    PPoly : piecewise polynomials in the power basis

    Notes
    -----
    Properties of Bernstein polynomials are well documented in the literature,
    see for example [1]_ [2]_ [3]_.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Bernstein_polynomial

    .. [2] Kenneth I. Joy, Bernstein polynomials,
       http://www.idav.ucdavis.edu/education/CAGDNotes/Bernstein-Polynomials.pdf

    .. [3] E. H. Doha, A. H. Bhrawy, and M. A. Saker, Boundary Value Problems,
           vol 2011, article ID 829546, :doi:`10.1155/2011/829543`.

    Examples
    --------
    >>> from scipy.interpolate import BPoly
    >>> x = [0, 1]
    >>> c = [[1], [2], [3]]
    >>> bp = BPoly(c, x)

    This creates a 2nd order polynomial

    .. math::

        B(x) = 1 \\times b_{0, 2}(x) + 2 \\times b_{1, 2}(x) + 3 \\times b_{2, 2}(x) \\\\
             = 1 \\times (1-x)^2 + 2 \\times 2 x (1 - x) + 3 \\times x^2

    """
    def derivative(self, nu=...): # -> Self@BPoly:
        """
        Construct a new piecewise polynomial representing the derivative.

        Parameters
        ----------
        nu : int, optional
            Order of derivative to evaluate. Default is 1, i.e., compute the
            first derivative. If negative, the antiderivative is returned.

        Returns
        -------
        bp : BPoly
            Piecewise polynomial of order k - nu representing the derivative of
            this polynomial.

        """
        ...
    
    def antiderivative(self, nu=...): # -> Self@BPoly:
        """
        Construct a new piecewise polynomial representing the antiderivative.

        Parameters
        ----------
        nu : int, optional
            Order of antiderivative to evaluate. Default is 1, i.e., compute
            the first integral. If negative, the derivative is returned.

        Returns
        -------
        bp : BPoly
            Piecewise polynomial of order k + nu representing the
            antiderivative of this polynomial.

        Notes
        -----
        If antiderivative is computed and ``self.extrapolate='periodic'``,
        it will be set to False for the returned instance. This is done because
        the antiderivative is no longer periodic and its correct evaluation
        outside of the initially given x interval is difficult.
        """
        ...
    
    def integrate(self, a, b, extrapolate=...): # -> NDArray[complexfloating[Any, Any]]:
        """
        Compute a definite integral over a piecewise polynomial.

        Parameters
        ----------
        a : float
            Lower integration bound
        b : float
            Upper integration bound
        extrapolate : {bool, 'periodic', None}, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs. If 'periodic', periodic
            extrapolation is used. If None (default), use `self.extrapolate`.

        Returns
        -------
        array_like
            Definite integral of the piecewise polynomial over [a, b]

        """
        ...
    
    def extend(self, c, x):
        ...
    
    @classmethod
    def from_power_basis(cls, pp, extrapolate=...): # -> Self@BPoly:
        """
        Construct a piecewise polynomial in Bernstein basis
        from a power basis polynomial.

        Parameters
        ----------
        pp : PPoly
            A piecewise polynomial in the power basis
        extrapolate : bool or 'periodic', optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used. Default is True.
        """
        ...
    
    @classmethod
    def from_derivatives(cls, xi, yi, orders=..., extrapolate=...):
        """Construct a piecewise polynomial in the Bernstein basis,
        compatible with the specified values and derivatives at breakpoints.

        Parameters
        ----------
        xi : array_like
            sorted 1-D array of x-coordinates
        yi : array_like or list of array_likes
            ``yi[i][j]`` is the ``j``th derivative known at ``xi[i]``
        orders : None or int or array_like of ints. Default: None.
            Specifies the degree of local polynomials. If not None, some
            derivatives are ignored.
        extrapolate : bool or 'periodic', optional
            If bool, determines whether to extrapolate to out-of-bounds points
            based on first and last intervals, or to return NaNs.
            If 'periodic', periodic extrapolation is used. Default is True.

        Notes
        -----
        If ``k`` derivatives are specified at a breakpoint ``x``, the
        constructed polynomial is exactly ``k`` times continuously
        differentiable at ``x``, unless the ``order`` is provided explicitly.
        In the latter case, the smoothness of the polynomial at
        the breakpoint is controlled by the ``order``.

        Deduces the number of derivatives to match at each end
        from ``order`` and the number of derivatives available. If
        possible it uses the same number of derivatives from
        each end; if the number is odd it tries to take the
        extra one from y2. In any case if not enough derivatives
        are available at one end or another it draws enough to
        make up the total from the other end.

        If the order is too high and not enough derivatives are available,
        an exception is raised.

        Examples
        --------

        >>> from scipy.interpolate import BPoly
        >>> BPoly.from_derivatives([0, 1], [[1, 2], [3, 4]])

        Creates a polynomial `f(x)` of degree 3, defined on `[0, 1]`
        such that `f(0) = 1, df/dx(0) = 2, f(1) = 3, df/dx(1) = 4`

        >>> BPoly.from_derivatives([0, 1, 2], [[0, 1], [0], [2]])

        Creates a piecewise polynomial `f(x)`, such that
        `f(0) = f(1) = 0`, `f(2) = 2`, and `df/dx(0) = 1`.
        Based on the number of derivatives provided, the order of the
        local polynomials is 2 on `[0, 1]` and 1 on `[1, 2]`.
        Notice that no restriction is imposed on the derivatives at
        ``x = 1`` and ``x = 2``.

        Indeed, the explicit form of the polynomial is::

            f(x) = | x * (1 - x),  0 <= x < 1
                   | 2 * (x - 1),  1 <= x <= 2

        So that f'(1-0) = -1 and f'(1+0) = 2

        """
        ...
    


class NdPPoly:
    """
    Piecewise tensor product polynomial

    The value at point ``xp = (x', y', z', ...)`` is evaluated by first
    computing the interval indices `i` such that::

        x[0][i[0]] <= x' < x[0][i[0]+1]
        x[1][i[1]] <= y' < x[1][i[1]+1]
        ...

    and then computing::

        S = sum(c[k0-m0-1,...,kn-mn-1,i[0],...,i[n]]
                * (xp[0] - x[0][i[0]])**m0
                * ...
                * (xp[n] - x[n][i[n]])**mn
                for m0 in range(k[0]+1)
                ...
                for mn in range(k[n]+1))

    where ``k[j]`` is the degree of the polynomial in dimension j. This
    representation is the piecewise multivariate power basis.

    Parameters
    ----------
    c : ndarray, shape (k0, ..., kn, m0, ..., mn, ...)
        Polynomial coefficients, with polynomial order `kj` and
        `mj+1` intervals for each dimension `j`.
    x : ndim-tuple of ndarrays, shapes (mj+1,)
        Polynomial breakpoints for each dimension. These must be
        sorted in increasing order.
    extrapolate : bool, optional
        Whether to extrapolate to out-of-bounds points based on first
        and last intervals, or to return NaNs. Default: True.

    Attributes
    ----------
    x : tuple of ndarrays
        Breakpoints.
    c : ndarray
        Coefficients of the polynomials.

    Methods
    -------
    __call__
    derivative
    antiderivative
    integrate
    integrate_1d
    construct_fast

    See also
    --------
    PPoly : piecewise polynomials in 1D

    Notes
    -----
    High-order polynomials in the power basis can be numerically
    unstable.

    """
    def __init__(self, c, x, extrapolate=...) -> None:
        ...
    
    @classmethod
    def construct_fast(cls, c, x, extrapolate=...): # -> Self@NdPPoly:
        """
        Construct the piecewise polynomial without making checks.

        Takes the same parameters as the constructor. Input arguments
        ``c`` and ``x`` must be arrays of the correct shape and type.  The
        ``c`` array can only be of dtypes float and complex, and ``x``
        array must have dtype float.

        """
        ...
    
    def __call__(self, x, nu=..., extrapolate=...): # -> ndarray[Any, dtype[complex_ | float_]]:
        """
        Evaluate the piecewise polynomial or its derivative

        Parameters
        ----------
        x : array-like
            Points to evaluate the interpolant at.
        nu : tuple, optional
            Orders of derivatives to evaluate. Each must be non-negative.
        extrapolate : bool, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.

        Returns
        -------
        y : array-like
            Interpolated values. Shape is determined by replacing
            the interpolation axis in the original array with the shape of x.

        Notes
        -----
        Derivatives are evaluated piecewise for each polynomial
        segment, even if the polynomial is not differentiable at the
        breakpoints. The polynomial intervals are considered half-open,
        ``[a, b)``, except for the last interval which is closed
        ``[a, b]``.

        """
        ...
    
    def derivative(self, nu): # -> Self@NdPPoly:
        """
        Construct a new piecewise polynomial representing the derivative.

        Parameters
        ----------
        nu : ndim-tuple of int
            Order of derivatives to evaluate for each dimension.
            If negative, the antiderivative is returned.

        Returns
        -------
        pp : NdPPoly
            Piecewise polynomial of orders (k[0] - nu[0], ..., k[n] - nu[n])
            representing the derivative of this polynomial.

        Notes
        -----
        Derivatives are evaluated piecewise for each polynomial
        segment, even if the polynomial is not differentiable at the
        breakpoints. The polynomial intervals in each dimension are
        considered half-open, ``[a, b)``, except for the last interval
        which is closed ``[a, b]``.

        """
        ...
    
    def antiderivative(self, nu): # -> Self@NdPPoly:
        """
        Construct a new piecewise polynomial representing the antiderivative.

        Antiderivative is also the indefinite integral of the function,
        and derivative is its inverse operation.

        Parameters
        ----------
        nu : ndim-tuple of int
            Order of derivatives to evaluate for each dimension.
            If negative, the derivative is returned.

        Returns
        -------
        pp : PPoly
            Piecewise polynomial of order k2 = k + n representing
            the antiderivative of this polynomial.

        Notes
        -----
        The antiderivative returned by this function is continuous and
        continuously differentiable to order n-1, up to floating point
        rounding error.

        """
        ...
    
    def integrate_1d(self, a, b, axis, extrapolate=...): # -> Self@NdPPoly:
        r"""
        Compute NdPPoly representation for one dimensional definite integral

        The result is a piecewise polynomial representing the integral:

        .. math::

           p(y, z, ...) = \int_a^b dx\, p(x, y, z, ...)

        where the dimension integrated over is specified with the
        `axis` parameter.

        Parameters
        ----------
        a, b : float
            Lower and upper bound for integration.
        axis : int
            Dimension over which to compute the 1-D integrals
        extrapolate : bool, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.

        Returns
        -------
        ig : NdPPoly or array-like
            Definite integral of the piecewise polynomial over [a, b].
            If the polynomial was 1D, an array is returned,
            otherwise, an NdPPoly object.

        """
        ...
    
    def integrate(self, ranges, extrapolate=...): # -> NDArray[Unknown] | NDArray[complex_ | float_] | Any:
        """
        Compute a definite integral over a piecewise polynomial.

        Parameters
        ----------
        ranges : ndim-tuple of 2-tuples float
            Sequence of lower and upper bounds for each dimension,
            ``[(a[0], b[0]), ..., (a[ndim-1], b[ndim-1])]``
        extrapolate : bool, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.

        Returns
        -------
        ig : array_like
            Definite integral of the piecewise polynomial over
            [a[0], b[0]] x ... x [a[ndim-1], b[ndim-1]]

        """
        ...
    


