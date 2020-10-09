class Settings:
    """Guarda los ajustes del juego"""

    def __init__(self):
        """Ajustes del juego"""

        # Ajustes de pantalla.
        self.screen_width = 850
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # Velocidad de la nave
        self.ship_speed = 0.15

        # Ajustes de las balas
        self.bullet_speed = 0.1
        self.bullet_width = 0.3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (60,60,60)
        
        # Ajustes de los alies
        self.alien_speed = 0.1

