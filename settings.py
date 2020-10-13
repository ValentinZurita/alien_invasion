class Settings:
    """Guarda los ajustes del juego"""

    def __init__(self):
        """Ajustes del juego"""

        # Ajustes de pantalla.
        self.screen_width = 850
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # Ajustes de la nave
        self.ship_limit = 1

        # Ajustes de las balas
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullets_allowed = 3
        self.bullet_color = (60,60,60)
        
        # Ajustes de los alies
        self.fleet_drop_speed = 15
        
        # Velocidad de incrementos
        self.speedup_scale = 1.2

        # Inicia los valores de velocidad.
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Inicializa los valores que cambiar durante el juego"""

        # Ajustes de la nave
        self.ship_speed = .5

        # Ajustes de las balas
        self.bullet_speed = 1

        # Ajustes de los alies
        self.alien_speed = 0.5
        self.fleet_direction = 1 # 1 Derecha, -1 Izquierda


    def increase_speed(self):
        """Incrementa la velocidad del juego"""
        
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale



        


