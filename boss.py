import pygame
from pygame import *
import random
from sprites import *

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

class Boss(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Boss, self).__init__()
        self.health = 200
        self.max_health = 200
        self.surf = pygame.image.load('img/shark.png')
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN + 200, 200))
        self.radius = 80
        self.cpt = 1000000
        self.check_pos = False
        self.screen = screen

    def damages(self):
        self.health -= 20
    
    def is_dead(self):
        return self.health <= 0

    def update_health_bar(self):
        pygame.draw.rect(self.screen, (60, 60, 60), [self.rect.left, self.rect.top - 10, self.max_health, 10])
        pygame.draw.rect(self.screen, (255, 0, 0), [self.rect.left, self.rect.top - 10, self.health, 10])

    def update(self):
        self.update_health_bar()
        bord = random.randint(100, 200)
        self.cpt -= 1
        if not self.check_pos:
            if self.cpt % 2 == 0:
                    self.rect.move_ip(-1, 2)
            if self.rect.centery >= HAUTEUR_ECRAN - bord:
                self.check_pos = True
        if self.check_pos:
            if self.cpt % 2 == 0:
                    self.rect.move_ip(-1, -2)
            if self.rect.centery <= bord:
                self.check_pos = False

        if self.cpt % 80 == 0:
            attaque = Attaque((self.rect.x + 20, self.rect.y + 160))
            les_meteorites.add(attaque)
            tous_sprites.add(attaque)

        if self.cpt <= 0:
            self.cpt = 1000000
        if self.rect.right < -300:
            self.kill()


class Attaque(pygame.sprite.Sprite):

    def __init__(self, center_missile):
        super(Attaque, self).__init__()
        self.surf = pygame.image.load('img/fish.png')
        self.surf = pygame.transform.scale(self.surf, (80, 40))
        self.surf.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=center_missile)
        self.direction_y = random.randint(-7, 7)
        self.radius = 20
        self.origin_surf = self.surf
        self.angle = 0
        self.speed_rotation = random.randint(5, 25)

    def rotate(self):
        self.angle += self.speed_rotation
        self.surf = pygame.transform.rotozoom(self.origin_surf, self.angle, 1)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def update(self):
        self.rotate()
        self.rect.move_ip(-7, self.direction_y)
        if self.rect.left > LARGEUR_ECRAN:
            self.kill()