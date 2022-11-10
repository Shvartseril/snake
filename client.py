import socket
import sys
import pygame
import threading
import pickle
import time
from server import Snake, SnakeFood, Message
from random import randint


class Client:
    def __init__(self):
        self.sock = None
        self.direction = None
        self.position: tuple[int, int] = (1, 1)
        self.WIDTH: int = 400
        self.HEIGHT: int = 600
        self.screen = None
        self.snake_food_color: tuple[int, int, int] = (0, 255, 0)
        self.FPS: int = 10
        self.snakes = []
        self.food = [(5, 5)]

    def run(self):
        self.sock = socket.socket()
        self.sock.connect(('37.228.116.65', 8110))
        get_field_state_thread = threading.Thread(target=self.handle_connection)
        get_field_state_thread.start()
        notify_server_thread = threading.Thread(target=self.send_to_server)
        notify_server_thread.start()
        game_thread = threading.Thread(target=self.draw_run)
        game_thread.start()

    def handle_connection(self):
        while True:
            recv: Message = pickle.loads(self.sock.recv(2048))
            self.snakes = recv.snakes
            self.food = recv.food

            # self.snakes = pickle.loads(self.sock.recv(2048))
            # self.food = pickle.loads(self.sock.recv(2048))
            # print(self.snakes, '=self.snakes in handle_connection')
            # print(self.food, '=self.food in handle_connection')

    def send_to_server(self):
        self.sock.send(str(self.direction).encode())

    def draw_square(self, color, old_position):
        # if type(old_position) == list:
        #     print('Михаил, обычно type(old_position) == tuple, но СЕЙЧАС ОН LIST')
        #     print('ОН иногда СТАНОВИТСЯ LISTом, а иногда нет! Я НЕ ПОНИМАЮ ПОЧЕМУ ЭТО ЕМАЕЕЕЕЕ')
        #     print('У МЕНЯ ИЗ-ЗА ЭТОГО ВЕСЬ КОД ЛОМАЕТСЯ К ЧЕРТЯМ')
        #     print('Почему-то в один момент self.food == self.snakes')
        #     print(self.snakes, '=self.snakes')
        #     print(self.food, '=self.food')
        #     print(old_position, '=old_position')
        #     print(type(old_position), '=type(old_position()')

        position = (old_position[0] * 10 + 200, old_position[1] * (-10) + 300)
        pygame.draw.rect(self.screen, color, [*position, 10, 10])

    def drawing_food_and_snake(self):
        self.screen.fill('black')
        for food in self.food:
            self.draw_square(self.snake_food_color, food)
        for snake in self.snakes:
            for position in snake.position:
                self.draw_square(snake.color, position)

    def draw_run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = 4
                        self.send_to_server()
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 2
                        self.send_to_server()
                    elif event.key == pygame.K_DOWN:
                        self.direction = 3
                        self.send_to_server()
                    elif event.key == pygame.K_UP:
                        self.direction = 1
                        self.send_to_server()
            self.drawing_food_and_snake()
            pygame.display.update()


if __name__ == '__main__':
    cl = Client()
    cl.run()
# cl.handle_connection()
