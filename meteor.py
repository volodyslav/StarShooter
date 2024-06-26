import pygame
import random
from settings import *
from os.path import join


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "meteor.png")).convert_alpha()
        self.original = self.image
        self.rotation_speed = 40
        self.rect = self.image.get_frect(center=pos)
        self.meteor_speed = random.randint(200, 1000)
        self.meteor_direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.meteor_speed * dt * self.meteor_direction
        if self.rect.bottom > SCREEN_HEIGHT + 300:
            self.kill()
        # Rotate
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original, self.rotation, 1)
        self.rect = self.image.get_frect(center=self.rect.center)





