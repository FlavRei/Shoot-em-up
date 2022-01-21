import pygame
from pygame import *
from sprites import *
from bouclier import TextBouclier
from vitesse import TextVitesse
from tir_infini import TextTirInfini

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
        self.radius = 35
        self.bouclier = False
        self.text_bouclier = TextBouclier(self)
        tous_sprites.add(self.text_bouclier)
        self.vitesse = 5
        self.text_vitesse = TextVitesse(self)
        tous_sprites.add(self.text_vitesse)
        self.tir_infini = False
        self.text_tir_infini = TextTirInfini(self)
        tous_sprites.add(self.text_tir_infini)
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
            if self.tir_infini:
                if self.cpt % 10 == 0:
                    missile = Missile((self.rect.x, self.rect.y + 55))
                    tous_sprites.add(missile)
                    les_missiles.add(missile)
            else:
                if len(les_missiles.sprites()) < 1: 
                    missile = Missile((self.rect.x, self.rect.y + 55))
                    tous_sprites.add(missile)
                    les_missiles.add(missile)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN

        self.text_bouclier.update()
        self.text_vitesse.update()
        self.text_tir_infini.update()
        self.decremente()

    def set_bouclier(self, bool):
        self.bouclier = bool

    def set_vitesse(self, int):
        self.vitesse = int

    def set_tir_infini(self, bool):
        self.tir_infini = bool

    def reset_bonus(self):
        self.set_bouclier(False)
        self.set_vitesse(5)
        self.set_tir_infini(False)
        self.cpt = 600
        self.text_bouclier.pourcentage = 100
        self.text_vitesse.pourcentage = 100
        self.text_tir_infini.pourcentage = 100


    def decremente(self):
        if self.bouclier or self.vitesse == 10 or self.tir_infini:
            self.cpt -= 1
            if self.cpt <= 0:
                self.set_bouclier(False)
                self.set_vitesse(5)
                self.set_tir_infini(False)
                self.cpt = 600


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