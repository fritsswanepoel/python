import pygame
import copy
import Settings

class Floater:
    def __init__(self, x, y):
        self.image = pygame.image.load(Settings.floater_image)
        
        self.sprite_width = Settings.floater_width
        self.sprite_height = Settings.floater_height

        self.frame = 0
        self.x = x - self.sprite_width // 2
        self.y = y
        self.dy = Settings.floater_yspeed 

    def update(self, winds):
        dx = 0
        in_wind = False

        for w in winds:
            if self.x >= w.x \
                and self.x <= w.x + w.sprite_width \
                and self.y >= w.y \
                and self.y <= w.y + w.sprite_height:
                    dx += w.speed // 2
                    in_wind = True

        self.x += dx

        if in_wind:
            self.y -= self.dy // 2 
        else:
            self.y -= self.dy
        
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

    def draw(self, screen):
        screen.blit(
            self.image, 
            [
                self.x, 
                self.y, 
                self.sprite_width, 
                self.sprite_height
            ],
            (
                self.frame * self.sprite_width, 
                0, 
                self.sprite_width, 
                self.sprite_height
            )
        )
        
