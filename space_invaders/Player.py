
import pygame
import Settings

from pygame.locals import *
from Bullet import Bullet

# https://www.clipartmax.com/download/m2H7i8i8b1b1K9H7_spaceship-pixel-art-space-ship/

class Player(pygame.sprite.Sprite):
    def __init__(self, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ship.png")
        self.x = 10
        self.y = ypos
        self.speed = 3
        self.bullets = []
        self.font = pygame.font.SysFont('Arial', 25)
        self.lives = 3

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.x -= self.speed
        if keys[K_RIGHT]:
            self.x += self.speed

        self.rect.topleft = (self.x, self.y)

        if keys[K_SPACE]:
            self.bullets.append(Bullet(self.x + (self.image.get_width() // 2), self.y, 20))

        for l in pygame.sprite.spritecollide(self, Settings.abullets, 0):
            Settings.abullets.remove(l)
            l.kill()
            self.lives -= 1

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])
        self.lives_text = self.font.render('Lives: ' + str(self.lives), True, (255, 100, 100))
        screen.blit(self.lives_text, (0, 0))

        deadbullets = []
        for b in self.bullets:
            if b.y < 0:
                deadbullets.append(b)
            b.draw(screen)

        for b in deadbullets:
            self.bullets.remove(b)