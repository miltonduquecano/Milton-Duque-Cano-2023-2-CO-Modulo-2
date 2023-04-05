import pygame
import time

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEAD
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.dinosaur import Dinosour # 3



class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosour()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen, "Press any key to start...")
        self.running = False
        self.score = 0
        self.score_max = 0 # 3
        self.death_count = 0
        self.dead = False # 3

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()

        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def execute(self):
        self.running = True
        # mientras la aplicacion corra
        while self.running:
            # y si no estoy jugando
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_dead()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.screen.blit(DEAD, (half_screen_width - 50, half_screen_height - 140))
            self.menu.update_message(f"Their deaths were {self.death_count}| Its current rating was {self.score}| your best brand {self.score_max}") # 3
            self.menu.draw(self.screen)
        self.menu.update(self)
        
    def update_score(self):
        if self.score >= self.score_max: # 3
            self.score_max = self.score + 1
        self.score += 1
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
            
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score {self.score}| ScoreMAX {self.score_max}| Deaths {self.death_count}', True, (0, 0, 0)) # 3
        text_rect = text.get_rect()
        text_rect.center = (800, 50)
        self.screen.blit(text, text_rect)
        
    def draw_dead(self): # 3
        if self.dead:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render(f'GAME OVER', True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (550, 300)
            self.screen.blit(text, text_rect)
            time.sleep(1)
            
    def reset_game(self): # 3
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.dead = False