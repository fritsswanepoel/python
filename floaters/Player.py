import pygame
from pygame.locals import *
import copy

import Settings

from Floater import Floater

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(Settings.player_image)
        self.sprite_width = 25
        self.sprite_height = 40
        self.frame = 1
        self.x = Settings.player_start_x
        self.y = Settings.screen_height - self.image.get_height() - Settings.player_start_y
        self.speed = Settings.player_speed
        self.floaters = []

        self.font = pygame.font.Font(Settings.player_font, Settings.player_font_size)
        self.points = 0
        self.cool_down = copy.deepcopy(Settings.player_cool_down)

    def update(self):
        keys = pygame.key.get_pressed()
        self.frame = 1
        if keys[K_LEFT]:
            self.x -= self.speed
            self.frame = 0
        if keys[K_RIGHT]:
            self.x += self.speed
            self.frame = 2

        if self.x < 0:
            self.x = 0
            self.frame = 1
        if self.x > Settings.screen_width - self.sprite_width:
            self.x = Settings.screen_width - self.sprite_width
            self.frame = 1

        if keys[K_SPACE] and self.cool_down <= 0:
            if self.frame == 2:
                floater_x = self.x + 5
            else:
                floater_x = self.x + self.sprite_width
            self.floaters.append(Floater(floater_x, self.y + (self.sprite_height // 3) * 2))
            self.cool_down = copy.deepcopy(Settings.player_cool_down)

        if self.cool_down > 0:
            self.cool_down -= 1

        for f in self.floaters:
            f.update()

    def draw(self, screen):
        screen.blit(self.image, 
                    [self.x, self.y, self.sprite_width, self.sprite_height],
                    (self.frame * self.sprite_width, 0, self.sprite_width, self.sprite_height)
                    )

        self.points_text = self.font.render('Points: ' + str(self.points), True, (255, 100, 100))
        screen.blit(self.points_text, (0,0))

        deadfloaters = []
        for f in self.floaters:
            if f.y < 0:
                deadfloaters.append(f)
            f.draw(screen)

        for f in deadfloaters:
            self.floaters.remove(f)




