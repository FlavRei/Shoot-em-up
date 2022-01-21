import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Vitesse(pygame.sprite.Sprite):

    def __init__(self):
        super(Vitesse, self).__init__()
        self.surf = pygame.image.load('img/vitesse.png')
        self.surf = pygame.transform.scale(self.surf, (55, 65))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 50, random.randint(0, HAUTEUR_ECRAN)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < -10:
            self.kill()


# Création de la police de caractère
pygame.font.init()
police_vitesse = pygame.font.SysFont('Comic Sans MS', 25)

class TextVitesse(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super(TextVitesse, self).__init__()
        self.pourcentage = 100
        self.vaisseau = vaisseau
        self._hideText()

    def _setText(self):
        self.surf = police_vitesse.render('Vitesse x2 : '+str(self.pourcentage)+'%', False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(self.vaisseau.rect.x + 30, self.vaisseau.rect.y + 90))

    def _hideText(self):
        self.surf = police_vitesse.render('Vitesse x2 : '+str(self.pourcentage)+'%', False, (0, 0, 0))
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN, HAUTEUR_ECRAN))

    def update(self):
        if self.vaisseau.vitesse == 10:
            self.decremente()
            self._setText()
        else:
            self._hideText()
            self.pourcentage = 100

    def decremente(self):
        self.pourcentage -= 1/6
        self.pourcentage = round(self.pourcentage, 2)
        if self.pourcentage <= 0:
            self.pourcentage = 0.00


class LogoVitesse(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super(LogoVitesse, self).__init__()
        self.vaisseau = vaisseau
        self._hideLogo()

    def _setLogo(self):
        self.surf = pygame.image.load('img/vitesse.png')
        self.surf = pygame.transform.scale(self.surf, (30, 40))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(250, 15))

    def _hideLogo(self):
        self.surf = pygame.image.load('img/black_vitesse.png')
        self.surf = pygame.transform.scale(self.surf, (30, 40))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(250, 15))

    def update(self):
        if self.vaisseau.vitesse == 10:
            self._setLogo()
        else:
            self._hideLogo()