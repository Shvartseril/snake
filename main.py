import pygame
from snake import Snake, Direction
from random import *
import time


def records_record(score):
    with open('record.txt', 'r') as file:
        current_record = int(file.read())
    if current_record > score:
        return current_record
    with open('record.txt', 'w') as file:
        file.write(str(score))
    return score


# Function for creating a square
def draw_square(screen, position: tuple[int, int], color: tuple[int, int, int]):
    position = (position[0] * 10 + 200, position[1] * (-10) + 300)
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
ORANGE = (255, 120, 0)
REMOTE_COLOR = (0, 204, 205)

WIDTH = 400
HEIGHT = 600
FPS = 10
winner = ''

# Initializing objects
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Creating a snake
snake = Snake([(8, 0)])
second_snake = Snake([(-8, 0)])

# Creating food
snake_food = (randint(-19, 19), randint(-29, 29))

# creating directions
direction, direction_for_second_snake = False, False

# The game cycle
running = True
while running:

    # Entering a process (event)
    for event in pygame.event.get():

        # Creating movement for two snakes
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                direction = Direction.RIGHT
            elif event.key == pygame.K_DOWN:
                direction = Direction.DOWN
            elif event.key == pygame.K_UP:
                direction = Direction.UP
            elif event.key == 97:
                direction_for_second_snake = Direction.LEFT
            elif event.key == 100:
                direction_for_second_snake = Direction.RIGHT
            elif event.key == 115:
                direction_for_second_snake = Direction.DOWN
            elif event.key == 119:
                direction_for_second_snake = Direction.UP

    if direction:
        snake.move(direction)

    if direction_for_second_snake:
        second_snake.move(direction_for_second_snake)

    # creating a border
    snake.going_abroad()
    second_snake.going_abroad()

    # Filling the screen with black
    screen.fill(BLACK)

    # Creating snakes
    for i in snake.position:
        draw_square(screen, i, RED)

    for i in second_snake.position:
        draw_square(screen, i, BLUE)

    if snake.position[0] == snake_food:
        snake_food = (randint(-19, 19), randint(-29, 29))
        FPS += 0.3
        snake.eating()

    if second_snake.position[0] == snake_food:
        snake_food = (randint(-19, 19), randint(-29, 29))
        FPS += 0.3
        second_snake.eating()

    # Achieving 20 points to win
    if snake.score == 20:
        winner = 'snake1 won!'
        running = False
    if second_snake.score == 20:
        winner = 'snake2 won!'
        running = False

    draw_square(screen, snake_food, GREEN)

    # displaying the score on the screen
    message(screen, f'Score1: {snake.score}', (0, 0), ORANGE, 'Arial', 24, True)

    message(screen, f'Score2: {second_snake.score}', (0, 25), ORANGE, 'Arial', 24, True)

    # Update of screen
    pygame.display.update()

    # Keeping the cycle on the correct speed
    clock.tick(FPS)

# Creating a message, who won
message(screen, winner, (20, 160), WHITE, 'Arial', 80)
time.sleep(3)

# Exit
pygame.quit()
quit()
