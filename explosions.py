import pygame
import random
from settings import *
from os.path import join


class Explosions(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.images = []
        self.frame = 0

        for index in range(21):
            self.images.append(pygame.image.load(join("images", "explosion", f"{index}.png")).convert_alpha())

        self.image = self.images[self.frame]
        self.rect = self.image.get_frect(center=pos)


    def update(self, dt):
        self.frame += 20 * dt
        if self.frame < len(self.images):
            self.image = self.images[int(self.frame)]
        else:
            self.kill()

