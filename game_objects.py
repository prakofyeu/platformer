import pygame

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.image = pygame.transform.scale(pygame.image.load("coin1.png"), (self.size, self.size))
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.image = pygame.transform.scale(pygame.image.load("food.png"), (self.size, self.size))
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)


class Portal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.image = pygame.transform.scale(pygame.image.load("portal.png"), (self.size, self.size))
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)


class Trap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.image = pygame.transform.scale(pygame.image.load("trap.png"), (self.size, self.size))
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)


class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load("platform.png"), (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)