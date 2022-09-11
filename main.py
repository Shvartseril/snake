import pygame
from settings import HEIGHT, WIDTH, FPS
from snake import Snake, Direction
from random import *
import time
from utils.colors import BLACK, GREEN, RED, BLUE, WHITE, ORANGE
from utils.functions import draw_square, message


def main():
    winner = ''

    # Initializing objects
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    # Creating a snake
    snake = Snake([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    second_snake = Snake([(-8, 0), (-8, -1), (-8, -2), (-8, -3)])

    # Creating food
    snake_food = (randint(-19, 19), randint(-29, 29))
    snake_food_coordinates = []

    # creating directions
    direction, direction_for_second_snake = False, False

    # The game cycle
    running = True
    while running:

        # Entering a process (event)
        for event in pygame.event.get():

            # Creating movement for two snakes
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
                elif event.key == 97:
                    direction_for_second_snake = Direction.LEFT
                elif event.key == 100:
                    direction_for_second_snake = Direction.RIGHT
                elif event.key == 115:
                    direction_for_second_snake = Direction.DOWN
                elif event.key == 119:
                    direction_for_second_snake = Direction.UP

        snake.find_next_head(direction)
        second_snake.find_next_head(direction_for_second_snake)

        if snake.next_head in second_snake.position and snake.next_head != second_snake.position[0]:
            snake_food_coordinates += snake.position
            snake.position = [(0, 0)]
        if second_snake.next_head in snake.position and second_snake.next_head != snake.position[0]:
            snake_food_coordinates += second_snake.position
            second_snake.position = [(0, 0)]

        if direction:
            snake.move(direction)

        if direction_for_second_snake:
            second_snake.move(direction_for_second_snake)

    # snake_food_coordinates += snake.position[snake.position.index(second_snake.position[0]):]
    # snake.position = snake.position[:snake.position.index(second_snake.position[0])]
    # snake_food_coordinates += snake.position[snake.position.index(second_snake.position[0]):]
    # snake.position = snake.position[:snake.position.index(second_snake.position[0])]

        # creating a border
        snake.going_abroad()
        second_snake.going_abroad()

        # Filling the screen with black
        screen.fill(BLACK)

        for i in snake_food_coordinates:
            draw_square(screen, i, GREEN, 9)

        draw_square(screen, snake_food, GREEN, 9)

        # Creating snakes
        for i in snake.position:
            draw_square(screen, i, RED, 10)

        for i in second_snake.position:
            draw_square(screen, i, BLUE, 10)

        if snake_food in snake.position:
            snake_food = (randint(-19, 19), randint(-29, 29))
            FPS += 0.3
            snake.eating()

        if snake_food in second_snake.position:
            snake_food = (randint(-19, 19), randint(-29, 29))
            FPS += 0.3
            second_snake.eating()

        if snake.position[0] in snake_food_coordinates:
            snake.eating()
            snake_food_coordinates.remove(snake.position[0])
        if second_snake.position[0] in snake_food_coordinates:
            second_snake.eating()
            snake_food_coordinates.remove(second_snake.position[0])

        # Achieving 20 points to win
        if snake.score == 20:
            winner = 'snake1 won!'
            running = False
        if second_snake.score == 20:
            winner = 'snake2 won!'
            running = False

        # displaying the score on the screen
        message(screen, f'Score1: {snake.score}', (0, 0), ORANGE, 'Arial', 24, True)

        message(screen, f'Score2: {second_snake.score}', (0, 25), ORANGE, 'Arial', 24, True)

        # Update of screen
        pygame.display.update()

        # Keeping the cycle on the correct speed
        clock.tick(FPS)

    # Creating a message, who won
    if winner != '':
        message(screen, winner, (20, 160), WHITE, 'Arial', 80)
        time.sleep(3)

    # Exit
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
