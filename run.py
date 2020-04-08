from Window import Window
from Board import Board
from Player import Player
from QLearner import QLearner
import pygame

pygame.init()
w = Window()
p = Player()
b = Board()
b.createPenaltyCells()
w.drawSurface(b, p)

q = QLearner(b)
q.learn()



while True:
    for e in pygame.event.get(): None
