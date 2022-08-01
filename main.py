import pygame
import random

from field import Field

WIDTH = 360
HEIGHT = 480
FPS = 3
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
    clock.tick(FPS)
    field.draw_field()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
