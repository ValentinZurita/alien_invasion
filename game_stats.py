class GameStats():
    """Registra las estadisticas del juego"""

    def __init__(self, ai_game):
        """Inicializa las estadisticas del juego"""

        # Instancia de los ajustes de juego
        self.settings = ai_game.settings

        # Reseto de las estadisticas
        self.reset_stats()
        
    
    def reset_stats(self):
        """Inicializa las estadisticas que pueden cambaiar durante el juego"""

        self.ships_left = self.settings.ship_limit
