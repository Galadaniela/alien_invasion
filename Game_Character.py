import pygame

class Character():
  def __init__(self,screen):
      self.screen = screen
      self.image = pygame.image.load('images/character1.bmp')
      

      self.rect  = self.image.get_rect()
      self.screen_rect = screen.get_rect()

      self.rect.centerx = self.screen_rect.centerx
  def blitme(self):
     self.screen.blit(self.image,self.rect)