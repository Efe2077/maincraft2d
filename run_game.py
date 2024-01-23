import pygame
from play_maincraft import play_game


pygame.init()
weight, height = 1200, 660
screen = pygame.display.set_mode((weight, height))
background_image = pygame.image.load('data/back2.png')
screen.blit(background_image, (0, 0))

clock = pygame.time.Clock()
maincraft = True
fps = 60
run = True

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
            if 74 <= event.pos[0] <= 198 and 38 <= event.pos[1] <= 159 and maincraft:
                play_game()
                screen = pygame.display.set_mode((weight, height))
                background_image = pygame.image.load('data/back2.png')
                screen.blit(background_image, (0, 0))
        if event.type == pygame.MOUSEMOTION:
            cur.rect.topleft = event.pos
            pygame.mouse.set_visible(False)
    all_sprites.draw(screen)
    pygame.display.update()
    screen.blit(background_image, (0, 0))
    clock.tick(fps)
