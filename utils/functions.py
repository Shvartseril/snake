import pygame


def records_record(score):
    with open('record.txt', 'r') as file:
        current_record = int(file.read())
    if current_record > score:
        return current_record
    with open('record.txt', 'w') as file:
        file.write(str(score))
    return score


# Function for creating a square
def draw_square(screen, position: tuple[int, int], color: tuple[int, int, int], size: int):
    position = (position[0] * 10 + 200, position[1] * (-10) + 300)
    pygame.draw.rect(screen, color, [*position, size, size])


# Function for creating messages
def message(screen, msg: str, coordinates: tuple[int, int], color: tuple[int, int, int], font_name: str, font_size: int, bold: bool = False,
            italic: bool = False):
    font = pygame.font.SysFont(font_name, font_size, bold, italic)
    msg_screen = font.render(msg, False, color)
    screen.blit(msg_screen, coordinates)
    pygame.display.update()
