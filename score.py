import pygame

LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

# Création de la police de caractère
pygame.font.init()
police_score = pygame.font.SysFont('Comic Sans MS', 40)
police_score_final = pygame.font.SysFont('Comic Sans MS', 60)

class Score(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Score, self).__init__()
        self._scoreCourant = 0
        self._setText()

    def getScore(self):
        return self._scoreCourant

    def _setText(self):
        self.surf = police_score.render('Score : '+str(self._scoreCourant), False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN / 2, 15))

    def showScore(self):
        return police_score_final.render('Score : '+str(self._scoreCourant), False, (255, 255, 255))
    
    def update(self):
        self._setText()

    def incremente(self, valeur):
        self._scoreCourant = self._scoreCourant + valeur