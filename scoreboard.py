import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard: 
    """"Reporta la informacion del Score"""

    def __init__(self, ai_game):
        """Inicializa los atributos del seguimientos de score"""

        self.ai_game = ai_game

        # Ajustes iniciales.
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Ajustes de fuente para el score
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparar la imagen incial del Score.
        self.prep_score()
        self.prep_hig_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """Renderiza el Score"""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, 
            self.settings.background_color)

        # Desplegar el Score en la parte superior derecha.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.screen_rect.top
        self.score_rect.right = self.screen_rect.right - 20

    
    def prep_level(self):
        """Renderizar el nivel"""

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.background_color)

        # Desplegar el nivel en la parte inferior del score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5


    def prep_hig_score(self):
        """Renderiza el High Score"""

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
            self.settings.background_color)
        
        # Centrar el High Score en el tope de la pantalla.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    
    def check_high_score(self):
        """Verificar el High Score"""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_hig_score()
            self.prep_level()


    def prep_ships(self):
        """Renderiza el numero de naves faltantes"""

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 20 + ship_number * ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)


    def show_score(self):
        """Dibuja el score en la pantalla"""

        # Dibuja el socore,
        self.screen.blit(self.score_image, self.score_rect)

        # Dibuja el highscore.
        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Dibuja el nivel.
        self.screen.blit(self.level_image, self.level_rect)

        # Dibuja las naves (vidas).
        self.ships.draw(self.screen)
