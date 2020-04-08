import pygame

class Player(object):
    def __init__(self, pos=(0,0)):
        self.currPos = pos
        self.score = 0

    def updateCurrPos(self, newCoords):
        self.currPos = newCoords
    def updateScore(self, newPoints):
        self.score += newpoints
    def getCurrCoords(self):
        return self.currPos
