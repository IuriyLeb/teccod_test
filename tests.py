import unittest
from unique_values import get_unique_values
from primes import primes_list
from strings_sort import merge_sort_asc, merge_sort_desc
from point import Point


class TaskTest(unittest.TestCase):

    def test_task_1(self):

        self.assertEqual(get_unique_values(['a', 'aa', 'aaa', 'a', 'aa', 'aaa']).sort(),
                         ['a', 'aa', 'aaa'].sort())

        self.assertEqual(get_unique_values(['a', 'ba', 'aba', 'b', 'ba', 'aba']).sort(),
                         ['ca', 'aba'].sort())

    def test_task_2(self):

        self.assertEqual(primes_list(5, 20).sort(),
                         [5, 7, 11, 13, 17, 19].sort())

        self.assertEqual(primes_list(1, 7).sort(),
                         [1, 2, 3, 5, 7].sort())

    def test_task_3(self):
        a = Point(5, 6)
        b = Point(0, -1)

        self.assertIsInstance(a, Point)
        self.assertIsInstance(b, Point)

        self.assertEqual(a.get_coordinates(), [5, 6])
        self.assertEqual(b.get_coordinates(), [0, -1])

        self.assertEqual(a.distance(b), [-5, -7])
        self.assertEqual(b.distance(a), [5, 7])

        a.set_coordinates(0,0)
        b.set_coordinates(0,0)

        self.assertEqual(a.get_coordinates(), [0, 0])
        self.assertEqual(b.get_coordinates(), [0, 0])

    def test_task_4(self):
        self.assertEqual(merge_sort_asc(['a', 'aa', 'aaa', 'a', 'aa', 'aaa']),
                         sorted(['a', 'a', 'aa', 'aa', 'aaa', 'aaa'], key=len))

        self.assertEqual(merge_sort_asc(['a', 'ba', 'aab', 'b', 'aa', 'aaa']),
                         sorted(['a', 'ba', 'aab', 'b', 'aa', 'aaa'], key=len))

        self.assertEqual(merge_sort_desc(['a', 'aa', 'aaa', 'a', 'aa', 'aaa']),
                         sorted(['a', 'a', 'aa', 'aa', 'aaa', 'aaa'], key=len, reverse=True))

        self.assertEqual(merge_sort_desc(['a', 'ba', 'aab', 'b', 'aa', 'aaa']),
                         sorted(['a', 'ba', 'aab', 'b', 'aa', 'aaa'], key=len, reverse=True))
