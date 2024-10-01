import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
   def __init__(self, ai_settings, screen):
        super(Ship,self).__init__()
        """Inicializa la nave y establece su posición inicial."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Cargar la imagen de la nave y obtener su rectángulo.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()  # Aquí debe estar definido self.rect

        # Comienza cada nueva nave en la parte inferior central de la pantalla.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Almacena un valor decimal para el centro de la nave.
        self.center = float(self.rect.centerx)


        self.moving_right = False
        self.moving_left = False

   # def update_ship(self):
   #    if self.moving_right and self.rect.right < self.screen_rect.right:
   #    # actualizamos el  movimiento de la nave 
   #      self.center += self.ai_settings.ship_speed_factor   
   #       # self.rect.centerx += 1
   #    if self.moving_left and self.rect.left > 0:
   #       self.center -= self.ai_settings.ship_speed_factor
   #       # self.rect.centerx -= 1
   #    self.rect.centerx = self.center
   def update_ship(self):
      if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
      if self.moving_left and self.rect.left > 0:
        self.center -= self.ai_settings.ship_speed_factor
      self.rect.centerx = self.center
   
   def center_ship(self):
      self.center = self.screen_rect.centerx
   #Blitme tare la nave a la posicion que pide rect 
   def blitme(self):
     self.screen.blit(self.image,self.rect)

# print(type(Ship)) 