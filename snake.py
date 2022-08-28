from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    LEFT = 4
    DOWN = 3


class SelfIntersection(Exception):
    pass


class Snake:
    def __init__(self, position: list[tuple[int, int]]):
        self.position = position

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
            raise SelfIntersection()

    def eating(self):
        self.position.append((self.position[-1]))

    def going_abroad(self):
        if self.position[0][0] >= 21 or self.position[0][0] <= -21:
            self.position[0] = -self.position[0][0], self.position[0][1]
        if self.position[0][1] >= 31 or self.position[0][1] <= -31:
            self.position[0] = self.position[0][0], -self.position[0][1]

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
