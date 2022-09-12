import time

import pygame

from snake import snake, second_snake
from utils.colors import GREEN, RED, BLUE, ORANGE, WHITE
from snake import food
from utils.functions import message


def draw_square(screen, position: tuple[int, int], color: tuple[int, int, int], size: int):
    position = (position[0] * 10 + 200, position[1] * (-10) + 300)
    pygame.draw.rect(screen, color, [*position, size, size])


def drawing_food_and_snake(screen):
    for i in food.snake_food_coordinates:
        draw_square(screen, i, GREEN, 9)

    draw_square(screen, food.snake_food, GREEN, 9)

    # Creating snakes
    for i in snake.position:
        draw_square(screen, i, RED, 10)

    for i in second_snake.position:
        draw_square(screen, i, BLUE, 10)


def draw_messages(screen):
    message(screen, f'Score1: {snake.score}', (0, 0), ORANGE, 'Arial', 24, True)
    message(screen, f'Score2: {second_snake.score}', (0, 25), ORANGE, 'Arial', 24, True)


def draw_message_who_won(screen):
    if snake.winner:
        message(screen, f'{snake.winner} win!', (20, 160), WHITE, 'Arial', 80)
        time.sleep(3)
    if second_snake.winner:
        message(screen, f'{second_snake.winner} win!', (0, 160), WHITE, 'Arial', 57)
        time.sleep(3)
