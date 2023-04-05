import random
import pygame
import time

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird # 2
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD # 2

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.typeobstacle = random.randint(0, 2) # 2
        if len(self.obstacles) == 0:
            if self.typeobstacle == 0: # 2
                Cactus.Y_POS_CACTUS = 325
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)
            elif self.typeobstacle == 1: # 2
                Cactus.Y_POS_CACTUS = 300
                cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(cactus)
            else: # 2
                Bird.Y_POS_BIRD = random.randint(100, 300)
                bird = Bird(BIRD)
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.dead = True # 3
                game.playing = False 
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []