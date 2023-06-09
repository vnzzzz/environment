"""
This type stub file was generated by pyright.
"""

import sys
import numpy as np
import types as _types
import importlib as _importlib
from numpy import __version__ as __numpy_version__, show_config as show_numpy_config
from ._lib.deprecation import _deprecated
from numpy.random import rand, randn
from numpy.fft import ifft
from numpy.lib import scimath
from scipy.version import version as __version__
from . import _distributor_init
from scipy._lib import _pep440
from scipy._lib._testutils import PytestTester

"""
SciPy: A scientific computing package for Python
================================================

Documentation is available in the docstrings and
online at https://docs.scipy.org.

Contents
--------
SciPy imports all the functions from the NumPy namespace, and in
addition provides:

Subpackages
-----------
Using any of these subpackages requires an explicit import. For example,
``import scipy.cluster``.

::

 cluster                      --- Vector Quantization / Kmeans
 fft                          --- Discrete Fourier transforms
 fftpack                      --- Legacy discrete Fourier transforms
 integrate                    --- Integration routines
 interpolate                  --- Interpolation Tools
 io                           --- Data input and output
 linalg                       --- Linear algebra routines
 linalg.blas                  --- Wrappers to BLAS library
 linalg.lapack                --- Wrappers to LAPACK library
 misc                         --- Various utilities that don't have
                                  another home.
 ndimage                      --- N-D image package
 odr                          --- Orthogonal Distance Regression
 optimize                     --- Optimization Tools
 signal                       --- Signal Processing Tools
 signal.windows               --- Window functions
 sparse                       --- Sparse Matrices
 sparse.linalg                --- Sparse Linear Algebra
 sparse.linalg.dsolve         --- Linear Solvers
 sparse.linalg.dsolve.umfpack --- :Interface to the UMFPACK library:
                                  Conjugate Gradient Method (LOBPCG)
 sparse.linalg.eigen          --- Sparse Eigenvalue Solvers
 sparse.linalg.eigen.lobpcg   --- Locally Optimal Block Preconditioned
                                  Conjugate Gradient Method (LOBPCG)
 spatial                      --- Spatial data structures and algorithms
 special                      --- Special functions
 stats                        --- Statistical Functions

Utility tools
-------------
::

 test              --- Run scipy unittests
 show_config       --- Show scipy build configuration
 show_numpy_config --- Show numpy build configuration
 __version__       --- SciPy version string
 __numpy_version__ --- Numpy version string

"""
if sys.version_info >= (3, 12):
    ...
if show_numpy_config is None:
    ...
_msg = ...
_msg = ...
rand = ...
randn = ...
ifft = ...
_msg = ...
if __SCIPY_SETUP__:
    ...
else:
    np_minversion = ...
    np_maxversion = ...
    test = ...
    submodules = ...
    def __dir__(): # -> list[str]:
        ...
    
    def __getattr__(name): # -> ModuleType | Any:
        ...
    
