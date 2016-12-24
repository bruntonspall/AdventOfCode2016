import unittest
import maze


class MazeTest(unittest.TestCase):
    def test_generate_maze(self):
        m = maze.Maze(10)
        self.assertEquals(0, m.get((0, 0)))
        self.assertEquals(1, m.get((1, 0)))
        self.assertEquals(0, m.get((2, 0)))
        self.assertEquals(0, m.get((0, 1)))
        self.assertEquals(0, m.get((1, 1)))
        self.assertEquals(1, m.get((2, 1)))
        self.assertEquals(1, m.get((0, 2)))
        self.assertEquals(0, m.get((1, 2)))
        self.assertEquals(0, m.get((2, 2)))

    def test_find_route(self):
        m = maze.Maze(10)
        route = m.find_route((0, 0), (1, 1))
        self.assertEquals([(0, 0), (0, 1), (1, 1)], route)
        route = m.find_route((1, 1), (7, 4))
        self.assertEquals([(1, 1),
                           (1, 2),
                           (2, 2),
                           (3, 2),
                           (3, 3),
                           (3, 4),
                           (4, 4),
                           (4, 5),
                           (5, 5),
                           (6, 5),
                           (7, 5),
                           (7, 4)], route)
        self.assertEquals(12, len(route))

    def test_countable_in_distance(self):
        m = maze.Maze(10)
        nearby = m.nearby((1, 1), 1)
        self.assertEquals([(0, 1), (1, 1), (1, 2)], sorted(nearby))
        self.assertEquals(3, len(nearby))
        self.assertEquals(5, len(m.nearby((1, 1), 2)))
        self.assertEquals(6, len(m.nearby((1, 1), 3)))
