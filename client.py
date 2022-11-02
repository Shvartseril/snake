import socket
import sys
import pygame
import threading
import pickle
from server import Snake


class Client:
    def __init__(self):
        self.sock = None
        self.direction = None
        self.position: tuple[int, int] = (1, 1)
        self.snake_food_coordinates: list[tuple[int, int]] = [(5, 5)]
        self.WIDTH: int = 400
        self.HEIGHT: int = 600
        self.screen = None
        self.snake_color: tuple[int, int, int] = (255, 0, 0)
        self.snake_food_color: tuple[int, int, int] = (0, 255, 0)
        self.FPS: int = 10
        self.snakes = []

    def run(self):
        self.sock = socket.socket()
        self.sock.connect(('localhost', 8110))
        get_field_state_thread = threading.Thread(target=self.handle_connection)
        get_field_state_thread.start()
        notify_server_thread = threading.Thread(target=self.send_to_server)
        notify_server_thread.start()
        game_thread = threading.Thread(target=self.draw_run)
        game_thread.start()

    def handle_connection(self):
        while True:
            self.snakes = pickle.loads(self.sock.recv(1024))
            print(self.snakes)
            # self.draw_run()
            # self.send_to_server()

    def send_to_server(self):
        self.sock.send(str(self.direction).encode())

    def draw_square(self, color, ppposition):
        position = (ppposition[0] * 10 + 200, ppposition[1] * (-10) + 300)
        pygame.draw.rect(self.screen, color, [*position, 10, 10])

    def drawing_food_and_snake(self):
        self.screen.fill('black')
        for i in self.snake_food_coordinates:
            self.draw_square(self.snake_food_color, i)
        for snake in self.snakes:
            for position in snake.position:
                self.draw_square(self.snake_color, position)

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
