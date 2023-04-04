import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle): # 2 all
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = self.Y_POS_BIRD
        self.fly_index = 0
            
    def draw(self, screen):
        if self.fly_index > 10:
            self.fly_index = 0
        screen.blit(self.image[0] if self.fly_index < 5 else self.image[1], self.rect)
        self.fly_index += 1