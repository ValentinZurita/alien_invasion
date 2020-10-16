class GameStats():
    """Registra las estadisticas del juego"""

    def __init__(self, ai_game):
        """Inicializa las estadisticas del juego"""

        # El High Score nunca debe ser reseteado.
        self.high_score = 0

        # Instancia de los ajustes de juego
        self.settings = ai_game.settings

        # Reseto de las estadisticas
        self.reset_stats()

        # Iniciar el juego en estado inactivo.
        self.game_active = False
        
    
    def reset_stats(self):
        """Inicializa las estadisticas que pueden cambaiar durante el juego"""

        self.ships_left = self.settings.ship_limit
        self.score = 0 
        self.level = 1
        