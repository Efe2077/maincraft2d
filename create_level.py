import pygame
from tile import Tile
from settings import tile_size, weight
from player import Player


class Level:
    def __init__(self, level_data, surface, fps):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(self.level_data)
        self.world_shift = 0
        self.fps = fps
        self.flag = False
        self.count_e = 5 * fps
        self.count_q = 5
        self.stop_play_maincraft = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.finish = pygame.sprite.GroupSingle()
        self.players = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y))
                    self.tiles.add(tile)
                elif cell == 'P':
                    player = Player((x, y))
                    self.players.add(player)

    def horizontal_collision(self):
        player = self.players.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.show_image():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.players.sprite
        player.gravitation()

        for sprite in self.tiles.sprites():
            if sprite.show_image():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0

    def check_player(self):
        player = self.players.sprite
        keystate = pygame.key.get_pressed()
        if player.rect.y >= 660:
            self.setup_level(self.level_data)
        elif keystate[pygame.K_e] and not self.flag:
            y = int(player.rect.x / tile_size)
            if player.rect.x % tile_size >= 30:
                y += 1
            x = player.rect.y // tile_size
            if (x < 10 and y + 1 < len(self.level_data[x]) and self.level_data[x + 1][y + 1] != 'P' and
                    self.level_data[x + 1][y + 1] != 'X'):
                if self.check_build(x + 1, y + 1):
                    self.level_data[x + 1] = self.level_data[x + 1][: y + 1] + 'X' + self.level_data[x + 1][y + 2:]
                    tile = Tile(((y + 1) * tile_size, (x + 1) * tile_size))
                    self.tiles.add(tile)
        elif keystate[pygame.K_q] and not self.flag:
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if x < 10 and y - 1 > 0 and self.level_data[x + 1][y - 1] != 'P' and self.level_data[x + 1][y - 1] != 'X':
                if self.check_build(x + 1, y - 1):
                    self.level_data[x + 1] = self.level_data[x + 1][: y - 1] + 'X' + self.level_data[x + 1][y:]
                    tile = Tile(((y - 1) * tile_size, (x + 1) * tile_size))
                    self.tiles.add(tile)
        elif keystate[pygame.K_r]:
            self.setup_level(self.level_data)

    def check_build(self, x, y):
        try:
            if (self.level_data[x - 1][y - 1] == 'X' or self.level_data[x - 1][y] == 'X' or
                    self.level_data[x - 1][y + 1] == 'X' or
                    self.level_data[x][y - 1] == 'X' or self.level_data[x][y + 1] == 'X' or
                    self.level_data[x + 1][y - 1] == 'X' or self.level_data[x + 1][y] == 'X' or
                    self.level_data[x + 1][y + 1] == 'X'):
                return True
            else:
                return False
        except Exception:
            return False

    def destroy(self):
        if self.flag:
            keystate = pygame.key.get_pressed()
            player = self.players.sprite
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if keystate[pygame.K_e]:
                if x < 10 and y + 1 < len(self.level_data[x]) and self.level_data[x + 1][y + 1] != 'P':
                    self.level_data[x + 1] = self.level_data[x + 1][: y + 1] + ' ' + self.level_data[x + 1][y + 2:]
                    tile = Tile(((y + 1) * tile_size, (x + 1) * tile_size), texture=False, vision=False)
                    self.tiles.add(tile)

            elif keystate[pygame.K_q]:
                if x < 10 and y - 1 > 0 and self.level_data[x+1][y-1] != 'P':
                    self.level_data[x + 1] = self.level_data[x + 1][: y - 1] + ' ' + self.level_data[x + 1][y:]
                    tile = Tile(((y - 1) * tile_size, (x + 1) * tile_size), texture=False, vision=False)
                    self.tiles.add(tile)
            self.tiles.draw(self.display_surface)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.finish.draw(self.display_surface)
        self.finish.update(self.world_shift)

        self.players.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.players.draw(self.display_surface)
        self.check_player()
        self.destroy()