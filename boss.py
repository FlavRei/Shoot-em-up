import pygame
from pygame import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Boss(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Boss, self).__init__()
        self.health = 200
        self.max_health = 200
        self.surf = pygame.image.load('img/shark.png')
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 200, 200))
        self.radius = 80
        self.cpt = 1000000
        self.check_pos = False
        self.screen = screen

    def damages(self):
        self.health -= 20
    
    def is_dead(self):
        return self.health <= 0

    def update_health_bar(self):
        pygame.draw.rect(self.screen, (60, 60, 60), [self.rect.left, self.rect.top - 10, self.max_health, 10])
        pygame.draw.rect(self.screen, (200, 0, 0), [self.rect.left, self.rect.top - 10, self.health, 10])

    def update(self):
        self.update_health_bar()
        self.cpt -= 1
        if not self.check_pos:
            if self.cpt % 2 == 0:
                    self.rect.move_ip(-1, 2)
            if self.rect.centery >= HAUTEUR_ECRAN:
                self.check_pos = True
        if self.check_pos:
            if self.cpt % 2 == 0:
                    self.rect.move_ip(-1, -2)
            if self.rect.centery <= 0:
                self.check_pos = False

        if self.cpt <= 0:
            self.cpt = 1000000
        if self.rect.right < -300:
            self.kill()