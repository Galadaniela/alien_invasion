import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        # Inicializa el alien y define su posición inicial.
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Carga la imagen del alien y obtiene su rectángulo.
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nuevo alien cerca de la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacena la posición exacta del alien.
        self.x = float(self.rect.x)

    def blitme(self):
        # Dibuja al alien en su posición actual.
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Mueve al alien a la derecha o a la izquierda.
        self.x += (self.ai_settings.alien_speed *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # Devuelve True si el alien está en el borde de la pantalla.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
