"""
Vectors with metods:
-adding
-substracting
-multiplying per scalar
-comparing lenght
"""
import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(v1, v2):
        result_vector = [v1.x + v2.x, v1.y + v2.y]
        return result_vector

    def __sub__(v1, v2):
        result_vector = [v1.x - v2.x, v1.y - v2.y]
        return result_vector

    def __mul__(v1, number):
        return [v1.x * number, v1.y * number]

    def compare_lenght(v1, v2):
        v1_len = math.sqrt(v1.x**2 + v1.y**2)
        v2_len = math.sqrt(v2.x**2 + v2.y**2)
        if v1_len > v2_len:
            return v1
        elif v1_len < v2_len:
            return v2
        else:
            return "equal"

vec1 = Vector(1, 2)
vec2 = Vector(3, 4)
vec3 = Vector(3, 4)
vec4 = Vector(1, 12)

def test_adding():
    assert vec1 + vec2 == [4, 6]

def test_substracting():
    assert vec2 - vec1 == [2, 2]
    assert vec1 - vec2 == [-2, -2]

def test_multiplying_per_scalar():
    assert vec1 * 2 == [2, 4]
    assert vec2 * 3 == [9, 12]

def test_length_compare():
    assert Vector.compare_lenght(vec3, vec2) == "equal"
    assert Vector.compare_lenght(vec1, vec2) == vec2
    assert Vector.compare_lenght(vec1, vec4) == vec4
