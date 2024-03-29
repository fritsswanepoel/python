import pygame
import copy

import Settings

class Portal:
    def __init__(self):
        self.colour = Settings.portal_colour
        self.x = 0
        self.y = -1 * (Settings.portal_height // 2)
        self.width = Settings.screen_width
        self.height = Settings.portal_height
        self.cooldown = copy.deepcopy(Settings.portal_speed)
        self.speed = 1

    def update(self):
        if self.cooldown <= 0:
            self.width -= 2
            self.x += 1
            self.cooldown = copy.deepcopy(Settings.portal_speed)
        
        if self.width < 0:
            self.width = 0
            self.x = 0
        else:
            self.cooldown -= 1

        if self.x <= 0 or self.x + self.width >= Settings.screen_width:
            self.speed *= -1
        self.x += self.speed   


    def draw(self, screen):
        surface = pygame.Surface((screen.get_width(), Settings.portal_height // 2))
        
        pygame.draw.ellipse(
            surface, 
            self.colour, 
            (self.x, self.y, self.width, self.height)
            )
        screen.blit(surface,
                    Settings.portal_position)