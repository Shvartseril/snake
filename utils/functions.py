import pygame


def records_record(score):
    with open('record.txt', 'r') as file:
        current_record = int(file.read())
    if current_record > score:
        return current_record
    with open('record.txt', 'w') as file:
        file.write(str(score))
    return score


# Function for creating messages
def message(screen, msg: str, coordinates: tuple[int, int], color: tuple[int, int, int], font_name: str, font_size: int, bold: bool = False,
            italic: bool = False):
    font = pygame.font.SysFont(font_name, font_size, bold, italic)
    msg_screen = font.render(msg, False, color)
    screen.blit(msg_screen, coordinates)
    pygame.display.update()
