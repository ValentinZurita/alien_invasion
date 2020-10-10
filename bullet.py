import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para manejar las balas que dispara la nave"""

    def __init__(self, ai_game):
        """Crear una bala en la posicion actual de la nave"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crear un rectangulo de bala en (0,0) y ponerla en posicion correcta
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guardar la posición de la bala con un valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Mover la bala arriba de la pantalla"""

        # Actualizar la posicion decimal de la nave
        self.y -= self.settings.bullet_speed

        # Actualizar la posicion del rectangulo
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujar la bala en la pantalla"""

        pygame.draw.rect(self.screen, self.color, self.rect)




