import pygame
from pygame import *
from sprites import *
from missile import Missile

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Vaisseau(pygame.sprite.Sprite):

    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.image.load('img/vaisseau.png')
        self.surf = pygame.transform.scale(self.surf, (70, 70))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(100, (HAUTEUR_ECRAN / 2)))
        self.bouclier = False
        self.vitesse = 5
        self.cpt = 600

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.vitesse)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.vitesse)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.vitesse, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.vitesse, 0)
        if pressed_keys[K_SPACE]:
            if len(le_missile.sprites()) < 1: 
                missile = Missile((self.rect.x, self.rect.y + 55))
                tous_sprites.add(missile)
                le_missile.add(missile)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN

        if self.bouclier or self.vitesse == 10:
            self.decremente()

    def set_bouclier(self):
        self.bouclier = True

    def set_vitesse(self):
        self.vitesse += 5

    def decremente(self):
        self.cpt -= 1
        if self.cpt <= 0:
            self.bouclier = False
            self.vitesse = 5
            self.cpt = 600