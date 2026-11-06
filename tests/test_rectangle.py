
import unittest

import rectangle


class RectangleAreaTestCase(unittest.TestCase):


    def test_different_sides(self):     
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_zero_mul(self):

        self.assertEqual(rectangle.area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_float_sides(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10.0)

    def test_commutative(self):
        self.assertEqual(rectangle.area(3, 5), rectangle.area(5, 3))


class RectanglePerimeterTestCase(unittest.TestCase):
    """rectangle.perimeter(a, b) -- периметр прямоугольника."""

    def test_different_sides(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_zero_sides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_equal_sides(self):
        # 2 * (10 + 10)
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_float_sides(self):
        # 2 * (2.5 + 4)
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4), 13.0)

    def test_commutative(self):
        self.assertEqual(rectangle.perimeter(3, 5), rectangle.perimeter(5, 3))


class RectangleInvalidInputTestCase(unittest.TestCase):

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -5)


if __name__ == "__main__":
    unittest.main()
