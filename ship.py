import pygame

class Ship:
    """Clase que maneja la nave"""

    def __init__(self, ai_game):
        """Iniciar la nave y fijar su posicion de partida"""

        # Se obtiene la pantalla del juego.
        self.screen = ai_game.screen

        # Instancia de la clase Setting para los ajustes del juego
        self.settings = ai_game.settings

        # Se obtiene el rectangulo de la pantalla.
        self.screen_rect = ai_game.screen.get_rect()

        # Cargar la imagen de la nave.
        self.image = pygame.image.load("images/ship.bmp")

        # Se obtiene el rectangulo de la nave.
        self.rect = self.image.get_rect()

        # Iniciar cada nueva nave al centro y fondo de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guardar en un valor decimal la posicion horizontal de la nave
        self.x = float(self.rect.x)

        # Banderas que indican si se mueve la nave
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Actualiza la posicion de la nave en base a la bandera "self.moving_?" """

        # Mueve la nave una posicion a la derecha.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Mueve la nave una posicion a la izquierda.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualizar el rectangulo del objeto de self.x
        self.rect.x = self.x


    def blitme(self):
        """Dibujar la nave en la pantalla"""

        # blit dibuja la nave dentro de la pantalla.
        self.screen.blit(self.image, self.rect)

    
    def center_ship(self):
        """Centra la nave en medio de la pantalla"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


