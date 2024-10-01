import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
from ship import Ship

def get_number_rows(ai_settings,ship_height, alien_height):
      availible_spaces_y = (ai_settings.screen_height - (3*alien_height)- ship_height)
      num_rows  = int(availible_spaces_y / (2* alien_height))
      return num_rows

def get_number_aliens_x(ai_settings, alien_width):
       available_space_x = ai_settings.screen_width - 2 * alien_width
       number_aliens_x = int(available_space_x / (2 * alien_width))
       return number_aliens_x
 
def create_alien(ai_settings, screen, aliens, alien_number , num_rows):
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number
     alien.rect.x = alien.x
     alien.rect.y = alien.rect.height + 2 * alien.rect.height * num_rows
     aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # Crea un alien temporal para calcular el número de aliens por fila y por columna.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    num_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Crear la flota completa de aliens.
    for row_number in range(num_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings,aliens):
     for alien in aliens.sprites():
          if alien.check_edges():
               change_fleet_direction(ai_settings,aliens)
               break
          
def  change_fleet_direction(ai_settings,aliens):
     for alien in aliens.sprites():
         alien.rect.y += ai_settings.fleet_drop_speed
     ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullet):
   
   if stats.ship_left > 0:

     stats.ship_left -= 1
     sb.prep_ship()
     aliens.empty()
     bullet.empty()

     create_fleet(ai_settings, screen, ship, aliens)
     ship.center_ship()

     sleep(0.5)
   else:
      stats.game_active = False
      pygame.mouse.set_visible(True)



def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
          ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
          break
        
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
     check_fleet_edges(ai_settings,aliens)
     aliens.update()    
     if pygame.sprite.spritecollideany(ship,aliens):
          ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
     check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
def check_keydown(event, ai_settings, screen, ship, bullet):
      if  event.key == pygame.K_q:
           sys.exit()
      if event.key == pygame.K_RIGHT:
          ship.moving_right = True
      if event.key == pygame.K_LEFT:
         ship.moving_left = True
      elif event.key == pygame.K_SPACE:
         fire_bullet(ai_settings, screen, ship, bullet)


def fire_bullet(ai_settings, screen, ship, bullet):
    if len(bullet) < ai_settings.bullet_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullet.add(new_bullet)

def check_keyup(event,ship):
      if event.key == pygame.K_RIGHT:
          ship.moving_right = False
      if event.key == pygame.K_LEFT:
         ship.moving_left = False

def check_event(ai_settings, screen, stats, sb, play_button, ship, aliens, bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullet)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullet, mouse_x, mouse_y)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullet, mouse_x, mouse_y):
         
         button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
         if button_clicked and not stats.game_active:
           
           ai_settings.initialize_dynamic_settings()

           pygame.mouse.set_visible(False)

           stats.reset_stats()
           stats.game_active = True
           

           sb.prep_score()
           sb.prep_high_score()
           sb.prep_level()
           sb.prep_ship()
           
           
           aliens.empty()
           bullet.empty()

           create_fleet(ai_settings, screen, ship, aliens)
           ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullet, play_button):
    # Actualiza la pantalla en cada ciclo del juego.
    screen.fill(ai_settings.color)  
    
    # Dibuja las balas
    for bullets in bullet.sprites():
        bullets.draw_bullet()
    
    # Dibuja la nave
    ship.blitme()

    # Dibuja los alienígenas
    aliens.draw(screen)
    sb.show_score()

    # Si el juego no está activo, muestra el botón de 'Play'
    if not stats.game_active:
        play_button.draw_button()

    # Actualiza la pantalla
    pygame.display.flip()

            
def bullet_allowed(ai_settings, screen, stats, sb, ship,aliens, bullet):
      
      bullet.update()
        # Eliminar las bales que desaparecen 
        
      for bullets in bullet.copy():
         if bullets.rect.bottom <= 0:
             bullet.remove(bullets)
      check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,aliens, bullet)


def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
      for aliens in collisions.values():
        stats.score += ai_settings.aliens_points * len(aliens)
        sb.prep_score()

    # Si todos los aliens han sido eliminados, se crea una nueva flota
    if len(aliens) == 0:
        ai_settings.increase_speed()
        bullets.empty()  
        
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


   
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
      stats.high_score = stats.score
      sb.prep_high_score()