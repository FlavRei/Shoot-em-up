import pygame
from pygame import *
import random

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class TirInfini(pygame.sprite.Sprite):

    def __init__(self):
        super(TirInfini, self).__init__()
        self.surf = pygame.image.load('img/tir_infini.png')
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 50, random.randint(0, HAUTEUR_ECRAN)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < -10:
            self.kill()


# Création de la police de caractère
pygame.font.init()
police_tir_infini = pygame.font.SysFont('Comic Sans MS', 25)

class TextTirInfini(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super(TextTirInfini, self).__init__()
        self.pourcentage = 100
        self.vaisseau = vaisseau
        self._hideText()

    def _setText(self):
        self.surf = police_tir_infini.render('Tir Infini : '+str(self.pourcentage)+'%', False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(self.vaisseau.rect.x + 30, self.vaisseau.rect.y + 90))

    def _hideText(self):
        self.surf = police_tir_infini.render('Tir Infini : '+str(self.pourcentage)+'%', False, (0, 0, 0))
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN, HAUTEUR_ECRAN))

    def update(self):
        if self.vaisseau.tir_infini:
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


class LogoTirInfini(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super(LogoTirInfini, self).__init__()
        self.vaisseau = vaisseau
        self._hideLogo()

    def _setLogo(self):
        self.surf = pygame.image.load('img/tir_infini.png')
        self.surf = pygame.transform.scale(self.surf, (30, 25))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(285, 15))

    def _hideLogo(self):
        self.surf = pygame.image.load('img/black_tir_infini.png')
        self.surf = pygame.transform.scale(self.surf, (30, 25))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(285, 15))

    def update(self):
        if self.vaisseau.tir_infini:
            self._setLogo()
        else:
            self._hideLogo()