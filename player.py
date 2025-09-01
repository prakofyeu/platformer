import pygame
from settings import WIDTH, HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.image = pygame.transform.scale(pygame.image.load("player.png"), (self.size, self.size))
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)
        self.speed = [10, 0]
        self.jump_power = 5
        self.standing = False
        self.gravity = 0.1

    def fall(self):
        if not self.standing:
            self.speed[1] += self.gravity
            self.y += self.speed[1]
            self.update_hitbox()

    def platform_collision(self, platform):
        if self.hitbox.colliderect(platform.hitbox):
            if self.speed[1] > 0 and self.hitbox.bottom <= platform.hitbox.top + 10:
                self.y = platform.y - self.size
                self.speed[1] = 0
                self.update_hitbox()
                self.standing = True
                return True
        else:
            self.standing = False
            return False

    def vertical_motion(self):
        if not self.standing:
            self.fall()

    def jump(self):
        if self.standing:
            self.speed[1] = -self.jump_power
            self.standing = False




    def move_right(self):
        if self.x < WIDTH - self.size:
            self.x += self.speed[0]

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed[0]

    def update_hitbox(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y