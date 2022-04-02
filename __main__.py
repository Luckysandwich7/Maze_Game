import random

from maze import Maze
from credits import Credit

# Easy to read representation for each cardinal direction.
N, S, W, E = ('n', 's', 'w', 'e')


class MazeGame(object):
    """
    Class for interactively playing random maze games.
    """
    def __init__(self, maze):
        self.maze = maze or Maze.generate()

    def _get_random_position(self):
        """
        Returns a random position on the maze.
        """
        return (random.randrange(0, self.maze.width),
                random.randrange(0, self.maze.height))

    def _display(self, pos, value):
        """
        Displays a value on the screen from an x and y maze positions.
        """
        x, y = pos
        # Double x position because displayed maze is double-wide.
        console.set_display(y * 2 + 1, x * 4 + 2, value)

    def play(self):
        """
        Starts an interactive game on this maze, with random starting and goal
        positions. Returns True if the user won, or False if player quit the game
        by pressing "q".
        """
        player = self._get_random_position()
        target = self._get_random_position()

        while player != target:
            console.display(str(self.maze))
            self._display(player, '@')
            self._display(target, '$')

            key = console.get_valid_key(['up', 'down', 'left', 'right', 'q'])

            if key == 'q':
                return False

            direction, difx, dify = {'up': (N, 0, -1),
                                     'down': (S, 0, 1),
                                     'left': (W, -1, 0),
                                     'right': (E, 1, 0)}[key]

            current_cell = self.maze[player]
            if direction not in current_cell:
                player = (player[0] + difx, player[1] + dify)

        console.display('You win!')
        console.get_key()
        return True

    message = "You Win!"

    credits = Credit()
    message.set_text_end(credits.getCredits())
    credits.add_actor("messages", message)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        width = int(sys.argv[1])
        if len(sys.argv) > 2:
            height = int(sys.argv[2])
        else:
            height = width
    else:
        width = 20
        height = 10

    import console
    try:
        while MazeGame(Maze.generate(width, height)).play(): pass
    except:
        import traceback
        traceback.print_exc(file=open('error_log.txt', 'a'))
        
