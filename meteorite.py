import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Meteorite(pygame.sprite.Sprite):

    def __init__(self):
        super(Meteorite, self).__init__()
        self.surf = pygame.image.load('img/meteorite.png')
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(LARGEUR_ECRAN * 2, LARGEUR_ECRAN * 4), -(random.randint(HAUTEUR_ECRAN * 2, HAUTEUR_ECRAN * 4))))

    def update(self):
        self.rect.move_ip(-8, 8)
        if self.rect.right < -200 or self.rect.bottom > HAUTEUR_ECRAN + 200:
            self.kill()