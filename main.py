import pygame
import random
from field import Field
import time


# Creating colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REMOTE_COLOR = (0, 204, 205)


WIDTH = 400
HEIGHT = 600
FPS = 30

# Creating coordinates
x = 300
y = 300

x_change = 0
y_change = 0

# Creating a game and a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

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
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -10

    # Recording coordinate changes
    x += x_change
    y += y_change

    # Filling the screen with black
    screen.fill(BLACK)

    # Creating a snake head
    pygame.draw.rect(screen, RED, [x, y, 10, 10])

    pygame.display.update()

    # Keeping the cycle on the correct speed
    clock.tick(30)
    time.sleep(0.1)

# Exit
pygame.quit()
quit()