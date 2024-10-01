# Ya no necesitamos importar sys por que ya esta importdao en game_fcuntion
# import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats  import GameStats
from scoreboard import Scoreboard
from Game_Character import Character
import game_function as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    character = Character(screen) 
    play_button = Button(ai_settings, screen, "Play")
    bullet = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("Alien Invasion")
    
    gf.create_fleet(ai_settings, screen, ship, aliens)  
      

    while True:
        gf.check_event(ai_settings, screen, stats, sb, play_button, ship,aliens, bullet)

        if stats.game_active:          
         ship.update_ship()
         gf.bullet_allowed(ai_settings, screen, stats, sb, ship,aliens,bullet)
         gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullet)
         
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullet, play_button)
        
        pygame.display.flip() 
run_game()