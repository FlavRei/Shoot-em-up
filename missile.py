import pygame
from pygame import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

# Initialisation du mixer
pygame.mixer.init()
son_missile = pygame.mixer.Sound('msq/laser.ogg')

class Missile(pygame.sprite.Sprite):

    def __init__(self, center_missile):
        super(Missile, self).__init__()
        self.surf = pygame.image.load('img/missile.png')
        self.surf = pygame.transform.scale(self.surf, (60, 20))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=center_missile)
        son_missile.play()

    def update(self):
        self.rect.move_ip(15, 0)
        if self.rect.left > LARGEUR_ECRAN:
            self.kill()