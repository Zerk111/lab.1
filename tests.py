import unittest
from logic import analyze_movement

class TestMovementAnalysis(unittest.TestCase):
    def test_acceleration(self):
        status, _ = analyze_movement([0, 10, 20, 30, 40])
        self.assertEqual(status, "ACCELERATION")
    def test_braking(self):
        status, _ = analyze_movement([50, 40, 30, 20, 10])
        self.assertEqual(status, "BRAKING")
    def test_violation(self):
        status, idx = analyze_movement([10, 20, 30, 15, 5])
        self.assertEqual(status, "VIOLATION")
        self.assertEqual(idx, 3)

if __name__ == '__main__':
    unittest.main()