import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Vitesse(pygame.sprite.Sprite):

    def __init__(self):
        super(Vitesse, self).__init__()
        self.surf = pygame.image.load('img/vitesse.png')
        self.surf = pygame.transform.scale(self.surf, (60, 60))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 50, random.randint(0, HAUTEUR_ECRAN)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < -10:
            self.kill()