import pygame

class Player(object):
    def __init__(self, pos=(0,0)):
        self.currPos = pos
        self.score = 0

    def move(self, action):
        oldX, oldY = self.currPos
        if action == 'left':
            self.currPos = (oldX - 1, oldY)
        elif action == 'right':
            self.currPos = (oldX + 1, oldY)
        elif action == 'up':
            self.currPos = (oldX, oldY + 1)
        elif action == 'down':
            self.currPos = (oldX, oldY - 1)



    def updateCurrPos(self, newCoords):
        self.currPos = newCoords
    def updateScore(self, newPoints):
        self.score += newpoints
    def getCurrCoords(self):
        return self.currPos
