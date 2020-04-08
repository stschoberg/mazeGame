from Window import Window
from Board import Board
from Player import Player
import pygame

w = Window()
p = Player()
b = Board()
w.drawSurface(b, p)

while True:
    for e in pygame.event.get(): None
