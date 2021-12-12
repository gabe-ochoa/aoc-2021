import unittest
from one import Day01


class Test01(unittest.TestCase):
    def test_num_instances(self):
        input = '''199
200
208
210
200
207
240
269
260
263'''
        answer = 7
        output = Day01.num_increases(input)
        self.assertEqual(answer, output)


if __name__ == '__main__':
    unittest.main()
