NUM_ROWS = 10

class Board(object):
    cellValues = {} # Maps cell (x, y) to reward r

    def __init__(self, numRows = NUM_ROWS):
        self.numRows = numRows
        self.initCellRewards()

    def initCellRewards(self):
        for xPos in range(NUM_ROWS):
            for yPos in range(NUM_ROWS):
                self.cellValues[(xPos, yPos)] = 50

    def getCellRewards(self, player):
        return self.cellValues[player.currLocation]

    def getCellReward(self, cellCoords):
        return self.cellValues[cellCoords]

    def getCellMap(self):
        return self.cellValues

    def getRewardCellsMap(self):
        return dict(filter(lambda cellMap: cellMap[1] > 0, self.cellValues.items()))

    def getPenaltyCellsMap(self):
        return dict(filter(lambda cellMap: cellMap[1] < 0, self.cellValues.items()))
