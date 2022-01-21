import pygame
from pygame import *

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