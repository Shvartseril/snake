import pygame

from snake import Direction, snake, second_snake


def handle_events():
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                snake.direction = Direction.RIGHT
            elif event.key == pygame.K_DOWN:
                snake.direction = Direction.DOWN
            elif event.key == pygame.K_UP:
                snake.direction = Direction.UP
            elif event.key == 97:
                second_snake.direction = Direction.LEFT
            elif event.key == 100:
                second_snake.direction = Direction.RIGHT
            elif event.key == 115:
                second_snake.direction = Direction.DOWN
            elif event.key == 119:
                second_snake.direction = Direction.UP
    return running
