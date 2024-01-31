import pygame
import os
from do import do_change


def draw_txt(screen, text, size, x, y, color=(100, 255, 100)):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))


def show_adding():
    pygame.init()
    weight, height = 660, 660
    screen = pygame.display.set_mode((weight, height))
    color = pygame.Color((248, 240, 255))
    screen.fill(color)

    run = True
    error = False
    flag = False

    bool_text = False
    print_text = True
    text = ''

    bool_symbol = False
    print_symbol = True
    symbol = ''

    bool_number = False
    print_number = True
    number = ''

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                # text
                if 37 <= x <= 577 and 72 <= y <= 130:
                    bool_text = True
                else:
                    bool_text = False
                # symbol
                if 37 <= x <= 577 and 252 <= y <= 312:
                    bool_symbol = True
                else:
                    bool_symbol = False
                # number
                if 37 <= x <= 577 and 432 <= y <= 492:
                    bool_number = True
                else:
                    bool_number = False

                if weight // 2 - 135 <= x <= weight // 2 + 135 and 525 <= y <= 605:
                        if (os.path.isfile(f"data/{text}") and len(symbol) == 1 and len(number) == 1 and
                                number.isdigit()):
                            do_change(text, symbol, int(number))
                            flag = True
                            error = False
                        else:
                            error = True
            elif event.type == pygame.KEYDOWN:
                if bool_text:
                    if event.key == pygame.K_RETURN:
                        bool_text = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 25:
                            text += event.unicode

                elif bool_symbol:
                    if event.key == pygame.K_RETURN:
                        bool_symbol = False
                    elif event.key == pygame.K_BACKSPACE:
                        symbol = symbol[:-1]
                    else:
                        if len(symbol) < 1:
                            symbol += event.unicode

                elif bool_number:
                    if event.key == pygame.K_RETURN:
                        bool_number = False
                    elif event.key == pygame.K_BACKSPACE:
                        number = number[:-1]
                    else:
                        if len(number) < 1:
                            number += event.unicode

        screen.fill(color)
        draw_txt(screen, 'Напишите название текстурки:', 45, 36, 20, color=(241, 112, 255))
        draw_txt(screen, 'Напишите символ текстурки:', 45, 36, 200, color=(241, 112, 255))
        draw_txt(screen, 'Напишите номер слота:', 45, 36, 380, color=(241, 112, 255))

        r = weight // 2 - 100
        pygame.draw.rect(screen, (198, 255, 194), (r - 35, 525, r + 25, 80))
        draw_txt(screen, 'Завершить ', 50, r, 550)

        if error:
            draw_txt(screen, 'Проверьте данные', 20, 250, 610, color=(0, 0, 0))

        if flag:
            draw_txt(screen, 'Добавлено', 20, 250, 610)

        if bool_text:
            pygame.draw.rect(screen, (0, 0, 0), (35, 70, 540, 60), 2)
        else:
            pygame.draw.rect(screen, (255, 179, 179), (35, 70, 540, 60), 2)

        if bool_symbol:
            pygame.draw.rect(screen, (0, 0, 0), (35, 250, 540, 60), 2)
        else:
            pygame.draw.rect(screen, (255, 179, 179), (35, 250, 540, 60), 2)

        if bool_number:
            pygame.draw.rect(screen, (0, 0, 0), (35, 430, 540, 60), 2)
        else:
            pygame.draw.rect(screen, (255, 179, 179), (35, 430, 540, 60), 2)

        if print_text:
            draw_txt(screen, text, 50, 41, 80, color=(248, 179, 255))
        if print_symbol:
            draw_txt(screen, symbol, 50, 41, 260, color=(248, 179, 255))
        if print_number:
            draw_txt(screen, number, 50, 41, 440, color=(248, 179, 255))
        pygame.display.flip()


