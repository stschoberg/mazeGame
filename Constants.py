WHITE_COLOR_RGB = (255,255,255)
BLACK_COLOR_RGB = (0,0,0)
RED_COLOR_RGB = (255, 0, 0)
GREEN_COLOR_RGB = (0, 255, 0)
BLUE_COLOR_RGB = (0, 0, 255)
WIDTH = 500
NUM_ROWS = 10
NUM_EPISODES=1000
EPSILON = 3 # Integer 1-10. 2 = 20% random, 3 = 30% random ...
CELL_SIZE = WIDTH/NUM_ROWS
ACTIONS = ['left', 'right', 'up', 'down']
TERMINAL_CELLS = [(4, 5), (7, 4)]
CELL_VALUES = [((2, 0), -10),
((2, 1), -10),
((2, 2), -10),
((2, 3), -10),
((2, 4), -10),
((2, 5), -10),
((2, 6), -10),
((2, 7), -10),
((2, 8), -10),
((4, 5), 50),
((7, 4), 30)]
