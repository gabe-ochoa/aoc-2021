import unittest
from one import Day01


class Test01(unittest.TestCase):
    def test_num_instances(self):
        input_list = '''199
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
        output = Day01.num_increases(input_list)
        self.assertEqual(answer, output)

    def test_measurement_window(self):
        input_list = '''
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263'''
        answer = [607, 618, 618, 617, 647, 716, 769, 792]
        output = Day01.measurement_windows(input_list)
        self.assertEqual(output, answer)


if __name__ == '__main__':
    unittest.main()
