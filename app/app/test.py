# Simple tests

from django.test import SimpleTestCase

from app.calc import add, subtract


class SimpleTests(SimpleTestCase):
    def test_add_numbers(self):
        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = subtract(5, 6)

        self.assertEqual(res, 1)
