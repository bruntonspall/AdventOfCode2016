import unittest
import timer


class TimerTest(unittest.TestCase):
    def test_find(self):
        self.assertEquals(5, timer.find_solution([(5, 4), (2, 1)]))
        self.assertEquals(4, timer.find_solution([(5, 0)]))

        self.assertEquals(16824, timer.find_solution([(17, 5), (19, 8),
                                                      (7, 1), (13, 7),
                                                      (5, 1), (3, 0)]))

        self.assertEquals(3543984, timer.find_solution([(17, 5), (19, 8),
                                                        (7, 1), (13, 7),
                                                        (5, 1), (3, 0),
                                                        (11, 0)]))
