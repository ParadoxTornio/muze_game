import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.rect.x += width // 2

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.left = WIDTH - self.width
        if self.rect.top > HEIGHT:
            self.rect.top = 0
        if self.rect.right < 0:
            self.rect.right = self.width
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

    def reset_position(self):
        self.rect.center = self.position
        self.rect.x += self.width // 2


class MuzeCell(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((20, 20))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class EndGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 128, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 400
