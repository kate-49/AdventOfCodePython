import unittest
import day1

class TestDay1(unittest.TestCase):
    def test_part_one(self):
        kate = day1.Day1(56)
        assert kate.calculate() == 56, "Should be something"
        self.assertEqual(56, kate.calculate())

if __name__ == '__main__':
    unittest.main()