from Constants import NUM_ROWS, CELL_VALUES, TERMINAL_CELLS

class Board(object):
    cellValues = {} # Maps cell (x, y) to reward r

    def __init__(self, numRows = NUM_ROWS):
        self.numRows = numRows
        self.initCellRewards()

    def initCellRewards(self):
        for xPos in range(NUM_ROWS):
            for yPos in range(NUM_ROWS):
                self.cellValues[(xPos, yPos)] = 0

    def createPenaltyCells(self):
        for cell, val in CELL_VALUES:
            self.cellValues[cell[0], cell[1]] = val

    def isTerminalCell(self, coord):
        return coord in TERMINAL_CELLS

    def isValidCell(self, coord, action):
        xCoord, yCoord = self.getCellAfterAction(coord, action)
        return (0 <= xCoord < NUM_ROWS  and 0 <= yCoord < NUM_ROWS)

    def getCellAfterAction(self, coord, action):
        xCoord, yCoord = coord
        if action == 'left':
            xCoord-=1
        elif action == 'right':
            xCoord+=1
        elif action == 'up':
            yCoord+=1
        elif action == 'down':
            yCoord-=1

        return (xCoord, yCoord)

    def getCellValue(self, coord):
        return self.cellValues[coord]

    def getCells(self):
        return self.cellValues.keys()

    def getCellMap(self):
        return self.cellValues

    def getRewardCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val > 0}

    def getPenaltyCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val < 0}
