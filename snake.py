from enum import Enum
from typing import Union


class Direction(Enum):
    UP = 1
    RIGHT = 2
    LEFT = 4
    DOWN = 3


class SelfIntersection(Exception):
    pass


class Snake:
    def __init__(self, position: list[tuple[int, int]]):
        self.direction: bool = False
        self.position: list[tuple[int, int]] = position
        self.score: int = 0

    def move(self, direction: Direction):
        self.position[1:] = self.position[:-1]
        if direction == Direction.UP:
            self.position[0] = (self.position[0][0], self.position[0][1] + 1)
        if direction == Direction.DOWN:
            self.position[0] = (self.position[0][0], self.position[0][1] - 1)
        if direction == Direction.LEFT:
            self.position[0] = (self.position[0][0] - 1, self.position[0][1])
        if direction == Direction.RIGHT:
            self.position[0] = (self.position[0][0] + 1, self.position[0][1])
        if len(self.position) != len(set(self.position)):
            self.position = [(0, 0)]
            if self.score >= 5:
                self.score -= 5
            else:
                self.score = 0

    def eating(self):
        self.position.append((self.position[-1]))
        self.score += 1

    def going_abroad(self):
        # if self.position[0][0] > 19 or self.position[0][0] < -20:
        #     self.position[0] = -self.position[0][0], self.position[0][1]
        # if self.position[0][1] >= 30 or self.position[0][1] <= -30:
        #     self.position[0] = self.position[0][0], -self.position[0][1]
        if self.position[0][0] < -20:
            self.position[0] = 19, self.position[0][1]
        if self.position[0][0] > 19:
            self.position[0] = -20, self.position[0][1]
        if self.position[0][1] < -29:
            self.position[0] = self.position[0][0], 30
        if self.position[0][1] > 30:
            self.position[0] = self.position[0][0], -30

    def __repr__(self):
        return str(self.position)


if __name__ == '__main__':
    snake = Snake([(1, 1), (1, 0), (0, 0), (0, -1)])
    try:
        snake.move(Direction.DOWN)
    except SelfIntersection:
        print('ERROR OCCURRED')
    # snake.move(Direction.UP)
    print(snake)
