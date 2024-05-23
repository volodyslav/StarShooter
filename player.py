import pygame
from os.path import join
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.player_speed = 300
        self.direction = pygame.Vector2()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.player_speed * dt
        print(self.rect.center)