import pygame
from settings import level_map, height, weight
from create_level import Level


def play_game():
    pygame.init()
    screen = pygame.display.set_mode((weight, height))
    clock = pygame.time.Clock()
    fps = 60
    count_for_del = 0
    count_for_texture = 0
    level = Level(level_map, screen, fps)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if count_for_del % 2 == 0:
                        level.k_del = True
                    else:
                        level.k_del = False
                    count_for_del += 1
                if event.key == pygame.K_1:
                    if count_for_texture % 2 == 0:
                        level.k_wood = True
                    else:
                        level.k_wood = False
                    count_for_texture += 1
        screen.fill('white')
        level.run()
        if level.stop_play_maincraft:
            running = False
        pygame.display.update()
        clock.tick(fps)


play_game()
