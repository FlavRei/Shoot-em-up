import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Etoile(pygame.sprite.Sprite):

    def __init__(self):
        super(Etoile, self).__init__()
        self.surf = pygame.image.load('img/etoile.png')
        self.surf = pygame.transform.scale(self.surf, (5, 5))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 20, random.randint(0, HAUTEUR_ECRAN)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < 0:
            self.kill()