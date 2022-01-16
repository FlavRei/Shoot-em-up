import pygame

# Création de la police de caractère
pygame.font.init()
police_bouclier = pygame.font.SysFont('Comic Sans MS', 25)

class TextBouclier(pygame.sprite.Sprite):

    def __init__(self, vaisseau):
        super(TextBouclier, self).__init__()
        self.pourcentage = 100
        self.vaisseau = vaisseau
        self._hideText()

    def _setText(self):
        self.surf = police_bouclier.render('Bouclier : '+str(self.pourcentage)+'%', False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(self.vaisseau.rect.x + 30, self.vaisseau.rect.y + 70))

    def _hideText(self):
        self.surf = police_bouclier.render('Bouclier : '+str(self.pourcentage)+'%', False, (0, 0, 0))
        self.rect = self.surf.get_rect(center=(self.vaisseau.rect.x + 30, self.vaisseau.rect.y + 70))

    def update(self):
        if self.vaisseau.bouclier:
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