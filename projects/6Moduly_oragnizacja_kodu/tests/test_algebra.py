"""
Testing algebra

"""

from mathematica.algebra.matrices import add_matrices, sub_matrices

def test_add_matrices():
    assert add_matrices(0, 0) == '+'

def test_substract_matrices():
    assert sub_matrices(0, 0) == '-'




