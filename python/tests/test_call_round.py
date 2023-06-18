import unittest
import source.functions.call_round as call_round

class TestCallRound(unittest.TestCase):
    def test_get_call_sequence(self):
        seq = call_round.get_call_sequence(0)
        self.assertEqual(seq, [0, 1, 2, 3])

        seq = call_round.get_call_sequence(1)
        self.assertEqual(seq, [1, 2, 3, 0])

        seq = call_round.get_call_sequence(2)
        self.assertEqual(seq, [2, 3, 0, 1])

        seq = call_round.get_call_sequence(3)
        self.assertEqual(seq, [3, 0, 1, 2])
