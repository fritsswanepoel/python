import pygame

class MainMenu:
    def __init__(self, screen):
        self.font = pygame.font.Font('fonts/aAbsoluteEmpire.ttf', 80)
        self.title = self.font.render('Alien Invasion', True, (255, 255, 255))
        self.title_position = (10, 10)
        self.game_play = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.game_play

        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)