import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """""Clase para manejar los assets del juego y su comportamiento"""


    def __init__(self):
        """""Inicia el juego y crea los recursos"""

        # Inicia pygame.
        pygame.init()

        # Incia Settings de la clase settings
        self.settings = Settings()

        # Inicia pantalla del juego.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_height = self.screen.get_rect().height
        #self.settings.screen_width = self.screen.get_rect().width

        # Pone el nombre en la barra de titulos.
        pygame.display.set_caption("Alien Invasion")

        # Instancia de la nave del juego.
        self.ship = Ship(self)

        # Crea un grupo de sprites que almacenara las balas.
        self.bullets = pygame.sprite.Group()

        # Crea un grupo de aliens para crear la flota.
        self.aliens = pygame.sprite.Group()
        self._create_fleet_()

        # Fija color de fondo para la pantalla.
        self.backgroung_color = (self.settings.background_color)


############################################### RUN GAME ########################################################


    def run_game(self):
        """""Inicia el Main Loop"""

        while True:
            # Responde a los eventos de teclado o mouse.
            self._check_events()

            # Actualiza la posicion de la nave cada vuelta de bucle.
            self.ship.update()

            # Actualiza las balas cada vuelta de bucle.
            self._update_bullets()

            # Cada vuelta de bucle pinta la pantalla.
            self._update_screen()


############################################### EVENTOS ########################################################


    def _check_events(self):
        """"Responde a enventos de teclado o mouse"""

        # Salir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                sys.exit()

            # Tecla presionada.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


            # Tecla liberada.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Responde cuando se presiona una tecla"""

        if event.key == pygame.K_RIGHT:  # Movimiento a la derecha
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Movimiento a la izquierda
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE: # Dispara la bala
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Responde cuando se libera una tecla"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


############################################### BULLETS ########################################################


    def _fire_bullet(self):
        """Crea una nueva bala y la agrega al grupo de ballas"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Actualizar la posicion de las balas y deshacerse de las viejas siempre ingratas"""

        # Actualizar la posicion de las balas
        self.bullets.update()

        # Deshacerse de las balas que desparecen de la pantalla
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


############################################## ALIEN FLEET #######################################################


    def _create_fleet_(self):
        """Crear la flota de aliens invasores como cerebros"""

        # Crear un alien y encontrar el numero de aliens que entran en una fila.
        # El espacio entre cada alien es igual al ancho de un alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avalible_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avalible_space_x // (2 * alien_width)
        
        # Determina el numero de filas de aliens que entran en la pantalla
        ship_height = self.ship.rect.height
        avalible_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        numbers_rows = avalible_space_y // (2 * alien_height)

        # Crear la flota llena de aliens.
        for row_number in range(numbers_rows):            
            for alien_number in range(number_aliens_x):
                #Invoca al metodo create_alien()
                self._create_alien(alien_number, row_number)
            
            
    def _create_alien(self, alien_number, row_number):
        """Crea un solo alien"""
        
        # Crear un alien y colocarlo en la fila
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        

############################################# UPDATE SCREEN ######################################################


    def _update_screen(self):
        """Actualiza la imagen en la pantalla"""

        # Fija el color de fondo para la pantalla.
        self.screen.fill(self.backgroung_color)

        # Dibuja la nave en la pantalla.
        self.ship.blitme()

        # Recorre el grupo de balas y la dibuja
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Dibuja los aliens.
        self.aliens.draw(self.screen)

        # Hacer visible el ultimo dibujo de pantalla.
        pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
