import datetime
import random
from random import randint
import socket
import threading
from enum import Enum
import pickle


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
        self.direction = Direction.RIGHT.value
        self.winner = None
        self.name = name

    def move(self):
        if self.direction is None:
            return
        self.position[1:] = self.position[:-1]
        print('movinggggg', self.direction, type(self.direction), Direction.UP.value)
        if self.direction == Direction.UP.value:
            print('HEEEEYEYYYYYY!!!!')
            self.position[0] = (self.position[0][0], self.position[0][1] + 1)
        if self.direction == Direction.DOWN.value:
            self.position[0] = (self.position[0][0], self.position[0][1] - 1)
        if self.direction == Direction.LEFT.value:
            self.position[0] = (self.position[0][0] - 1, self.position[0][1])
        if self.direction == Direction.RIGHT.value:
            self.position[0] = (self.position[0][0] + 1, self.position[0][1])
        if len(self.position) != len(set(self.position)):
            self.position = [(0, 0)]
            if self.score >= 5:
                self.score -= 5
            else:
                self.score = 0

    # remove magic numbers
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

    def __repr__(self):
        return str(self.position)


class SnakeFood:
    def __init__(self):
        self.snake_food = (randint(-19, 19), randint(-29, 29))

    # def crash(self):
    #     if snake.position[0] in second_snake.position and snake.position[0] != second_snake.position[0]:
    #         self.snake_food_coordinates += snake.position
    #         snake.position = [(randint(-19, 19), randint(-29, 29))]
    #
    #     if second_snake.position[0] in snake.position and second_snake.position[0] != snake.position[0]:
    #         self.snake_food_coordinates += second_snake.position
    #         second_snake.position = [(randint(-19, 19), randint(-29, 29))]

    def eating_food(self, snake):
        if self.snake_food in snake.position:
            self.snake_food = (randint(-19, 19), randint(-29, 29))
            snake.eating()


class Server:

    def __init__(self,
                 ip: str = '0.0.0.0',
                 port: int = 8080,
                 field_size: tuple[int, int] = (40, 60)):
        self.ip: str = ip
        self.port: int = port
        self.field_size = field_size
        self.snakes: list = []
        self.FPS: int = 10
        self.sock = None
        self.client_sockets: list[socket.socket] = []
        self.connections = []
        self.direction = None
        self.food = SnakeFood()

    def flick_world(self):
        for snake in self.snakes:
            snake.move()
            snake.going_abroad()
            self.food.eating_food(snake)

    def run(self):
        self.sock = socket.socket()
        self.sock.bind(('', self.port))
        self.sock.listen(10)
        x = threading.Thread(target=self.receive_connections)
        x.start()
        prev_flick_moment = datetime.datetime.now()
        while True:
            if prev_flick_moment + datetime.timedelta(
                    seconds=1) / self.FPS < datetime.datetime.now():
                self.flick_world()
                self.send_all_connections()
                prev_flick_moment = datetime.datetime.now()

    def handle_connection(self,
                          connection: socket.socket,
                          snake_name: str = 'username'):
        new_snake = Snake(position=[(random.randint(0, 10), random.randint(0, 10)),],name=snake_name)
        self.snakes.append(new_snake)
        direction = Direction.RIGHT.value

        while direction:
            new_snake.direction = direction
            print(direction)
            print(new_snake.direction)
            try:
                direction = int(connection.recv(1024).decode())
            except ValueError:
                pass
        # Remove snake

    def receive_connections(self):
        print('start recv conn')
        while True:
            new_client_connection, new_client_d = self.sock.accept()
            self.client_sockets.append(new_client_connection)
            waiter = threading.Thread(target=self.handle_connection,
                                      args=(new_client_connection,
                                            'brave_snake'))
            waiter.start()

    def send_all_connections(self):
        for client_socket in self.client_sockets:
            client_socket.send(pickle.dumps(self.snakes))
            client_socket.send(pickle.dumps(self.food.snake_food))


if __name__ == '__main__':
    beta_server = Server(port=8110)
    beta_server.run()
