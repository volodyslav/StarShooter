import pygame
from os.path import join
from settings import *
import random


class Star(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "star.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(random.randint(10, SCREEN_WIDTH - 10),
                                                 random.randint(10, SCREEN_HEIGHT - 10)))



