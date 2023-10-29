import pygame
import Settings

class Floater:
    def __init__(self, x, y):
        self.image = pygame.image.load(Settings.floater_image)

        self.frame = 0
        self.x = x - self.image.get_width() // 2
        self.y = y
        self.dy = Settings.floater_yspeed 
        self.sprite_width = Settings.floater_sprite_width
        self.sprite_height = Settings.floater_sprite_height

    def update(self):
        self.y -=1
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

    def draw(self, screen):
        screen.blit(self.image, 
                    [
                        self.x, 
                        self.y, 
                        self.sprite_width, 
                        self.sprite_height],
                    (self.frame * self.sprite_width, 0, self.sprite_width, self.sprite_height)
                    )