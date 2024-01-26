import pygame
from tile import Tile
from settings import tile_size, save, symbol_of_blocks, load_level
from player import Player
from random import choice
from do import get_list_of_blocks, get_dict


class Level:
    def __init__(self, level_data, surface, fps):
        self.display_surface = surface
        self.level_data = load_level('map.txt')
        self.blocks = get_dict()

        self.icons = {'X': 'data/grass_icon.png',
                      'W': 'data/wood_icon.png',
                      'L': 'data/leaf_icon.png',
                      'B': 'data/obsidian_icon.png',
                      'S': 'data/stone_icon.png'}

        self.blocks_sounds = {'X': f'data/sound/grass/{choice(["grass1.mp3", "grass2.mp3"])}',
                              'W': f'data/sound/wood/{choice(["wood1.mp3", "wood2.mp3"])}',
                              'L': f'data/sound/leaves/leaves1.mp3',
                              'B': f'data/sound/obsidian/{choice(["obsidian1.mp3", "obsidian2.mp3"])}',
                              'S': f'data/sound/stone/{choice(["stone1.mp3", "stone2.mp3"])}'}

        self.blocks_sounds_br = {'X': f'data/sound_break/grass/grass_break.mp3',
                                 'W': f'data/sound_break/wood/wood_break.mp3',
                                 'L': f'data/sound_break/leaves/leaves_break.mp3',
                                 'B': f'data/sound_break/obsidian/stone_break.mp3',
                                 'S': f'data/sound_break/stone/stone_break.mp3'}
        self.symbol = 'X'
        self.texture = self.blocks['X']
        self.setup_level(self.level_data)
        self.text = get_list_of_blocks()
        self.world_shift = 0
        self.fps = fps
        self.k_del = False
        self.count_e = 5 * fps
        self.count_q = 5
        self.stop_play_maincraft = False

    def draw_line_of_chose(self):
        if self.texture == self.blocks[self.text[0]]:
            pygame.draw.rect(self.display_surface, (pygame.Color('red')), (30, 30, 30, 30), 3)
        else:
            pygame.draw.rect(self.display_surface, (pygame.Color('black')), (30, 30, 30, 30), 2)
        if self.texture == self.blocks[self.text[1]]:
            pygame.draw.rect(self.display_surface, (pygame.Color('red')), (57, 30, 30, 30), 3)
        else:
            pygame.draw.rect(self.display_surface, (pygame.Color('black')), (30, 30, 60, 30), 2)
        if self.texture == self.blocks[self.text[2]]:
            pygame.draw.rect(self.display_surface, (pygame.Color('red')), (87, 30, 30, 30), 3)
        else:
            pygame.draw.rect(self.display_surface, (pygame.Color('black')), (30, 30, 90, 30), 2)
        if self.texture == self.blocks[self.text[3]]:
            pygame.draw.rect(self.display_surface, (pygame.Color('red')), (117, 30, 30, 30), 3)
        else:
            pygame.draw.rect(self.display_surface, (pygame.Color('black')), (30, 30, 120, 30), 2)
        if self.texture == self.blocks[self.text[4]]:
            pygame.draw.rect(self.display_surface, (pygame.Color('red')), (147, 30, 30, 30), 3)
        else:
            pygame.draw.rect(self.display_surface, (pygame.Color('black')), (30, 30, 150, 30), 2)

        x = 32
        y = 35

        for symbol in self.text[0: 5]:
            if symbol in list(self.icons.keys()):
                image = pygame.image.load(self.icons[symbol])
            else:
                image = pygame.image.load(self.blocks[symbol])
                image = pygame.transform.scale(image, (20, 20))
            rect = image.get_rect(topleft=(x, y))
            self.display_surface.blit(image, rect)
            x += 30

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.finish = pygame.sprite.GroupSingle()
        self.players = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                x_cor = col_index
                y_cor = row_index
                if cell != '.' and cell != 'P':
                    tile = Tile((x, y), self.blocks[self.level_data[y_cor][x_cor]])
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

        if self.texture == self.blocks[self.text[0]]:
            symbol = list(self.blocks.keys())[0]
        elif self.texture == self.blocks[self.text[1]]:
            symbol = list(self.blocks.keys())[1]
        elif self.texture == self.blocks[self.text[2]]:
            symbol = list(self.blocks.keys())[2]
        elif self.texture == self.blocks[self.text[3]]:
            symbol = list(self.blocks.keys())[3]
        elif self.texture == self.blocks[self.text[4]]:
            symbol = list(self.blocks.keys())[4]
        else:
            symbol = 'X'

        self.symbol = symbol

        play = False

        if symbol in symbol_of_blocks:
            s = pygame.mixer.Sound(self.blocks_sounds[symbol])
            s.set_volume(0.5)
            play = True

        if player.rect.y >= 660 or player.rect.x <= -60 or player.rect.y < -50:
            self.setup_level(self.level_data)
        elif keystate[pygame.K_c] and not self.k_del:
            y = int(player.rect.x / tile_size)
            if player.rect.x % tile_size >= 30:
                y += 1
            x = player.rect.y // tile_size
            if (-1 < x + 1 < 18 and -1 < y + 1 < len(self.level_data[x]) and self.level_data[x + 1][y + 1] != 'P' and
                    self.level_data[x + 1][y + 1] not in self.text):
                if self.check_build(x + 1, y + 1):
                    self.level_data[x + 1] = self.level_data[x + 1][: y + 1] + symbol + self.level_data[x + 1][y + 2:]
                    tile = Tile(((y + 1) * tile_size, (x + 1) * tile_size), self.texture)
                    self.tiles.add(tile)
                    if play:
                        s.play()

        elif keystate[pygame.K_x] and not self.k_del:
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if (-1 < x + 1 < 18 and -1 < y - 1 < len(self.level_data[x]) and self.level_data[x + 1][y - 1] != 'P' and
                    self.level_data[x + 1][y - 1] not in self.text):
                if self.check_build(x + 1, y - 1):
                    self.level_data[x + 1] = self.level_data[x + 1][: y - 1] + symbol + self.level_data[x + 1][y:]
                    tile = Tile(((y - 1) * tile_size, (x + 1) * tile_size), self.texture)
                    self.tiles.add(tile)
                    if play:
                        s.play()

        elif keystate[pygame.K_e] and not self.k_del:
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if (-1 < x - 1 < 18 and -1 < y + 1 < len(self.level_data[x]) and self.level_data[x - 1][y + 1] != 'P' and
                    self.level_data[x - 1][y + 1] not in self.text):
                if self.check_build(x - 1, y + 1):
                    self.level_data[x - 1] = self.level_data[x - 1][: y + 1] + symbol + self.level_data[x - 1][y + 2:]
                    tile = Tile(((y + 1) * tile_size, (x - 1) * tile_size), self.texture)
                    self.tiles.add(tile)
                    if play:
                        s.play()

        elif keystate[pygame.K_q] and not self.k_del:
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if (-1 < x - 1 < 18 and -1 < y - 1 < len(self.level_data[x]) and self.level_data[x - 1][y - 1] != 'P' and
                    self.level_data[x - 1][y - 1] not in self.text):
                if self.check_build(x - 1, y - 1):
                    self.level_data[x - 1] = self.level_data[x - 1][: y - 1] + symbol + self.level_data[x - 1][y:]
                    tile = Tile(((y - 1) * tile_size, (x - 1) * tile_size), self.texture)
                    self.tiles.add(tile)
                    if play:
                        s.play()

        elif keystate[pygame.K_r]:
            self.setup_level(self.level_data)

    def check_build(self, x, y):
        text = self.text
        try:
            if (self.level_data[x - 1][y] in text or self.level_data[x][y - 1] in text or
                    self.level_data[x][y + 1] in text or self.level_data[x + 1][y] in text):
                return True
            else:
                return False
        except Exception:
            return False

    def destroy(self):
        if self.k_del:
            f2 = pygame.font.SysFont('serif', 20)
            text2 = f2.render("Удалить", False, (0, 255, 0))
            self.display_surface.blit(text2, (10, 0))

            keystate = pygame.key.get_pressed()

            player = self.players.sprite
            y = int(player.rect.x / tile_size)
            x = player.rect.y // tile_size
            if keystate[pygame.K_c]:
                if -1 < x < 18 and -1 < y + 1 < len(self.level_data[x]) and self.level_data[x + 1][y + 1] != 'P':
                    self.delete_block(x + 1, y + 1)
                    self.level_data[x + 1] = self.level_data[x + 1][: y + 1] + '.' + self.level_data[x + 1][y + 2:]

            elif keystate[pygame.K_x]:
                if -1 < x < 18 and -1 < y - 1 < len(self.level_data[x]) and self.level_data[x + 1][y - 1] != 'P':
                    self.delete_block(x + 1, y - 1)
                    self.level_data[x + 1] = self.level_data[x + 1][: y - 1] + '.' + self.level_data[x + 1][y:]

            elif keystate[pygame.K_e]:
                if -1 < x - 1 < 18 and -1 < y + 1 < len(self.level_data[x]) and self.level_data[x - 1][y + 1] != 'P':
                    self.delete_block(x - 1, y + 1)
                    self.level_data[x - 1] = self.level_data[x - 1][: y + 1] + '.' + self.level_data[x - 1][y + 2:]

            elif keystate[pygame.K_q]:
                if -1 < x - 1 < 18 and -1 < y - 1 < len(self.level_data[x]) and self.level_data[x - 1][y - 1] != 'P':
                    self.delete_block(x - 1, y - 1)
                    self.level_data[x - 1] = self.level_data[x - 1][: y - 1] + '.' + self.level_data[x - 1][y:]

    def delete_block(self, x, y):
        flag = False
        text = self.text
        for row_index, row in enumerate(self.level_data):
            for col_index, cell in enumerate(row):
                if col_index == y and row_index == x:
                    if self.level_data[row_index][col_index] in text:
                        flag = True
        if flag:
            for sprite in self.tiles.sprites():
                del_y = int(sprite.rect.x / tile_size)
                del_x = sprite.rect.y // tile_size
                if flag:
                    if x == del_x and y == del_y:
                        s = pygame.mixer.Sound('data/chponk.mp3')
                        s.set_volume(0.05)
                        s.play()
                        sprite.kill()

    def run(self):
        self.tiles.draw(self.display_surface)

        self.players.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.draw_line_of_chose()
        save(self.level_data, 'map.txt')
        self.players.draw(self.display_surface)
        self.check_player()
        self.destroy()
