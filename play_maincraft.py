import pygame
from settings import level_map, height, weight
from create_level import Level


def play_game():
    #wires()
    pygame.init()
    screen = pygame.display.set_mode((weight, height))
    clock = pygame.time.Clock()
    fps = 60
    count = 0
    level = Level(level_map, screen, fps)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if count % 2 == 0:
                        level.flag = True
                    else:
                        level.flag = False
        screen.fill('black')
        level.run()
        if level.stop_play_maincraft:
            running = False
        pygame.display.update()
        clock.tick(fps)

play_game()