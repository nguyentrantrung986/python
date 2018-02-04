import unittest
import a2

class TestA2(unittest.TestCase):
    def test_move_1(self):
        """Test move out of range of the maze"""
        
        maze = a2.Maze([['.','#'],['.','@'],['#','.']], \
                       a2.Rat('J',1,0), a2.Rat('P',0,0))
        actual = maze.move(maze.rat_1,a2.NO_CHANGE,a2.LEFT)
        expected = False
        self.assertEqual(actual,expected)
        
        actual = maze.move(maze.rat_1,a2.NO_CHANGE,a2.RIGHT)
        expected = True
        self.assertEqual(actual,expected)

        actual = maze.move(maze.rat_1,a2.DOWN,a2.NO_CHANGE)
        actual = maze.move(maze.rat_1,a2.DOWN,a2.NO_CHANGE)
        expected = False
        self.assertEqual(actual,expected)

    def test_str_1(self):
        """Test __str__ when 2 rats at the same position"""
        maze = a2.Maze([['.','#'],['.','@'],['#','.']], \
                       a2.Rat('J',1,0), a2.Rat('P',1,0))
        actual = str(maze)
        expected = ('.#\nJ@\n#.'
                    '\nJ at (1, 0) ate 0 sprouts.'
                    '\nP at (1, 0) ate 0 sprouts.')
        self.assertEqual(actual,expected)

    def test_str_2(self):
        """Test __str__ after move"""
        maze = a2.Maze([['.','#'],['.','@'],['#','.']], \
                       a2.Rat('J',1,0), a2.Rat('P',1,0))
        maze.move(maze.rat_1,a2.NO_CHANGE,a2.RIGHT)
        actual = str(maze)
        expected = ('.#\nPJ\n#.'
                    '\nJ at (1, 1) ate 1 sprouts.'
                    '\nP at (1, 0) ate 0 sprouts.')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
