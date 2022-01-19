import pygame
from pygame import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Boss(pygame.sprite.Sprite):

    def __init__(self):
        super(Boss, self).__init__()
        self.surf = pygame.image.load('img/shark.png')
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 200, 200))
        self.radius = 80
        self.cpt = 1000000
        self.check_pos = False

    def update(self):
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