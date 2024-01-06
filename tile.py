import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, texture, vision=True):
        super().__init__()
        self.im = texture
        self.draw = True
        if not texture:
            self.draw = False
            self.vision = False
        else:
            self.image = pygame.image.load(texture)
            self.vision = vision
            self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        if self.draw:
            self.rect.x += x_shift

    def show_image(self):
        if self.vision:
            return True
        else:
            return False