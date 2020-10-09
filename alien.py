import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase que reprenta un alien dentro de la flota"""

    def __init__(self, ai_game):
        """Iniciar el alien y su posicion en la flota"""

        super().__init__()
        self.screen = ai_game.screen
        
        # Cargar los ajustes
        self.settings = self.ai_game.settings

        # Cargar la imagen del alien y fijar su rectangulo.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Iniciar cada nuevo alien en la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guardar la posicion horizontal del aline
        self.x = float(self.rect.x)
        
        
    def update(self):
        """Mover el alien a la derecha"""
        
        self.x += self.settings.alien_speed
        self.rect.x = self.x
        

