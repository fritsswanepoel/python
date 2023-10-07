
import pygame
from pygame.locals import *
import math

pygame.init()

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption("Breakin' bricks")

#bat
bat = pygame.image.load('./images/bat.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

bat_rect[1] = screen.get_height() - bat_rect[3] - 10

#brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()

bricks = []
brick_gap = 1
brick_rows = 3

brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) //2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

#ball
ball = pygame.image.load('./images/ball.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (screen.get_width() // 3, brickY + brick_rect[3] + brick_gap + ball_rect.height)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_velocity = math.sqrt(sx**2 + sy**2)
ball_rect.topleft = ball_start
ball_prev = ball_rect[:2]

clock = pygame.time.Clock()

game_over = False
x = 0
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_SPACE]:
        ball_served = True
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    
    # Contain bat
    if x <= 0:
        x = 0
    elif x >= screen.get_width() - bat_rect[2]:
        x = screen.get_width() - bat_rect[2]

    bat_rect[0] = x

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
    
    # Bat ball
    if bat_rect[0] <= ball_rect[0] <= bat_rect[0] + bat_rect.width \
        and bat_rect[1] <= ball_rect[1] + ball_rect.height \
        and bat_rect[1] + bat_rect.height >= ball_rect[1] + ball_rect.height \
        and sy > 0:
        sy *= -1

        # Speed up ball
        # sx *= 1.01
        # sy *= 1.01

        ball_velocity = ball_velocity * 1.02 

        # Position on bat
        bat_pos = (ball_rect[0] - (bat_rect.width / 2) - bat_rect[0]) / bat_rect.width
        print(bat_pos)
        if sx < 0:
            bat_pos *= -1

        if bat_pos < 0:
            angle = 45
        elif bat_pos < 0.1:
            angle = 40
        elif bat_pos < 0.2:
            angle = 35
        elif bat_pos < 0.3:
            angle = 30
        elif bat_pos < 0.4:
            angle = 25
        elif bat_pos <= 0.5:
            angle = 20
        
        x_velocity = ball_velocity * math.cos(math.radians(angle))
        if sx < 0:
            x_velocity *= -1
        y_velocity = ball_velocity * math.sin(math.radians(angle)) * -1

        sx = x_velocity
        sy = y_velocity

        print(x_velocity)
        print(y_velocity)
        print(ball_velocity)
        print(x_velocity ** 2 +  y_velocity ** 2)
        print(ball_velocity ** 2)

    # Hit bricks
    delete_brick = None
    for b in bricks:
        bx, by = b
        if ball_rect[0] + ball_rect.width >= bx \
            and ball_rect[0] <= bx + brick_rect.width \
            and ball_rect[1] + ball_rect.height >= by \
            and ball_rect[1] <= by + brick_rect.height \
            and delete_brick == None:
            
            delete_brick = b

            #Left of brick
            if ball_rect[0] + ball_rect.width >= bx \
                and ball_prev[0] + ball_rect.width < bx:
                sx *= -1
            #Right of brick
            elif ball_rect[0] <= bx + brick_rect.width \
                and ball_prev[0] > bx + brick_rect.width:
                sx *= -1
                
            #Top of brick
            if ball_rect[1] + ball_rect.height >= by \
                and ball_prev[1] + ball_rect.height < by:
                sy *= -1
            #Bottom of brick
            elif ball_rect[1] <= by + brick_rect.height \
                and ball_prev[1] > by + brick_rect.height:
                sy *= -1
                
            break

    if delete_brick is not None:
        bricks.remove(delete_brick)

    # Contain ball in screen
    # Top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    
    # Bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = ball_start
    
    # Left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1

    # Right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    ball_prev = ball_rect[:2]

    pygame.display.update()

pygame.quit()