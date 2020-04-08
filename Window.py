import pygame

WHITE_COLOR_RGB = (255,255,255)
BLACK_COLOR_RGB = (0,0,0)
RED_COLOR_RGB = (255, 0, 0)
GREEN_COLOR_RGB = (0, 255, 0)
BLUE_COLOR_RGB = (0, 0, 255)
WIDTH = 500
NUM_ROWS = 10
CELL_SIZE = WIDTH/NUM_ROWS

class Window(object):
    def __init__(self, width=WIDTH):
        self.surface = pygame.display.set_mode((width, width))
        self.width_pxs = width

    def drawSurface(self, board, player):
        self.fillSurfaceWithColor()
        self.drawGridLines()
        self.drawRewardAndPenaltySquares(board)
        self.drawPlayer(player)
        pygame.display.update()

    def fillSurfaceWithColor(self, color=BLACK_COLOR_RGB):
        self.surface.fill(color)

    def drawGridLines(self, numRows=NUM_ROWS, lineColor=WHITE_COLOR_RGB):
        xPos = 0
        yPos = 0
        spaceWidth = self.width_pxs / numRows

        for i in range(numRows):
            xPos+=spaceWidth
            yPos+=spaceWidth

            pygame.draw.line(self.surface, lineColor, (xPos,0),(xPos,self.width_pxs))
            pygame.draw.line(self.surface, lineColor, (0,yPos),(self.width_pxs,yPos))

    def drawPlayer(self, player):
        playerCurrXCoord, playerCurrYCoord = player.getCurrCoords()
        # Divisions need to be casted for pygame circle function
        radius = int(CELL_SIZE/2)
        centerPoint = (int(playerCurrXCoord*CELL_SIZE + CELL_SIZE/2),
                        int(playerCurrYCoord*CELL_SIZE + CELL_SIZE/2))
        # Player is a circle in a cell
        pygame.draw.circle(self.surface, BLUE_COLOR_RGB,centerPoint, radius)

    def drawRewardAndPenaltySquares(self, board):
        cellsWithRewards = board.getRewardCellsMap().keys()
        cellsWithPenalties = board.getPenaltyCellsMap().keys()

        for c in cellsWithPenalties: self.colorCell(color=RED_COLOR_RGB, cell=c)
        for c in cellsWithRewards: self.colorCell(color=GREEN_COLOR_RGB, cell=c)

    def colorCell(self, cell, color, cellSize=WIDTH/NUM_ROWS):
        xCoord, yCoord = cell
        pygame.draw.rect(
            self.surface,
            color,
            (xCoord*cellSize+1,yCoord*cellSize+1, cellSize-2, cellSize-2)
            )

    def getsurfaceWidth(self):
        return self.width_pxs

    def getsurface(self):
        return self.surface
