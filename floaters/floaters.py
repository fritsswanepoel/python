
import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((240,240))

pygame.display.set_caption("Floaters")

# functions
def set_wind_left(wind_left_rect):
        
    wind_left_rect[0] = 0 - (wind_left_rect.width + screen.get_width())
    wind_left_rect[1] = random.randint(portal_height,screen.get_height() - wind_left_rect.height - character_rect.height)
    wind_left_counter = random.randint(1,5)

    return (wind_left_rect, wind_left_counter)


def set_wind_right(wind_right_rect):
        
    wind_right_rect[0] = screen.get_width()
    wind_right_rect[1] = random.randint(portal_height,screen.get_height() - wind_right_rect.height - character_rect.height)
    wind_right_counter = random.randint(1,5)

    return (wind_right_rect, wind_right_counter)


# parameters
portal_shrink_rate = 0.3
wind_blow_rate = 10

# portal
portal_height = 5
portal_width = screen.get_width()
portal = pygame.image.load('./images/portal.png')
portal = portal.convert_alpha()
portal = pygame.transform.scale(portal, (portal_width, portal_height))
portal_rect = portal.get_rect()

portal_rect[0] = (screen.get_width() / 2) + (portal_rect.width / 2)

print(portal_rect)

# floater
floater = pygame.image.load('./images/floater.png')
floater = floater.convert_alpha()
floater_rect = floater.get_rect()
floater_speed = 1

# character
character = pygame.image.load('./images/character.png')
character = character.convert_alpha()
character_rect = character.get_rect()

character_rect[1] = screen.get_height() - character_rect.height

# wind_left
wind_left = pygame.image.load('./images/wind.png')
wind_left = wind_left.convert_alpha()
wind_left_rect = wind_left.get_rect()

wind_left_rect, wind_left_counter = set_wind_left(wind_left_rect)


# wind_right
wind_right = pygame.image.load('./images/wind.png')
wind_right = wind_right.convert_alpha()
wind_right_rect = wind_right.get_rect()

wind_right_rect, wind_right_counter = set_wind_left(wind_right_rect)


clock = pygame.time.Clock()
game_over = False
floater_released = False
wind_left_blowing = False
wind_right_blowing = False

x = 0
y = -10
while not game_over:
    dt = clock.tick(50)
    screen.fill((150,150,150))

    screen.blit(portal, portal_rect)
    screen.blit(character, character_rect)
    screen.blit(floater, floater_rect)
    screen.blit(wind_left, wind_left_rect)
    screen.blit(wind_right, wind_right_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Shrink portal
    portal_width -= portal_shrink_rate

    if portal_width <= 0:
        game_over = True
    else:
        portal = pygame.transform.scale(portal, (portal_width, portal_height))
        portal_rect = portal.get_rect()
        portal_rect[0] = (screen.get_width() / 2) - (portal_rect[2] / 2)

    # Move character
    pressed = pygame.key.get_pressed()
    if pressed[K_SPACE] \
        and floater_released == False:
        floater_released = True
    if pressed[K_LEFT]:
        x -= 0.1 * dt
    if pressed[K_RIGHT]:
        x += 0.1 * dt

    # Blow wind_left
    if wind_left_counter <= 0:
        if wind_left_blowing == False:
            wind_left_blowing = True
        if wind_left_blowing == True:
            wind_left_rect[0] += 5
    elif wind_left_counter > 0:
        wind_left_counter -= 1

    if wind_left_rect[0] >= screen.get_width():
        wind_left_blowing = False
        wind_left_rect, wind_left_counter = set_wind_left(wind_left_rect)

    # Blow wind_right
    if wind_right_counter <= 0:
        if wind_right_blowing == False:
            wind_right_blowing = True
        if wind_right_blowing == True:
            wind_right_rect[0] -= 5
    elif wind_right_counter > 0:
        wind_right_counter -= 1

    if wind_right_rect[0] + wind_right_rect.width <= 0:
        wind_right_blowing = False
        wind_right_rect, wind_right_counter = set_wind_right(wind_right_rect)


    # Blow floater left
    if floater_rect[0] >= wind_left_rect[0] \
        and floater_rect[0] + floater_rect.width <= wind_left_rect[0] + wind_left_rect.width \
        and floater_rect[1] >= wind_left_rect[1] \
        and floater_rect[1] + floater_rect.height <= wind_left_rect[1] + wind_left_rect.height:
        floater_rect[0] += wind_blow_rate


    # Blow floater right
    if floater_rect[0] >= wind_right_rect[0] \
        and floater_rect[0] + floater_rect.width <= wind_right_rect[0] + wind_right_rect.width \
        and floater_rect[1] >= wind_right_rect[1] \
        and floater_rect[1] + floater_rect.height <= wind_right_rect[1] + wind_right_rect.height:
        floater_rect[0] -= wind_blow_rate


    # Contain floater
    if floater_released:
        if y == -10:
            floater_rect[0] = character_rect[0] - floater_rect.height + character_rect.width / 2
            floater_rect[1] = character_rect[1] 
            y = floater_rect[1]
        elif y >= 0:
            y -= 3
        else:
            y = -10
            floater_released = False


    # Contain character
    if x <= 0:
        x = 0
    elif x >= screen.get_width() - character_rect[2]:
        x = screen.get_width() - character_rect[2]

    character_rect[0] = x
    floater_rect[1] = y

    pygame.display.update()

pygame.quit()
