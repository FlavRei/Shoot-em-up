import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Vie(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Vie, self).__init__()
        self._compteur = 15
        self.surf = pygame.image.load('img/vie.png')
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)

    def tuer(self):
        self.rect.move_ip(0, -30)

class BonusVie(pygame.sprite.Sprite):

    def __init__(self):
        super(BonusVie, self).__init__()
        self.surf = pygame.image.load('img/vie_bonus.png')
        self.surf = pygame.transform.scale(self.surf, (50, 45))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 50, random.randint(0, HAUTEUR_ECRAN)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < -10:
            self.kill()