import pygame

import Settings

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

        pygame.display.set_caption(Settings.screen_caption)

        self.current_state = None

    def run(self, state):
        game_over = False
        self.current_state = state
        clock = pygame.time.Clock()

        while not game_over:
            clock.tick(Settings.game_tick)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
            self.screen.fill(Settings.screen_colour)
            self.current_state = self.current_state.update(events)
            self.current_state.draw(self.screen)
            pygame.display.update()

        pygame.quit()

