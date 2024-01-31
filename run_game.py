import pygame
from play_maincraft import play_game
from do import reset_all, return_furst_value
from add_custom import show_adding, draw_txt


pygame.init()
weight, height = 1200, 660
screen = pygame.display.set_mode((weight, height))
background_image = pygame.image.load('data/back.png')
background_image = pygame.transform.scale(background_image, (1200, 660))
screen.blit(background_image, (0, 0))

clock = pygame.time.Clock()
maincraft = True
fps = 60
run = True

print_reset = False
print_return = False

all_sprites = pygame.sprite.Group()
cur_im = pygame.image.load('data/sword.png')
cur = pygame.sprite.Sprite(all_sprites)
cur.image = cur_im
cur.rect = cur.image.get_rect()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if 52 <= x <= 232 and 45 <= y <= 219 and maincraft:
                play_game()
                screen = pygame.display.set_mode((weight, height))
                screen.blit(background_image, (0, 0))
            elif 375 <= x <= 555 and 45 <= y <= 219:
                pygame.mouse.set_visible(True)
                show_adding()
                screen = pygame.display.set_mode((weight, height))
            elif 705 <= x <= 885 and 45 <= y <= 219:
                reset_all()
                print_reset = True
                print_return = False
            elif 990 <= x <= 1170 and 45 <= y <= 219:
                return_furst_value()
                print_reset = False
                print_return = True
            else:
                print_reset = False
                print_return = False

        if event.type == pygame.MOUSEMOTION:
            cur.rect.topleft = event.pos
            pygame.mouse.set_visible(False)

    if print_reset:
        draw_txt(screen, '+', 50, 795, 300)
    elif print_return:
        draw_txt(screen, '+', 50, 1080, 300)
    all_sprites.draw(screen)
    pygame.display.update()
    screen.blit(background_image, (0, 0))
    clock.tick(fps)
    pygame.display.flip()
