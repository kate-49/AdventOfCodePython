import unittest
import day1pt1
import day1pt2

class TestDay1(unittest.TestCase):
    def test_part_one(self):
        kate = day1pt1.Day1("test_input.txt")
        assert kate.calculate() == 11, "Should be 11"

    def test_real_answer(self):
        kate = day1pt1.Day1('real_input.txt')
        real_answer = kate.calculate()
        assert real_answer == 2430334, "Expected 2430334"

    def test_part_two(self):
        kate = day1pt2.Day1Pt2("test_input.txt")
        assert kate.calculate() == 31, "Should be 31"

    def test_real_answer_part_two(self):
        kate = day1pt2.Day1Pt2('real_input.txt')
        real_answer = kate.calculate()
        assert real_answer == 2430334, "Expected 2430334"


if __name__ == '__main__':
    unittest.main()