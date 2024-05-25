import pygame
from os.path import join
from settings import *


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.image.load(join("images", "laser.png")).convert_alpha()
        self.rect = self.image.get_frect(midbottom=pos)
        self.speed_laser = 500


    def update(self, dt):
        self.rect.centery -= self.speed_laser * dt
        if self.rect.top < 200:
            self.kill()
