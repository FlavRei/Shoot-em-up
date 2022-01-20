import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Ennemi(pygame.sprite.Sprite):

    def __init__(self):
        super(Ennemi, self).__init__()
        self.surf = pygame.image.load('img/ennemi.png')
        self.surf = pygame.transform.scale(self.surf, (80, 40))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 200, random.randint(0, HAUTEUR_ECRAN)))
        self.radius = 20
        self.speed = random.randint(7, 14)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()