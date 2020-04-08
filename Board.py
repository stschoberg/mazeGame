NUM_ROWS = 10

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
        for i in range(7):
            self.cellValues[(5, i)] = -10
        for i in range(8, 11):
            self.cellValues[(5, i)] = -10

        self.cellValues[0, 9] = 10
        self.cellValues[9, 9] = 50


    def getCellRewards(self, player):
        return self.cellValues[player.currLocation]

    def getCellReward(self, cellCoords):
        return self.cellValues[cellCoords]

    def getCellMap(self):
        return self.cellValues

    def getRewardCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val > 0}

    def getPenaltyCellsMap(self):
        return {cell: val for cell, val in self.cellValues.items() if val < 0}
