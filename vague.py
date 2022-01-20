import pygame

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

# Création de la police de caractère
pygame.font.init()
police_vitesse = pygame.font.SysFont('Comic Sans MS', 25)

class Vague:

    def __init__(self, screen):
        self.percent = 0
        self.percent_speed = 10

    def add_percent(self):
        self.percent += self.percent_speed / 100
        if self.percent >= 100:
            self.percent = 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, screen):
        self.add_percent()
        pygame.draw.rect(screen, (0, 255, 0), [LARGEUR_ECRAN / 2 + 100, 10, (LARGEUR_ECRAN / 2 - 150) / 100 * self.percent, 10])
        self.percent = round(self.percent, 2)
        self.surf = police_vitesse.render(str(self.percent)+'%', False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN - 25, 15))
        screen.blit(self.surf, self.rect)