import pygame
from settings import level_map, height, weight
from create_level import Level


def play_game():
    pygame.init()
    screen = pygame.display.set_mode((weight, height))
    clock = pygame.time.Clock()
    fps = 60
    count_for_del = 0
    count_for_wood = 0
    count_for_leafes = 0
    count_for_grass = 0
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
                elif event.key == pygame.K_1:
                    level.texture = level.blocks['X']
                elif event.key == pygame.K_2:
                    level.texture = level.blocks['W']
                elif event.key == pygame.K_3:
                    level.texture = level.blocks['L']
                elif event.key == pygame.K_4:
                    level.texture = level.blocks['B']
                elif event.key == pygame.K_5:
                    level.texture = level.blocks['S']
        screen.fill('white')
        level.run()
        if level.stop_play_maincraft:
            running = False
        pygame.display.update()
        clock.tick(fps)
