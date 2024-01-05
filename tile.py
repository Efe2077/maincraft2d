import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, texture='data/grass_tex2.jpg'):
        super().__init__()
        self.im = texture
        self.image = pygame.image.load(texture)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

    def show_image(self):
        return self.im