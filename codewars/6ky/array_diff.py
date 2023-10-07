import unittest


def array_diff(a, b):
    return [x for x in a if x not in b]


class TestArrayDiff(unittest.TestCase):

    def test_basic_test_cases(self):
        self.assertEqual(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
        self.assertEqual(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")


if __name__ == '__main__':
    unittest.main()
