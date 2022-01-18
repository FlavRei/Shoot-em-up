import pygame
from pygame import *

# Initialisation du mixer
pygame.mixer.init()
son_explosion = pygame.mixer.Sound('msq/explosion.ogg')

class Explosion(pygame.sprite.Sprite):

    def __init__(self, center_vaisseau):
        super(Explosion, self).__init__()
        self._compteur = 15
        self.surf = pygame.image.load('img/explosion.png')
        self.surf = pygame.transform.scale(self.surf, (150, 150))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=center_vaisseau)
        son_explosion.play()

    def update(self):
        self._compteur = self._compteur - 1
        if self._compteur == 0:
            self.kill()
            self._compteur = 15