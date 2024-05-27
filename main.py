import random
import pygame
from settings import *
import sys
from player import Player
from star import Star
from meteor import Meteor
from laser import Laser
from explosions import Explosions
from os.path import join


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

        # Init Star class and draw stars
        for i in range(NUMBER_STARS):
            Star(self.group_sprites)

        self.meteor_event = pygame.event.custom_type()
        pygame.time.set_timer(self.meteor_event, 100)

        self.meteor_group = pygame.sprite.Group()

        # For getting laser amount
        self.laser_group = pygame.sprite.Group()

        # Init Player
        self.player = Player(self.group_sprites)

        # Musics
        self.music_laser = pygame.mixer.Sound(join("audio", "laser.wav"))
        self.music_laser.set_volume(0.4)

        self.music_game = pygame.mixer.Sound(join("audio", "game_music.wav"))
        self.music_game.set_volume(0.1)
        self.music_game.play()

        self.music_explosion = pygame.mixer.Sound(join("audio", "explosion.wav"))
        self.music_explosion.set_volume(0.5)

        self.music_player_damage = pygame.mixer.Sound(join("audio", "damage.ogg"))
        self.music_player_damage.set_volume(0.7)

        # Text
        self.font = pygame.font.Font(join("images", "Oxanium-Bold.ttf"))
        self.font_large = pygame.font.Font(join("images", "Oxanium-Bold.ttf"), 50)

        # Lives
        self.life = 6
        self.image_ship = pygame.image.load(join("images", "player.png")).convert_alpha()

        # Start the game
        self.game_start = False
        self.start_button_rect = pygame.Rect(SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT//2 - 25, 150, 50)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.life == 0:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_start = False
                    elif event.key == pygame.K_SPACE and len(self.laser_group) < 2 and self.game_start:
                        self.music_laser.play()
                        laser = Laser((self.group_sprites, self.laser_group), self.player.rect.midtop)
                        self.laser_group.add(laser)
                elif event.type == self.meteor_event and self.game_start:
                    x, y = random.randint(0, SCREEN_WIDTH), random.randint(-300, -100)
                    Meteor((self.group_sprites, self.meteor_group), (x, y))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.start_button_rect.collidepoint(mouse_x, mouse_y):
                        self.game_start = True

            # Check game and menu
            if self.game_start:
                self.show_screen()
                self.collide_player_meteors()
                self.collide_laser_meteor()
            else:
                self.draw_menu()

    def draw_menu(self):
        """Before playing the game show the menu"""
        self.screen.fill("gray")
        # Draw a title
        text_title = self.font_large.render("Star Shooter", True, "blue")
        title_rect = text_title.get_frect(center=(SCREEN_WIDTH // 2, 100))
        # Draw a button to start
        pygame.draw.rect(self.screen, "black", self.start_button_rect, border_radius=10)
        # Draw start on the button
        text = self.font.render("Start", True, "white")
        text_rect = text.get_frect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 5))
        self.screen.blit(text_title, title_rect)
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def collide_player_meteors(self):
        if pygame.sprite.spritecollide(self.player, self.meteor_group, True,
                                              pygame.sprite.collide_mask):
            self.music_player_damage.play()
            self.life -= 1


    def collide_laser_meteor(self):
        for laser in self.laser_group:
            if pygame.sprite.spritecollide(laser, self.meteor_group, True):
                Explosions(self.group_sprites, laser.rect.midtop)
                self.music_explosion.play()
                laser.kill()


    def display_score(self):
        time = pygame.time.get_ticks() // 1000
        text = self.font.render(str(f"Score: {time}"), True, "white")
        text_rect = text.get_frect(center=(SCREEN_WIDTH / 2, 20))
        self.screen.blit(text, text_rect)

    def draw_lives(self):
        for i in range(1, self.life+1):
            ship_rect = self.image_ship.get_frect(center=(SCREEN_WIDTH - i * 40, 50))
            self.screen.blit(self.image_ship, ship_rect)

    def show_screen(self):
        """Represent all sprites on the screen"""
        dt = self.clock.tick(60) / 1000

        self.group_sprites.update(dt)

        self.screen.fill(SCREEN_COLOR)

        # draw score
        self.display_score()

        # Draw player's lives
        self.draw_lives()

        # Draw a player
        self.group_sprites.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run_game()
