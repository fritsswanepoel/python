import pygame
from pygame.locals import *
import copy

import Settings

from Floater import Floater

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(Settings.player_image)
        self.sprite_width = Settings.player_width
        self.sprite_height = Settings.player_height
        self.frame = 1
        self.x = Settings.player_start_x
        self.y = Settings.screen_height - self.sprite_height - Settings.player_start_y
        self.speed = Settings.player_speed
        self.floaters = []

        self.font = pygame.font.Font(Settings.player_font, Settings.player_font_size)
        self.points = 0
        self.cool_down = copy.deepcopy(Settings.player_cool_down)
        self.fainted = 0

    def update(self, winds):
        if self.fainted <= 0:
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
        
        else:
            self.fainted -= 1
    
        if self.cool_down > 0:
            self.cool_down -= 1

        for f in self.floaters:
            f.update(winds)

            if  f.x <= self.x + (self.sprite_width // 2) <= f.x + f.sprite_width \
                and f.y + f.sprite_height >= self.y:
                self.frame = 3
                self.fainted = 10      

    def draw(self, screen, portal_x, portal_width):
        screen.blit(self.image, 
                    [self.x, self.y, self.sprite_width, self.sprite_height],
                    (self.frame * self.sprite_width, 0, self.sprite_width, self.sprite_height)
                    )

        deadfloaters = []
        for f in self.floaters:
            if f.y <= 15:
                if f.x >= portal_x and f.x <= portal_x + portal_width - f.sprite_width:
                    self.points += 1
                    deadfloaters.append(f)
            elif f.y < -1 * Settings.floater_height:
                deadfloaters.append(f)
            f.draw(screen)
            

        for f in deadfloaters:
            self.floaters.remove(f)

        self.points_text = self.font.render(Settings.points_text + str(self.points), True, Settings.points_colour)
        screen.blit(self.points_text, Settings.points_position)

