"""
testing for Geometry
"""

from mathematica.geometry import figures as f

def test_square_area():
    assert f.square_area(2, 3) == 6

def test_triangle_area():
    assert f.triangle_area(2, 2) == 2