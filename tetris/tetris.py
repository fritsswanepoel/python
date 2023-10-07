
import pygame
import random

pygame.init()

#Variables
display_size = (500, 600)
display_fill = (0, 0, 0)
grid_size = 30
block_grid_size = 4
fps = 3

game_board = []

game_over = False

#Setup
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Tetris")

rows = screen.get_height() // grid_size
cols = screen.get_width() // grid_size
pad_rows = (screen.get_height() - (rows * grid_size)) // 2
pad_cols = (screen.get_width() - (cols * grid_size)) // 2
    
blocks = [
    [ # Straight 
        [1,5,9,13], # Vertical 
        [4,5,6,7], # Horizontal
        [2,6,10,14],
        [8,9,10,11]
    ],
    [ # Cross
        [2,5,6,7,10]
    ],
    [ # Z
        [5,6,10,11],
        [6,9,10,13],
    ],
    [ # Square
        [1,2,5,6]
    ],
    [ # L
        [2,3,6,10],
        [5,6,7,11],
        [2,6,9,10],
        [1,5,6,7]
    ],
    [ # L2
        [1,2,6,10],
        [3,5,6,7],
        [2,6,10,11],
        [5,6,7,9]
    ],
    [ # T
        [1,2,3,6],
        [3,6,7,11],
        [6,9,10,11],
        [1,5,6,9]
    ],
    [ # U
        [5,7,9,10,11],
        [6,7,10,14,15],
        [5,6,7,9,11],
        [6,7,11,14,15]
    ]
]

#Initialize game board
for i in range(cols):
    new_col = []
    for j in range(rows):
        new_col.append((0,0,0))
    game_board.append(new_col)


#Classes
class Block:
    def __init__(self):
        self.x = random.randint(block_grid_size // 2 - 1, cols - block_grid_size - block_grid_size // 2)
        self.y = 0
        self.type = random.randint(0, len(blocks)-1)
        self.rotation = 0

    def shape(self):
        return blocks[self.type][self.rotation]

#Functions
def draw_grid():
    for y in range(rows): # rows
        for x in range(cols): # columns
            pygame.draw.rect(screen, (100, 100, 100), [(x * grid_size) + pad_cols, (y * grid_size) + pad_rows, grid_size, grid_size], 1)
            if game_board[x][y] != (0, 0, 0):
                pygame.draw.rect(screen, game_board[x][y], [(x * grid_size) + pad_cols + 1, (y * grid_size) + pad_rows + 1, grid_size - 1, grid_size-1])


def draw_block():
    for y in range(block_grid_size): # rows
        for x in range(block_grid_size): # cols
            if y * block_grid_size + x in block.shape():
                pygame.draw.rect(screen, 
                    (255, 255, 255), 
                    [
                        ((x + block.x) * grid_size) + pad_cols + 1,
                        ((y + block.y) * grid_size) + pad_rows + 1,
                        grid_size - 2,
                        grid_size - 2
                    ]
                    )

def drop_block():
    can_drop = True
    for y in range(block_grid_size):
        for x in range(block_grid_size):
            if y * block_grid_size + x in block.shape():
                if block.y + y >= rows - 1:
                    can_drop = False 
    
    if can_drop:
        block.y += 1
    else:
        for y in range(block_grid_size):
            for x in range(block_grid_size):
                if y * block_grid_size + x in block.shape():
                    game_board[x + block.x][y + block.y] = (0, 255, 0)
    
    return can_drop


def side_move(dx):
    can_move = True
    for y in range(block_grid_size):
        for x in range(block_grid_size):
            if y * block_grid_size  + x in block.shape():
                if dx < 0:
                    if x + block.x < 1:
                        can_move = False
                elif dx > 0:
                    if x + block.x >= cols - 1:
                        can_move = False
    
    if can_move:
        block.x += dx
    else:
        drop_block()


def rotate():
    last_rotation = block.rotation
    block.rotation = (block.rotation + 1) % len(blocks[block.type])
    can_rotate = True
    for y in range(block_grid_size):
        for x in range(block_grid_size):
            if y * block_grid_size + x in block.shape():
                if block.x + x < 0 \
                        or block.x + x > cols - 1 \
                        or block.y + y > rows - 1 \
                        or block.y + y < 0:
                    can_rotate = False
                

    if not can_rotate:
        block.rotation = last_rotation 


#
block = Block()

clock = pygame.time.Clock()

while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rotate()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)

    screen.fill(display_fill)

    draw_grid()
    if block is not None:
        draw_block()
        if event.type != pygame.KEYDOWN:
            if not drop_block():
                block = Block()

    pygame.display.update()

pygame.quit()


