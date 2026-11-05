"""Unit-тесты для модуля triangle.py (площадь и периметр треугольника).

Формулы: S = a * h / 2,  P = a + b + c
Код самого модуля triangle.py не изменяется.
"""
import unittest

import triangle


class TriangleAreaTestCase(unittest.TestCase):
    """triangle.area(a, h) -- площадь по основанию и высоте."""

    def test_integer_values(self):
        # Пример из справочника: area(10, 3) = 15.0
        self.assertEqual(triangle.area(10, 3), 15.0)

    def test_pythagorean_values(self):
        # Пример из README: area(5, 12) = 30.0
        self.assertEqual(triangle.area(5, 12), 30.0)

    def test_zero_base(self):
        self.assertEqual(triangle.area(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(triangle.area(3, 0), 0)

    def test_float_values(self):
        self.assertAlmostEqual(triangle.area(2.5, 4), 5.0)

    def test_unit_values(self):
        self.assertAlmostEqual(triangle.area(1, 1), 0.5)


class TrianglePerimeterTestCase(unittest.TestCase):
    """triangle.perimeter(a, b, c) -- периметр по трём сторонам."""

    def test_right_triangle(self):
        # Пример из справочника: perimeter(3, 4, 5) = 12
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_pythagorean_values(self):
        # Пример из README: perimeter(5, 12, 13) = 30
        self.assertEqual(triangle.perimeter(5, 12, 13), 30)

    def test_equilateral(self):
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)

    def test_float_sides(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3), 7.0)

    def test_zero_sides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)


class TriangleInvalidInputTestCase(unittest.TestCase):
    """Недопустимые данные.

    Ожидаем ValueError для отрицательных значений и для сторон, из которых
    нельзя составить треугольник (нарушено неравенство треугольника).
    Если функции не проверяют вход, тесты упадут -- это результат
    тестирования, его нужно описать в отчёте.
    """

    def test_area_negative_base(self):
        with self.assertRaises(ValueError):
            triangle.area(-10, 3)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)

    def test_perimeter_triangle_inequality(self):
        # 1 + 1 < 10: такого треугольника не существует
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 10)


if __name__ == "__main__":
    unittest.main()
