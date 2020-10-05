import ddt
import unittest

from src.main import add


@ddt.ddt
class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add(1, 2), 3)

    @ddt.data(
        (), {}, [], None, 'Some str', sum, object
    )
    def test_bad_value(self, failed_value):
        """Test that add function returns 'Bad value' on {failed_value} value"""
        self.assertEqual(add(failed_value, 1), 'Bad value')


if __name__ == '__main__':
    unittest.main()
