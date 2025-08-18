import pygame
from settings import *
from player import Player
from game_objects import Portal, Trap, Coin, Food, Platform


platforms = []
platforms.append(Platform(0, 100, 100, 50))
platforms.append(Platform(150, 100, 100, 50))
