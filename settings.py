class Settings:
    """Guarda los ajustes del juego"""

    def __init__(self):
        """Ajustes del juego"""

        # Ajustes de pantalla.
        self.screen_width = 850
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # Ajustes de la nave
        self.ship_speed = .5
        self.ship_limit = 3

        # Ajustes de las balas
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullets_allowed = 3
        self.bullet_color = (60,60,60)
        
        # Ajustes de los alies
        self.alien_speed = 0.5
        self.fleet_drop_speed = 15
        self.fleet_direction = 1


