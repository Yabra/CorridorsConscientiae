import pygame
import random
from data_loader import load_image
from Tile import Tile, TileType
from Monster import Monster
from Item import Item
from Player import Player
from Camera import Camera


class Labyrinth:
    # sprites_group - группа всех спрайтов для отрисовки камерой
    # maze          - двумерный список с описанием всех клеток
    def __init__(self, game, sprites_group, items_group, monsters_group, maze):
        tile_size = load_image("floor.png").get_width()
        self.size = (len(maze[0]), len(maze))
        self.tiles_group = pygame.sprite.Group()
        self.sprites_group = sprites_group
        self.tiles = [[None for _y in range(self.size[0])] for _x in range(self.size[1])]

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if maze[y][x] == "w":
                    for dx in range(0, 2):
                        for dy in range(0, 2):
                            Tile(
                                sprites_group,
                                self.tiles_group,
                                TileType.WALL,
                                ((x * 2 + dx) * tile_size, (y * 2 + dy) * tile_size)
                            )

                else:
                    for dx in range(0, 2):
                        for dy in range(0, 2):
                            Tile(
                                sprites_group,
                                self.tiles_group,
                                TileType.FLOOR,
                                ((x * 2 + dx) * tile_size, (y * 2 + dy) * tile_size)
                            )

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if maze[y][x] == "m":
                    Monster(
                        sprites_group,
                        monsters_group,
                        pygame.math.Vector2((x * 2 + 0.5) * tile_size, (y * 2 + 0.5) * tile_size),
                        game.add_lostness
                    )

                elif maze[y][x] == "k":
                    if random.randint(0, 1):
                        Item(
                            sprites_group,
                            items_group,
                            ((x * 2 + 0.5) * tile_size, (y * 2 + random.choice([0, 0.5, 1.25, 1.5])) * tile_size),
                            game.heal_mind, "crystal0.png"
                        )  # кристалл восстановления разума

                    else:
                        Item(
                            sprites_group,
                            items_group,
                            ((x * 2 + 0.5) * tile_size, (y * 2 + random.choice([0, 0.5, 1.25, 1.5])) * tile_size),
                            game.remove_lostness,
                            "crystal1.png"
                        )  # кристалл уменьшения потерянности

                elif maze[y][x] == "t":
                    Item(
                        sprites_group,
                        items_group,
                        ((x * 2 + 0.5) * tile_size, (y * 2 + 0.5) * tile_size),
                        lambda: game.make_state_transition(game.next_level),
                        "portal.png"
                    )

                elif maze[y][x] == "e":
                    mind = Player.max_mind
                    if game.player:
                        mind = game.player.mind
                    game.player = Player(
                        sprites_group,
                        pygame.math.Vector2((x * 2 + 0.5) * tile_size, (y * 2 + 0.5) * tile_size),
                        mind
                    )
                    game.camera = Camera(pygame.math.Vector2((x * 2 + 0.5) * tile_size, (y * 2 + 0.5) * tile_size))
