import pygame
from support import import_folder
from settings import tile_size


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {}
        self.character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.tile_size = tile_size
        self.speed = 5
        self.gravity = 0.8
        self.jump = True
        self.jump_speed = -11
        self.status = 'idle'
        self.right = True

    def character_assets(self):
        path = 'data/hero_move2/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for anim in self.animations.keys():
            full_path = path + anim
            self.animations[anim] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > self.gravity + 0.1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def gravitation(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.direction.x = -1
            self.right = False
        elif keystate[pygame.K_d]:
            self.direction.x = 1
            self.right = True
        else:
            self.direction.x = 0

        if keystate[pygame.K_SPACE]:
            if not self.jump:
                if self.direction.y == 0:
                    self.jump = True
            else:
                if self.direction.y == 0:
                    self.jumping()
                    self.jump = False

        if keystate[pygame.K_w]:
            self.direction.y = -self.gravity - 2

    def jumping(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.move()
        self.get_status()
        self.animate()
