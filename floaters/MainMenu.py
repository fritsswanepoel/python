import pygame

import Settings

class MainMenu:
    def __init__(self, screen):
        self.font = pygame.font.Font(Settings.mainmenu_font, Settings.mainmenu_font_size)
        self.title = self.font.render(Settings.mainmenu_font_text, True, Settings.game_font_colour)
        self.title_position = ((Settings.screen_width / 2) - (self.title.get_width() / 2), Settings.mainmenu_font_down)
        self.game_play = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.game_play

        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)