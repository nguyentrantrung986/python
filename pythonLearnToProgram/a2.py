# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        >>> rat1 = Rat('P', 1, 1)
        >>> rat1.symbol
        'P'
        >>> rat1.row
        1
        >>> rat1.num_sprouts_eaten
        0
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
    
    def set_location(self, new_row, new_col):
        """ (Rat, int, int) -> NoneType

        set the location of the rat to new_row and new_col
        >>> rat1 = Rat('P', 1, 1)
        >>> rat1.set_location(3, 4)
        >>> rat1.row
        3
        >>> rat1.col
        4
        """

        self.row = new_row
        self.col = new_col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Yuck
        >>> rat1 = Rat('P', 1, 1)
        >>> rat1.eat_sprout()
        >>> rat1.num_sprouts_eaten
        1
        >>> rat1.eat_sprout()
        >>> rat1.num_sprouts_eaten
        2
        """

        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """ (Rat) -> str

        return the string representation of the rat
        >>> rat2 = Rat('J', 4, 3)
        >>> rat2.eat_sprout()
        >>> rat2.eat_sprout()
        >>> print(rat2)
        J at (4, 3) ate 2 sprouts.
        """
        
        return '{0} at ({1}, {2}) ate {3} sprouts.'.\
             format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        initialize a maze with the content and 2 rats
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
            ['#', '.', '.', '.', '.', '.', '#'], \
            ['#', '.', '#', '#', '#', '.', '#'], \
            ['#', '.', '.', '@', '#', '.', '#'], \
            ['#', '@', '#', '.', '@', '.', '#'], \
            ['#', '#', '#', '#', '#', '#', '#']], \
            Rat('J', 1, 1),\
            Rat('P', 1, 4))
        >>> maze.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for lis in self.maze:
            self.num_sprouts_left = self.num_sprouts_left + lis.count(SPROUT)

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        return true if there is a wall at row and col
        >>> maze = Maze([['.', '#'], ['.','@']], Rat('J',1,0), Rat('P',0,0))
        >>> maze.is_wall(0, 1)
        True
        >>> maze.is_wall(1, 1)
        False
        """
        
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should
        be returned rather than HALL.
        >>> maze = Maze([['.','#'],['.','@'],['#','.']], Rat('J',1,0), Rat('P',0,0))
        >>> maze.get_character(2,1)
        '.'
        >>> maze.get_character(1,0)
        'J'
        >>> maze.get_character(0,1)
        '#'
        >>> maze.get_character(1,1)
        '@'
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        if self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        return self.maze[row][col]

    def move(self, rat, v_direction, h_direction):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given directions, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location and, if present:
        - have the rat eat the Brussels sprout,
        - make that location a HALL, and
        - decrease the value that num_sprouts_left refers to by one.
        - Return True if and only if there wasn't a wall in the way.

        >>> maze = Maze([['.','#'],['.','@'],['#','.']], Rat('J',1,0), Rat('P',0,0))
        >>> maze.move(maze.rat_2, DOWN, NO_CHANGE)
        True
        >>> print(maze.rat_2)
        P at (1, 0) ate 0 sprouts.
        >>> maze.move(maze.rat_2, NO_CHANGE, RIGHT)
        True
        >>> print(maze.rat_2)
        P at (1, 1) ate 1 sprouts.
        >>> maze.num_sprouts_left
        0
        """

        new_row = rat.row + v_direction
        new_col = rat.col + h_direction
        if new_row >= len(self.maze) or new_row < 0 or \
           new_col >= len(self.maze[0]) or new_col < 0 or \
           self.maze[new_row][new_col] == WALL:
            return False
        
        rat.set_location(new_row, new_col)
        if self.maze[new_row][new_col] == SPROUT:
            rat.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left = self.num_sprouts_left - 1
            
        return True

    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the maze
        >>> maze = Maze([['.','#'],['.','@'],['#','.']], Rat('J',1,0), Rat('P',0,0))
        >>> print(maze)
        P#
        J@
        #.
        J at (1, 0) ate 0 sprouts.
        P at (0, 0) ate 0 sprouts.
        """

        maze_string = ''
        width = len(self.maze)
        height = len(self.maze[0])
        for row in range(width):
            for col in range(height):
                if row == self.rat_1.row and col == self.rat_1.col:
                    maze_string = maze_string + self.rat_1.symbol
                elif row == self.rat_2.row and col == self.rat_2.col:
                    maze_string = maze_string + self.rat_2.symbol
                else:
                    maze_string = maze_string + self.maze[row][col]
            maze_string = maze_string + '\n'

        maze_string = maze_string + str(self.rat_1) + '\n' + \
                      str(self.rat_2)

        return maze_string
        
if __name__ ==  '__main__':
    import doctest
    doctest.testmod()
