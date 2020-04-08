from Window import Window
from Board import Board
from Player import Player
import pygame

pygame.init()
w = Window()
p = Player()
b = Board()
b.createPenaltyCells()
w.drawSurface(b, p)

while True:
    for e in pygame.event.get(): None
