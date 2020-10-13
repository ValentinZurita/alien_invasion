import pygame.font

class Button():
    """Crea un boton dentro del juego"""

    def __init__(self, ai_game, msg):
        """"Inicializa los valores para el boton"""

        # Obtener la pantalla del juego.
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Tamaño, colores y fuente para el boton.
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Construye el rectangulo para el boton y centra.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Preparar el mensaje del boton
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prepara el mensaje para el boton"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.message_image_rect = self.msg_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        """Dibuja un boton en blanco y despues el mensaje"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.message_image_rect)
        