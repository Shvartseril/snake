from enum import Enum
from random import randint
from typing import Optional

import settings


class Direction(Enum):
    UP = 1
    RIGHT = 2
    LEFT = 4
    DOWN = 3


class SelfIntersection(Exception):
    pass


class Snake:
    def __init__(self, position: list[tuple[int, int]], name: str):
        self.position = position
        self.score = 0
        self.next_head = (0, 0)
        self.direction: Optional[Direction] = None
        self.winner = None
        self.name = name

    def move(self):
        if self.direction is None:
            return
        self.position[1:] = self.position[:-1]
        if self.direction == Direction.UP:
            self.position[0] = (self.position[0][0], self.position[0][1] + 1)
        if self.direction == Direction.DOWN:
            self.position[0] = (self.position[0][0], self.position[0][1] - 1)
        if self.direction == Direction.LEFT:
            self.position[0] = (self.position[0][0] - 1, self.position[0][1])
        if self.direction == Direction.RIGHT:
            self.position[0] = (self.position[0][0] + 1, self.position[0][1])
        if len(self.position) != len(set(self.position)):
            self.position = [(0, 0)]
            if self.score >= 5:
                self.score -= 5
            else:
                self.score = 0

    def going_abroad(self):
        if self.position[0][0] < -20:
            self.position[0] = 19, self.position[0][1]
        if self.position[0][0] > 19:
            self.position[0] = -20, self.position[0][1]
        if self.position[0][1] < -29:
            self.position[0] = self.position[0][0], 30
        if self.position[0][1] > 30:
            self.position[0] = self.position[0][0], -30

    def eating(self):
        self.position.append((self.position[-1]))
        self.score += 1

    def check_win(self):
        if self.score == 20:
            settings.running = False
            self.winner = self.name

    def __repr__(self):
        return str(self.position)


class SnakeFood:
    def __init__(self):
        self.snake_food = (randint(-19, 19), randint(-29, 29))
        self.snake_food_coordinates = []

    def crash(self):
        if snake.position[0] in second_snake.position and snake.position[0] != second_snake.position[0]:
            self.snake_food_coordinates += snake.position
            snake.position = [(randint(-19, 19), randint(-29, 29))]

        if second_snake.position[0] in snake.position and second_snake.position[0] != snake.position[0]:
            self.snake_food_coordinates += second_snake.position
            second_snake.position = [(randint(-19, 19), randint(-29, 29))]

    def eating_food(self):
        if self.snake_food in snake.position:
            self.snake_food = (randint(-19, 19), randint(-29, 29))
            settings.FPS += 0.3
            snake.eating()

        if self.snake_food in second_snake.position:
            self.snake_food = (randint(-19, 19), randint(-29, 29))
            settings.FPS += 0.3
            second_snake.eating()

        if snake.position[0] in self.snake_food_coordinates:
            snake.eating()
            self.snake_food_coordinates.remove(snake.position[0])

        if second_snake.position[0] in self.snake_food_coordinates:
            second_snake.eating()
            self.snake_food_coordinates.remove(second_snake.position[0])


snake = Snake([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)], 'snake')
second_snake = Snake([(-8, 0), (-8, -1), (-8, -2), (-8, -3)], 'second snake')

food = SnakeFood()
