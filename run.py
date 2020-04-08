from Window import Window
from Board import Board
import pygame

w = Window()

b = Board()
w.drawSurface(b)

while True:
    for e in pygame.event.get(): None
