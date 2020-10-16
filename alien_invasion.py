import sys
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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

        # Instancia de las estadisticas del juego
        self.stats = GameStats(self)

        # Instancia del Scoreboard
        self.sb = Scoreboard(self)

        # Instancia de la nave del juego.       
        self.ship = Ship(self)

        # Crea un grupo de sprites que almacenara las balas.
        self.bullets = pygame.sprite.Group()

        # Crea un grupo de aliens para crear la flota.
        self.aliens = pygame.sprite.Group()
        self._create_fleet_()

        # Crear el boton "Play"
        self.play_button = Button(self, "Play")

        # Fija color de fondo para la pantalla.
        self.backgroung_color = (self.settings.background_color)


############################################### RUN GAME ########################################################


    def run_game(self):
        """""Inicia el Main Loop"""

        while True:
            # Responde a los eventos de teclado o mouse.
            self._check_events()

            if self.stats.game_active:

                # Actualiza la posicion de la nave cada vuelta de bucle.
                self.ship.update()

                # Actualiza las balas cada vuelta de bucle.
                self._update_bullets()
                
                # Actualiza la posicion de los aliens.
                self._update_aliens()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


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

    
    def _check_play_button(self, mouse_pos):
        """Empieza un nuevo juego cuando el jugador
        presiona el boton "Play" """
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            # Resetear los ajustes del juego.
            self.settings.initialize_dynamic_settings()

            # Resetear las estadisticas del juego.
            self.stats.game_active = True

            # Resetear Score.
            self.stats.score = 0
            self.sb.prep_score()
            self.stats.level = 0
            self.sb.prep_level()
            self.stats.ships_left = self.settings.ship_limit
            self.sb.prep_ships()

            # Quitar todas las balas y aliens.
            self.aliens.empty()
            self.bullets.empty()

            # Crear una nueva flota y centrar la nave.
            self._create_fleet_()
            self.ship.center_ship()

            # Esconder el cursor del mouse.
            pygame.mouse.set_visible(False)
        

############################################### BULLETS ########################################################


    def _fire_bullet(self):
        """Crea una nueva bala y la agrega al grupo de ballas"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Actualizar la posicion de las balas y deshacerse de las viejas siempre ingratas"""

        # Actualizar la posicion de las balas.
        self.bullets.update()

        # Deshacerse de las balas que desparecen de la pantalla.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # Llama al metodo en caso de detectar una colision.
        self._check_bullet_alien_collision()
        

    def _check_bullet_alien_collision(self):
        """Responder a una colision de balas y aliens"""

        # Remover cualquier alien y bala que haya colisionado.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        # Agregar puntaje por cada alien cruelmente asesinado.
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.aliens_point * len(aliens)
            self.sb.prep_score()

        # En caso de tener la lista de alien vacia.
        # Repopular la flota de aliens.
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet_()
            self.settings.increase_speed()

            # Incrementar el nivel.
            self.stats.level += 1
            self.sb.prep_level()


################################################## NAVE ##########################################################


    def _ship_hit(self):
        """Responde cuando una nave es impactada por un alien"""

        # Si el numero de naves es mayor a 0
        # Se restablece el juego 
        if self.stats.ships_left > 0:

            # Reduce el numero de naves restantes
            self.stats.ships_left -= 1

            # Actualiza el numero de naves del Scoreboard.
            self.sb.prep_ships()

            # Se deshace de cualquier alien y bala sobrante
            self.aliens.empty()
            self.bullets.empty()

            # Se crea una nueva flota y se centra la nave
            self._create_fleet_()
            self.ship.center_ship()

            # Pausa 
            sleep(0.8)
        
        # Si el numero de naves es menor a 0
        # El estado del juego pasa a False
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


############################################## ALIEN FLEET #######################################################


    def _create_fleet_(self):
        """Crear la flota de aliens invasores como cerebros"""

        # ***alien por fila*** Crear un alien y encontrar el numero de aliens que entran en una fila.
        # El espacio entre cada alien es igual al ancho de un alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avalible_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avalible_space_x // (2 * alien_width)
        
        # ****alien por columna*** Determina el numero de filas de aliens que entran en la pantalla
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

    
    def _check_fleet_edges(self):
        """Responde apropiadamente cuando algun alien toca el borde de la pantalla"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    

    def _change_fleet_direction(self):
        """Baja la flota de aliens y cambia su direccion"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed # Ajusta la coordenada y
        self.settings.fleet_direction *= -1 #Cambia la direccion

    
    def _check_aliens_bottom(self):
        """Verificar si algun alien ha tocado el fondo de la pantalla"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    
    def _update_aliens(self):
        """Actualizar la posicion de todos los aliens en la flota"""
        
        self._check_fleet_edges() # Verifica si algun alien ha llegado al borde la pantalla
        self.aliens.update() # Llama al metodo update de aline para la coordenada x

        # Buscar colisiones entre los aliens y la nave.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Buscar por aliens que toquen el fondo de la pantalla
        self._check_aliens_bottom()
        

############################################# UPDATE SCREEN ######################################################


    def _update_screen(self):
        """Actualiza la imagen en la pantalla"""

        # Fija el color de fondo para la pantalla.
        self.screen.fill(self.backgroung_color)

        # Dibuja la nave en la pantalla.
        self.ship.blitme()

        # Recorre el grupo de balas y las dibuja
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Dibuja los aliens.
        self.aliens.draw(self.screen)

        # Dibuja el Scoreboard.
        self.sb.show_score()

        # Dibujar el HighScore.
        self.sb.check_high_score()                       

        # Dibujar boton "Play" si el juego esta inactivo.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Hacer visible el ultimo dibujo de pantalla.
        pygame.display.flip()


################################################## MAIN #############################################################


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
