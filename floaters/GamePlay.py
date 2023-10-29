import pygame
from Player import Player
from Wind import Wind
from Portal import Portal
import Settings

class GamePlay:
    def __init__(self, screen):
        self.font = pygame.font.Font(Settings.gameplay_font, Settings.gameplay_font_size)

        self.main_menu = None
        self.text_colour = (255, 255, 255)
        self.button_colour = (0, 0, 170)
        self.button_over_colour = (255, 50, 50)
        self.button_width = 50
        self.button_height = 20
        self.button_rect = [screen.get_width() - self.button_width,
                            0,
                            self.button_width,
                            self.button_height]
        
        self.button_font = pygame.font.Font(Settings.gameplay_font, Settings.button_font_size)
        self.button_text = self.button_font.render("Back", True, self.text_colour)
        self.mousex, self.mousey = (0, 0)
        self.player = Player()
        self.portal = Portal()

        self.winds = []
        for x in range(5):
            self.winds.append(Wind())

        self.screen = screen

    def update(self, events):
        self.player.update(self.winds)
        self.portal.update()
        
        return self
    
    def draw(self, screen):
        self.portal.draw(screen)
        self.player.draw(screen, self.portal.x, self.portal.width)

        deadwind = []

        for w in self.winds:
            w.draw(screen)
            if w.x >= screen.get_width() and w.frame == 0:
                deadwind.append(w)
            elif w.x <= -1 * w.image.get_width() and w.frame == 1:
                deadwind.append(w)

        for w in deadwind:
            self.winds.remove(w)
            self.winds.append(Wind())
    