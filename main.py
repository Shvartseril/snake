import pygame
import random
from field import Field
import time


# Создаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REMOTE_COLOR = (0, 204, 205)


WIDTH = 400
HEIGHT = 600
FPS = 30

x = 300
y = 300

x_change = 0
y_change = 0

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
field = Field(screen)
running = True
while running:
    # Держим цикл на правильной скорости
    # Ввод процесса (события)
    for event in pygame.event.get():

        # Перемещаем голову змейки по клавишам: вверх, вниз, направо, налево
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

    x += x_change
    y += y_change
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [x, y, 10, 10])

    pygame.display.update()

    clock.tick(30)
    time.sleep(0.1)

pygame.quit()
quit()