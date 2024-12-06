import unittest
import day1

class TestDay1(unittest.TestCase):
    def test_part_one(self):
        kate = day1.Day1("test_input.txt")
        assert kate.calculate() == 11, "Should be 11"

    def test_real_answer(self):
        kate = day1.Day1('real_input.txt')
        realAnswer = kate.calculate()
        assert realAnswer == 11, "Expected 11 but got " +  str(realAnswer)
# 494 too low
if __name__ == '__main__':
    unittest.main()