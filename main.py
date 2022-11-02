import pygame
import socket
import settings
from drawing import drawing_food_and_snake, draw_messages, draw_message_who_won
from movement import handle_events
import pickle
from snake import snake, second_snake, food
from utils.colors import BLACK


# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('', 9090))


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("My Game")

    clock = pygame.time.Clock()

    while settings.running:

        food.crash()

        snake.move()
        second_snake.move()

        snake.going_abroad()
        second_snake.going_abroad()

        screen.fill(BLACK)

        drawing_food_and_snake(screen)

        food.eating_food()

        snake.check_win()
        second_snake.check_win()

        draw_messages(screen)

        pygame.display.update()

        clock.tick(settings.FPS)

    draw_message_who_won(screen)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
