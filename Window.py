import pygame
from Constants import (WHITE_COLOR_RGB, BLACK_COLOR_RGB, RED_COLOR_RGB,
GREEN_COLOR_RGB, BLUE_COLOR_RGB, WIDTH,NUM_ROWS, CELL_SIZE)

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
    def updateSurface(self, player):
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
        cellsWithRewards = board.getRewardCellsMap()
        cellsWithPenalties = board.getPenaltyCellsMap()

        # Color the cells
        for c in cellsWithPenalties.keys(): self.colorCell(color=RED_COLOR_RGB, cell=c)
        for c in cellsWithRewards.keys(): self.colorCell(color=GREEN_COLOR_RGB, cell=c)

        # Print values on cells
        for cell, value in cellsWithPenalties.items(): self.drawCellValue(cell, value)
        for cell, value in cellsWithRewards.items(): self.drawCellValue(cell, value)


    def drawCellValue(self, cell, value):
        xCoord, yCoord = cell
        font = pygame.font.SysFont(None, 32)
        text = font.render(str(value), True, WHITE_COLOR_RGB)
        # Weird text placement formatting. Theres probably a better way
        self.surface.blit(text,
            (xCoord * CELL_SIZE + 10, yCoord* CELL_SIZE + CELL_SIZE/2-10)
            )

    def colorCell(self, cell, color):
        xCoord, yCoord = cell
        pygame.draw.rect(
            self.surface,
            color,
            (xCoord*CELL_SIZE+1,yCoord*CELL_SIZE+1, CELL_SIZE-2, CELL_SIZE-2)
            )

    def getsurfaceWidth(self):
        return self.width_pxs

    def getsurface(self):
        return self.surface
