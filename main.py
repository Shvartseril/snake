import pygame
from snake import Snake, Direction
from random import *


# Function for creating a square
def draw_square(screen, position: tuple[int, int], color: tuple[int, int, int]):
    position = (position[0] * 10 + 195, position[1] * (-10) + 295)
    pygame.draw.rect(screen, color, [*position, 10, 10])


# Function for creating messages
def message(screen, msg: str, coordinates: tuple[int, int], color: tuple[int, int, int], font_name: str, font_size: int, bold: bool = False,
            italic: bool = False):
    font = pygame.font.SysFont(font_name, font_size, bold, italic)
    msg_screen = font.render(msg, False, color)
    screen.blit(msg_screen, coordinates)
    pygame.display.update()


# Creating colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REMOTE_COLOR = (0, 204, 205)

WIDTH = 400
HEIGHT = 600
FPS = 10

# Initializing objects
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Creating a snake
snake = Snake([(0, 0)])

# Creating food
snake_food = (randint(-19, 19), randint(-29, 29))

direction = False

# The game cycle
running = True
while running:

    # Entering a process (event)
    for event in pygame.event.get():

        # Move the snake's head on the keys: up, down, right, left
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                direction = Direction.RIGHT
            elif event.key == pygame.K_DOWN:
                direction = Direction.DOWN
            elif event.key == pygame.K_UP:
                direction = Direction.UP

    if direction:
        snake.move(direction)

        # creating a border
        snake.going_abroad()

    # Filling the screen with black
    screen.fill(BLACK)

    # Creating a snake
    for i in snake.position:
        draw_square(screen, i, RED)

    if snake.position[0] == snake_food:
        snake_food = (randint(-19, 19), randint(-29, 29))
        FPS += 0.3
        snake.eating()

    draw_square(screen, snake_food, GREEN)

    # Update of screen
    pygame.display.update()

    # Keeping the cycle on the correct speed
    clock.tick(FPS)

# Exit
pygame.quit()
quit()
