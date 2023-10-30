import pygame
from Player import Player
from Wind import Wind
from Portal import Portal
import Settings

class GamePlay:
    def __init__(self, screen):
        self.font = pygame.font.Font(Settings.gameplay_font, Settings.gameplay_font_size)

        self.main_menu = None
        self.text_colour = Settings.mainmenu_text_colour
        self.button_colour = Settings.mainmenu_button_colour
        self.button_over_colour = Settings.mainmenu_button_over_colour
        self.button_width = Settings.mainmenu_button_width
        self.button_height = Settings.mainmenu_button_height

        self.button_rect = [Settings.screen_width - self.button_width,
                            0,
                            self.button_width,
                            self.button_height]
        
        self.button_font = pygame.font.Font(Settings.gameplay_font, Settings.button_font_size)

        self.mousex, self.mousey = (0, 0)

        self.screen = screen

        self.reset()

    def reset(self):
        self.player = Player()
        self.portal = Portal()

        self.winds = []
        for _ in range(Settings.wind_count):
            self.winds.append(Wind())

    def update(self, events):
        if self.portal.width <= 0:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                        return self.main_menu
                
        self.player.update(self.winds)
        self.portal.update()
        
        return self
    
    def draw(self, screen):

        if self.portal.width <= 0:
            title = self.button_font.render("Score: " + str(self.player.points), True, self.text_colour)
            screen.blit(
                title, 
                (
                    (Settings.screen_width - self.button_width) //2,
                    (Settings.screen_height - self.button_height) //2,
                )
            )
            return self
        
        self.portal.draw(screen)
        self.player.draw(screen, self.portal.x, self.portal.width)

        deadwind = []

        for w in self.winds:
            w.draw(screen)
            if w.x >= Settings.screen_width and w.frame == 0:
                deadwind.append(w)
            elif w.x <= -1 * Settings.wind_width and w.frame == 1:
                deadwind.append(w)

        for w in deadwind:
            self.winds.remove(w)
            self.winds.append(Wind())

        
    