"""Unit-тесты для модуля circle.py (площадь круга и длина окружности).

Ожидаемые значения посчитаны вручную по формулам из справочника:
    S = pi * r^2,   P = 2 * pi * r
Код самого модуля circle.py не изменяется.
"""
import unittest

import circle


class CircleAreaTestCase(unittest.TestCase):
    """circle.area(r) -- площадь круга."""

    def test_unit_radius(self):
        # Пример из справочника: area(1) = pi
        self.assertAlmostEqual(circle.area(1), 3.141592653589793)

    def test_integer_radius(self):
        # pi * 2^2 = 4 * pi
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_float_radius(self):
        # pi * 0.5^2 = pi / 4
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)

    def test_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_large_radius(self):
        # pi * 1000^2
        self.assertAlmostEqual(circle.area(1000), 3141592.653589793, delta=1e-6)

    def test_returns_float(self):
        self.assertIsInstance(circle.area(1), float)


class CirclePerimeterTestCase(unittest.TestCase):
    """circle.perimeter(r) -- длина окружности."""

    def test_unit_radius(self):
        # 2 * pi * 1
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586)

    def test_integer_radius(self):
        # Пример из справочника: perimeter(2) = 4 * pi
        self.assertAlmostEqual(circle.perimeter(2), 12.566370614359172)

    def test_float_radius(self):
        # 2 * pi * 0.5 = pi
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793)

    def test_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_large_radius(self):
        # 2 * pi * 1000
        self.assertAlmostEqual(circle.perimeter(1000), 6283.185307179586, delta=1e-6)

    def test_returns_float(self):
        self.assertIsInstance(circle.perimeter(1), float)


class CircleInvalidInputTestCase(unittest.TestCase):
    """Недопустимые данные (в справочнике поведение не описано).

    Радиус не может быть отрицательным, поэтому ожидаем ошибку ValueError.
    Если функции не проверяют вход, эти тесты упадут -- это результат
    тестирования (найденный дефект), его нужно описать в отчёте.
    """

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)


if __name__ == "__main__":
    unittest.main()
