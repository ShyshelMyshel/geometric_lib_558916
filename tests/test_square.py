"""Unit-тесты для модуля square.py (площадь и периметр квадрата).

Формулы: S = a^2,  P = 4 * a
Код самого модуля square.py не изменяется.
"""
import unittest

import square


class SquareAreaTestCase(unittest.TestCase):
    """square.area(a) -- площадь квадрата."""

    def test_integer_side(self):
        # Пример из справочника: area(3) = 9
        self.assertEqual(square.area(3), 9)

    def test_unit_side(self):
        self.assertEqual(square.area(1), 1)

    def test_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_float_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_large_side(self):
        self.assertEqual(square.area(1000000), 10 ** 12)


class SquarePerimeterTestCase(unittest.TestCase):
    """square.perimeter(a) -- периметр квадрата."""

    def test_integer_side(self):
        # Пример из справочника: perimeter(4) = 16
        self.assertEqual(square.perimeter(4), 16)

    def test_unit_side(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_float_side(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_large_side(self):
        self.assertEqual(square.perimeter(1000000), 4000000)


class SquareInvalidInputTestCase(unittest.TestCase):
    """Недопустимые данные: сторона не может быть отрицательной.

    Если функции не проверяют вход, тесты упадут -- это результат
    тестирования, его нужно описать в отчёте.
    """

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-3)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)


if __name__ == "__main__":
    unittest.main()
