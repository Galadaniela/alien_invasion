import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  def __init__(self,ai_settings,screen,ship):
    # creamos el objeto de bala en la posición actual de la neve 
      super(Bullet,self).__init__()
      self.screen = screen

    # creamos en rectangula de la bala a (0,0) y ponemos las posición correcta
      self.rect = pygame.Rect(0,0,  ai_settings.bullet_width ,ai_settings.bullet_height)
      self.rect.centerx = ship.rect.centerx
      self.rect.top    =  ship.rect.top

    # Guardamos la posicon de la bala en valor decimal
      self.y = float(self.rect.y)

      self.color = ai_settings.bullet_color
      self.speed = ai_settings.bullet_speed

  def update(self):
      # actualizamos la posicion decimal de la bala 
      self.y -= self.speed
      # actualizamos la posicopn de rect
      self.rect.y = self.y

  def draw_bullet(self):
     pygame.draw.rect(self.screen,self.color,self.rect)
