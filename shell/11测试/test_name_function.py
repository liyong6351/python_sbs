import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    def test_first_name(self):
        formatted_name = get_formated_name("hello","world")
        self.assertEqual(formatted_name,"Hello World")

    def test_first_middle_last_name(self):
        name = get_formated_name("hello","greate","python")
        self.assertEqual(name,"Hello Greate Python")

unittest.main()