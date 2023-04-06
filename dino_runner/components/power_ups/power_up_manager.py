import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.throwhammer import ThrowHammer


from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, HAMMER, DEFAULT_TYPE

class PowerUpManeger:
    def __init__(self):
        self.power_ups = []
        self.throws = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(50, 70)
        self.power_up_shield = False
        self.power_up_hammer = False
        self.throwhammer = False
        
    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()
            
            
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                # 20:37:00
                if self.power_up_shield: # 1
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = SHIELD_TYPE
                    game.player.power_up_time = power_up.start_time + (self.duration + 1000)
                    self.power_ups.remove(power_up)
                elif self.power_up_hammer:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = HAMMER_TYPE
                    
                    game.player.power_up_time = power_up.start_time + (self.duration + 2000)
                    self.power_ups.remove(power_up)
                    
                    
                    
                    
                    
                    
                
    
    def draw(self, screen):
        if not self.throwhammer:
            for power_up in self.power_ups:
                power_up.draw(screen)
            
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50, 70)
        self.power_up_shield = False
        self.power_up_hammer = False
        self.throwhammer = False
        
    def generate_power_up(self):
        self.when_appears += random.randint(200, 300)
        self.poweryou = random.randint(0, 1)
        
        if self.poweryou == 0: # 1
            self.power_up_shield = True
            self.power_up_hammer = False
            power_up = Shield()
        elif self.poweryou == 1:
            self.power_up_hammer = True
            self.power_up_shield = False
            power_up = Hammer()
            
            
        self.power_ups.append(power_up)
        
            
    '''def throwR(self, user_input): #
        if user_input[pygame.K_RIGHT]:
            self.throwhammer = True'''
