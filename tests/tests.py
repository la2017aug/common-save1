import unittest
from math import sqrt

from homework import Rectangle


class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(2, 2)
        self.rectangle2 = Rectangle(4, 2)
        self.rectangle3 = Rectangle(2, 4)
        self.rectangle4 = Rectangle(2.2, 2.2)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rectangle1.get_rectangle_perimeter(), 8)
        self.assertEqual(self.rectangle2.get_rectangle_perimeter(), 12)
        self.assertEqual(self.rectangle3.get_rectangle_perimeter(), 12)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rectangle1.get_rectangle_square(), 4)
        self.assertEqual(self.rectangle2.get_rectangle_square(), 8)
        self.assertEqual(self.rectangle3.get_rectangle_square(), 8)

    def test_get_sum_of_corners(self):
        for i in range(0, 5):
            self.assertEqual(self.rectangle1.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rectangle2.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rectangle3.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_corners_error(self):
        with self.assertRaises(ValueError):
            self.rectangle1.get_sum_of_corners(5)
            self.rectangle2.get_sum_of_corners(5)
            self.rectangle3.get_sum_of_corners(5)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rectangle1.get_rectangle_diagonal(),
                         sqrt(8))
        self.assertEqual(self.rectangle2.get_rectangle_diagonal(),
                         sqrt(20))
        self.assertEqual(self.rectangle3.get_rectangle_diagonal(),
                         sqrt(20))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(
            self.rectangle1.get_radius_of_circumscribed_circle(),
            sqrt(8) / 2)
        self.assertEqual(
            self.rectangle2.get_radius_of_circumscribed_circle(),
            sqrt(20) / 2)
        self.assertEqual(
            self.rectangle3.get_radius_of_circumscribed_circle(),
            sqrt(20) / 2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertEqual(
            self.rectangle1.get_radius_of_inscribed_circle(),
            sqrt(pow(2, 2) + pow(2, 2)) / (2 * sqrt(2)))
        self.assertEqual(
            self.rectangle4.get_radius_of_inscribed_circle(),
            sqrt(pow(2.2, 2) + pow(2.2, 2)) / (2 * sqrt(2)))
        with self.assertRaises(ValueError):
            self.rectangle2.get_radius_of_inscribed_circle()
            self.rectangle3.get_radius_of_inscribed_circle()


if __name__ == '__main__':
    unittest.main()
