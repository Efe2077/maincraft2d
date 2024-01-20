import pygame
from play_maincraft import play_game


pygame.init()
weight, height = 1200, 675
screen = pygame.display.set_mode((weight, height))
background_image = pygame.image.load('data/back.png')
screen.blit(background_image, (0, 0))
clock = pygame.time.Clock()
maincraft = True
fps = 60
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 74 <= event.pos[0] <= 198 and 38 <= event.pos[1] <= 159 and maincraft:
                play_game()
                screen = pygame.display.set_mode((weight, height))
                background_image = pygame.image.load('data/back.png')
                screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(fps)
