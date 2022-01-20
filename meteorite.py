import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Meteorite(pygame.sprite.Sprite):

    def __init__(self):
        super(Meteorite, self).__init__()
        self.surf = pygame.image.load('img/meteorite.png')
        self.surf = pygame.transform.scale(self.surf, (120, 120))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(LARGEUR_ECRAN * 2, LARGEUR_ECRAN * 3), -(random.randint(HAUTEUR_ECRAN * 2, HAUTEUR_ECRAN * 3))))
        self.radius = 50

    def update(self):
        self.rect.move_ip(-8, 8)
        if self.rect.right < -200 or self.rect.bottom > HAUTEUR_ECRAN + 200:
            self.kill()