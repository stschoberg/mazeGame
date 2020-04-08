import pygame

class Player(object):
    def __init__(self, pos=(0,0)):
        self.currPos = pos
        self.score = 0

    def moveDown(self):
        oldX, oldY = self.currPos
        self.currPos = (oldX, oldY - 1)
    def moveUp(self):
        oldX, oldY = self.currPos
        self.currPos = (oldX, oldY + 1)
    def moveRight(self):
        oldX, oldY = self.currPos
        self.currPos = (oldX + 1, oldY)
    def moveLeft(self):
        oldX, oldY = self.currPos
        self.currPos = (oldX - 1, oldY)

    def updateCurrPos(self, newCoords):
        self.currPos = newCoords
    def updateScore(self, newPoints):
        self.score += newpoints
    def getCurrCoords(self):
        return self.currPos
