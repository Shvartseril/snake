import datetime
import random
from random import randint
import socket
import threading
from enum import Enum
import pickle


ID = int


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
        self.color = (randint(100, 255), 0, randint(100, 255))

    def move(self):
        if self.direction is None:
            return
        self.position[1:] = self.position[:-1]
        if self.direction == Direction.UP.value:
            self.position[0] = (self.position[0][0], self.position[0][1] + 1)
        if self.direction == Direction.DOWN.value:
            self.position[0] = (self.position[0][0], self.position[0][1] - 1)
        if self.direction == Direction.LEFT.value:
            self.position[0] = (self.position[0][0] - 1, self.position[0][1])
        if self.direction == Direction.RIGHT.value:
            self.position[0] = (self.position[0][0] + 1, self.position[0][1])
        if len(self.position) != len(set(self.position)):
            self.position = [(0, 0)]

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

    def __repr__(self):
        return str(self.position)


class Message:
    def __init__(self, msg: str, snakes: list[Snake], food: list[tuple[int, int]]):
        self.msg = msg
        self.snakes = snakes
        self.food = food


class Player:
    def __init__(self, snake: Snake, player_socket: socket.socket, player_id: ID):
        self.snake: Snake = snake
        self.socket: socket.socket = player_socket
        self.id = player_id


class SnakeFood:
    def __init__(self):
        self.snake_food: list[tuple[int, int]] = [(randint(-19, 19), randint(-29, 29))]

    # def crash(self, snakes):
    #     for frst_snake in snakes:
    #         for scnd_snake in snakes:
    #             if frst_snake.position[0] in scnd_snake.position and frst_snake.position[0] != scnd_snake.position[0]:
    #                 frst_snake.position = [(randint(-19, 19), randint(-29, 29))]

    def eating_food(self, snake):
        for food_id in range(len(self.snake_food)):
            if self.snake_food[food_id] in snake.position:
                self.snake_food[food_id] = (randint(-19, 19), randint(-29, 29))
                snake.eating()


class Server:

    def __init__(self,
                 ip: str = '0.0.0.0',
                 port: int = 8080,
                 field_size: tuple[int, int] = (40, 60)):
        self.ip: str = ip
        self.port: int = port
        self.field_size = field_size
        self.FPS: int = 10
        self.sock = None
        self.client_sockets: list[socket.socket] = []
        self.food = SnakeFood()
        self.max_id: int = 1
        self.players: dict[ID, Player] = {}

    def flick_world(self):
        for player in self.players.values():
            # self.food.crash(player.Snake)
            player.snake.move()
            player.snake.going_abroad()
            self.food.eating_food(player.snake)

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
        new_snake = Snake(position=[(random.randint(0, 10), random.randint(0, 10))], name=snake_name)
        current_player_id = self.max_id
        # new_snake = Snake(position=[(0, 0)], name=snake_name)
        self.players[current_player_id] = Player(new_snake, connection, current_player_id)
        self.max_id += 1
        direction = Direction.RIGHT.value

        while direction:
            new_snake.direction = direction
            try:
                direction = int(connection.recv(1024).decode())
            except ValueError:
                pass
            except ConnectionResetError:
                self.players.pop(current_player_id)

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
        message = Message('ok', [player.snake for player in self.players.values()], self.food.snake_food)
        ids_to_pop = []
        for player in self.players.values():
            try:
                player.socket.send(pickle.dumps(message))
            except ConnectionResetError:
                ids_to_pop.append(player.id)
        for id_to_pop in ids_to_pop:
            self.players.pop(id_to_pop)

            # print(self.snakes, '=self.snakes')
            # print(self.food.snake_food, '=self.food')
            #
            # client_socket.send(pickle.dumps(self.snakes))
            # print(f'self.snakes ({self.snakes}) have been sent')
            # client_socket.send(pickle.dumps(self.food.snake_food))
            # print(f'self.food.snake_food ({self.food.snake_food}) have been sent')


if __name__ == '__main__':
    beta_server = Server(port=8110)
    beta_server.run()
