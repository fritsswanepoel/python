import random
import pygame

import Settings

winds = {
    0: {
        'x':-1 * Settings.wind_width,
        'direction':1
        },
    1: {
        'x':Settings.screen_width,
        'direction':-1
       }
    }

class Wind(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(Settings.wind_image)
        self.sprite_height = Settings.wind_height
        self.sprite_width = Settings.wind_width
        self.frame = random.randint(0, 1)

        self.speed = Settings.wind_speed * winds[self.frame]['direction']
        self.x = winds[self.frame]['x']

        self.y = random.randint(Settings.wind_min_y, Settings.wind_max_y)
        self.delay = random.randint(Settings.wind_min_delay,Settings.wind_max_delay)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.delay <= 0:
            self.x += self.speed
            screen.blit(
                self.image,
                [
                    self.x,
                    self.y,
                    self.sprite_width,
                    self.sprite_height 
                ],
                (
                    0, 
                    self.sprite_height * self.frame,
                    self.sprite_width,
                    self.sprite_height
                )
            )
        else:
            self.delay -= 1