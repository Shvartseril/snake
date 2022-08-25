import pygame
import time
from snake import Snake, Direction


def draw_square(screen, position: tuple[int, int]):
    position = (position[0] * 10 + 195, position[1] * (-10) + 295)
    pygame.draw.rect(screen, RED, [*position, 10, 10])


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
direction = Direction.UP


# Creating a game and a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

snake = Snake([(0, 0), (-1, 0), (-2, 0)])

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
    snake.move(direction)

    # Filling the screen with black
    screen.fill(BLACK)

    # Creating a snake head
    for i in snake.position:
        draw_square(screen, i)

    pygame.display.update()

    # Keeping the cycle on the correct speed
    clock.tick(FPS)

# Exit
pygame.quit()
quit()
