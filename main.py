import pygame
from settings import *
import sys
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        # Screen's settings
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")

        # Data time
        self.clock = pygame.time.Clock()

        # All groups
        self.group_sprites = pygame.sprite.Group()

        # Init Player
        self.player = Player(self.group_sprites)


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.show_screen()


    def show_screen(self):
        """Represent all sprites on the screen"""
        dt = self.clock.tick(60) / 1000

        self.group_sprites.update(dt)
        self.screen.fill(SCREEN_COLOR)
        # Draw a player
        self.group_sprites.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run_game()
