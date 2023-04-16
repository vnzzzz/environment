"""
This type stub file was generated by pyright.
"""

from ._data import _minmax_mixin
from ._compressed import _cs_matrix

"""Compressed Block Sparse Row matrix format"""
__docformat__ = ...
__all__ = ['bsr_matrix', 'isspmatrix_bsr']
class bsr_matrix(_cs_matrix, _minmax_mixin):
    """Block Sparse Row matrix

    This can be instantiated in several ways:
        bsr_matrix(D, [blocksize=(R,C)])
            where D is a dense matrix or 2-D ndarray.

        bsr_matrix(S, [blocksize=(R,C)])
            with another sparse matrix S (equivalent to S.tobsr())

        bsr_matrix((M, N), [blocksize=(R,C), dtype])
            to construct an empty matrix with shape (M, N)
            dtype is optional, defaulting to dtype='d'.

        bsr_matrix((data, ij), [blocksize=(R,C), shape=(M, N)])
            where ``data`` and ``ij`` satisfy ``a[ij[0, k], ij[1, k]] = data[k]``

        bsr_matrix((data, indices, indptr), [shape=(M, N)])
            is the standard BSR representation where the block column
            indices for row i are stored in ``indices[indptr[i]:indptr[i+1]]``
            and their corresponding block values are stored in
            ``data[ indptr[i]: indptr[i+1] ]``. If the shape parameter is not
            supplied, the matrix dimensions are inferred from the index arrays.

    Attributes
    ----------
    dtype : dtype
        Data type of the matrix
    shape : 2-tuple
        Shape of the matrix
    ndim : int
        Number of dimensions (this is always 2)
    nnz
        Number of stored values, including explicit zeros
    data
        Data array of the matrix
    indices
        BSR format index array
    indptr
        BSR format index pointer array
    blocksize
        Block size of the matrix
    has_sorted_indices
        Whether indices are sorted

    Notes
    -----
    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    **Summary of BSR format**

    The Block Compressed Row (BSR) format is very similar to the Compressed
    Sparse Row (CSR) format. BSR is appropriate for sparse matrices with dense
    sub matrices like the last example below.  Block matrices often arise in
    vector-valued finite element discretizations. In such cases, BSR is
    considerably more efficient than CSR and CSC for many sparse arithmetic
    operations.

    **Blocksize**

    The blocksize (R,C) must evenly divide the shape of the matrix (M,N).
    That is, R and C must satisfy the relationship ``M % R = 0`` and
    ``N % C = 0``.

    If no blocksize is specified, a simple heuristic is applied to determine
    an appropriate blocksize.

    Examples
    --------
    >>> from scipy.sparse import bsr_matrix
    >>> bsr_matrix((3, 4), dtype=np.int8).toarray()
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]], dtype=int8)

    >>> row = np.array([0, 0, 1, 2, 2, 2])
    >>> col = np.array([0, 2, 2, 0, 1, 2])
    >>> data = np.array([1, 2, 3 ,4, 5, 6])
    >>> bsr_matrix((data, (row, col)), shape=(3, 3)).toarray()
    array([[1, 0, 2],
           [0, 0, 3],
           [4, 5, 6]])

    >>> indptr = np.array([0, 2, 3, 6])
    >>> indices = np.array([0, 2, 2, 0, 1, 2])
    >>> data = np.array([1, 2, 3, 4, 5, 6]).repeat(4).reshape(6, 2, 2)
    >>> bsr_matrix((data,indices,indptr), shape=(6, 6)).toarray()
    array([[1, 1, 0, 0, 2, 2],
           [1, 1, 0, 0, 2, 2],
           [0, 0, 0, 0, 3, 3],
           [0, 0, 0, 0, 3, 3],
           [4, 4, 5, 5, 6, 6],
           [4, 4, 5, 5, 6, 6]])

    """
    format = ...
    def __init__(self, arg1, shape=..., dtype=..., copy=..., blocksize=...) -> None:
        ...
    
    def check_format(self, full_check=...):
        """check whether the matrix format is valid

            *Parameters*:
                full_check:
                    True  - rigorous check, O(N) operations : default
                    False - basic check, O(1) operations

        """
        ...
    
    blocksize = ...
    def getnnz(self, axis=...): # -> int:
        ...
    
    def __repr__(self): # -> Any:
        ...
    
    def diagonal(self, k=...): # -> NDArray[Unknown] | NDArray[bool_ | csingle | single | byte | ubyte]:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, val):
        ...
    
    def tobsr(self, blocksize=..., copy=...): # -> bsr_matrix | Self@bsr_matrix:
        """Convert this matrix into Block Sparse Row Format.

        With copy=False, the data/indices may be shared between this
        matrix and the resultant bsr_matrix.

        If blocksize=(R, C) is provided, it will be used for determining
        block size of the bsr_matrix.
        """
        ...
    
    def tocsr(self, copy=...): # -> csr_matrix:
        ...
    
    def tocsc(self, copy=...): # -> csc_matrix:
        ...
    
    def tocoo(self, copy=...): # -> coo_matrix:
        """Convert this matrix to COOrdinate format.

        When copy=False the data array will be shared between
        this matrix and the resultant coo_matrix.
        """
        ...
    
    def toarray(self, order=..., out=...): # -> NDArray[float64]:
        ...
    
    def transpose(self, axes=..., copy=...): # -> bsr_matrix:
        ...
    
    def eliminate_zeros(self): # -> None:
        """Remove zero elements in-place."""
        ...
    
    def sum_duplicates(self): # -> None:
        """Eliminate duplicate matrix entries by adding them together

        The is an *in place* operation
        """
        ...
    
    def sort_indices(self): # -> None:
        """Sort the indices of this matrix *in place*
        """
        ...
    
    def prune(self): # -> None:
        """ Remove empty space after all non-zero elements.
        """
        ...
    


def isspmatrix_bsr(x): # -> bool:
    """Is x of a bsr_matrix type?

    Parameters
    ----------
    x
        object to check for being a bsr matrix

    Returns
    -------
    bool
        True if x is a bsr matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import bsr_matrix, isspmatrix_bsr
    >>> isspmatrix_bsr(bsr_matrix([[5]]))
    True

    >>> from scipy.sparse import bsr_matrix, csr_matrix, isspmatrix_bsr
    >>> isspmatrix_bsr(csr_matrix([[5]]))
    False
    """
    ...

