import pygame
from settings import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        # Screen's settings
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")

        # Data time
        self.clock = pygame.time.Clock()



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
        dt = self.clock.tick()

        self.screen.fill(SCREEN_COLOR)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
