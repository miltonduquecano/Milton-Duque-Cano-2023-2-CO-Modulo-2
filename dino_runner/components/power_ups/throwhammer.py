from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class ThrowHammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.rect.x = 80
            
    def draw(self, screen):
        screen.blit(HAMMER, (self.rect.x, 310))
        
    def update(self, game_speed, power_ups):
        self.rect.x += game_speed
        if self.rect.x < +self.rect.width:
            power_ups.pop()