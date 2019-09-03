def classify_triangle(sides):
    if min(sides) <= 0:
        return False
    if sum(sorted(sides)[:-1]) < sorted(sides)[-1]:
        return False
    return True


def equilateral(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y == z
    else:
        return False


def isosceles(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x == y or y == z or z == x
    else:
        return False

def right(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x*x+y*y==z*z or x*x+z*z==y*y or y*y+z*z==x*x
    else:
        return False

def scalene(sides):
    triangle = classify_triangle(sides)
    if triangle:
        x, y, z = sides
        return x!=y and y!=z and z!=x
    else:
        return False
  
import unittest

from triangle import equilateral, isosceles, scalene

class TestEquilateralTriangle(unittest.TestCase):
    def test_all_sides_are_equal(self):
        self.assertIs(equilateral([1, 1, 1]), True)

    def test_all_zero_sides_is_not_a_triangle(self):
        self.assertIs(equilateral([0, 0, 0]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([1, 5, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(equilateral([0.5, 0.5, 0.5]), True)


class TestIsoscelesTriangle(unittest.TestCase):
    def test_last_two_sides_are_equal(self):
        self.assertIs(isosceles([6, 8, 8]), True)

    def test_equilateral_triangles_are_also_isosceles(self):
        self.assertIs(isosceles([2, 2, 2]), True)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([5, 1, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(isosceles([0.1, 0.1, 0.15]), True)


class TestScaleneTriangle(unittest.TestCase):
    def test_no_sides_are_equal(self):
        self.assertIs(scalene([3, 4, 5]), True)

    def test_all_sides_are_equal(self):
        self.assertIs(scalene([2, 2, 2]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([1, 1, 11]), False)

class TestrightTriangle(unittest.TestCase):
    def test_rhght(self):
        self.assertIs(scalene([3, 4, 5]), True)

    def test_all_sides_are_equal(self):
        self.assertIs(scalene([2, 2, 2]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([1, 1, 11]), False)
if __name__ == "__main__":
    unittest.main()
