import pygame
from pygame import *
from sprites import *
from textvitesse import TextVitesse
from vaisseau import Vaisseau
from textbouclier import TextBouclier
from bouclier import Bouclier
from textvitesse import TextVitesse
from vitesse import Vitesse
from explosion import Explosion
from ennemi import Ennemi
from score import Score
from etoile import Etoile


LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600


# Réglage de l'horloge
clock = pygame.time.Clock()

# Importer les images et fonts de l'écran d'accueil
background = pygame.image.load('img/galaxy.jpg')
bouton_start = pygame.image.load('img/start.png')
bouton_start = pygame.transform.scale(bouton_start, (150, 150))
start_rect = bouton_start.get_rect()
start_rect.x = LARGEUR_ECRAN / 2.5
start_rect.y = HAUTEUR_ECRAN / 2
my_font = pygame.font.Font("font/title_font.ttf", 80)
title = my_font.render("Shoot'Em Up", 1, (255, 255, 255))

# Initialisation de la librairie
pygame.init()
pygame.display.set_caption("Shoot'em up")

# Événement création d'un ennemi
AJOUTE_ENNEMI = pygame.USEREVENT + 1
pygame.time.set_timer(AJOUTE_ENNEMI, 500)
# Événement création d'une étoile
AJOUTE_ETOILE = pygame.USEREVENT + 2
pygame.time.set_timer(AJOUTE_ETOILE, 50)
# Événement création d'un bouclier
AJOUTE_BOUCLIER = pygame.USEREVENT + 3
pygame.time.set_timer(AJOUTE_BOUCLIER, 27000)
# Événement création d'un vitesse x2
AJOUTE_VITESSE = pygame.USEREVENT + 4
pygame.time.set_timer(AJOUTE_VITESSE, 45000)

# Création de la surface principale
ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])

# Création du vaisseau
vaisseau = Vaisseau()
tous_sprites.add(vaisseau)
text_bouclier = TextBouclier(vaisseau)
vaisseau.set_text_bouclier(text_bouclier)
tous_sprites.add(text_bouclier)
text_vitesse = TextVitesse(vaisseau)
vaisseau.set_text_vitesse(text_vitesse)
tous_sprites.add(text_vitesse)
score = Score()
tous_sprites.add(score)

def game_over():
    over = my_font.render("Game Over", 1, (255, 255, 255))
    text_score = score.showScore()
    pos_score = text_score.get_rect()
    pos_score.x = LARGEUR_ECRAN / 2 - text_score.get_width() / 2
    pos_score.y = HAUTEUR_ECRAN / 2 - text_score.get_height() / 2 + 50
    ecran.blit(over, (LARGEUR_ECRAN / 6.5, HAUTEUR_ECRAN / 3.5))
    ecran.blit(text_score, pos_score)
    pygame.display.flip()
    for sprite in tous_sprites:
        sprite.kill()


# Game Loop
accueil = True
continuer = True
while continuer:

    # Écran d'accueil
    if accueil:
        # Appliquer le background
        ecran.blit(background, (0, -100))
        ecran.blit(bouton_start, start_rect)
        ecran.blit(title, (LARGEUR_ECRAN / 8, HAUTEUR_ECRAN / 3.5))

        # Affichage de la surface
        pygame.display.flip()

        for event in pygame.event.get():
            # Utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
            # Utilisateur clique sur Start
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    accueil = False
            # Utilisateur appuie sur espace
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    accueil = False

    # Jeu
    else:
        for event in pygame.event.get():
            # Utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                continuer = False
            # Création d'un nouvel ennemi
            elif event.type == AJOUTE_ENNEMI:
                nouvel_ennemi = Ennemi()
                # Ajout de l'ennemi aux groupes
                les_ennemis.add(nouvel_ennemi)
                tous_sprites.add(nouvel_ennemi)
            # Création d'une nouvelle étoile
            elif event.type == AJOUTE_ETOILE:
                nouvelle_etoile = Etoile()
                # Ajout de l'ennemi aux groupes
                les_etoiles.add(nouvelle_etoile)
                tous_sprites.add(nouvelle_etoile)
            # Création d'un nouveau bouclier
            elif event.type == AJOUTE_BOUCLIER:
                nouveau_bouclier = Bouclier()
                # Ajout du bouclier aux groupes
                les_boucliers.add(nouveau_bouclier)
                tous_sprites.add(nouveau_bouclier)
            # Création d'un nouveau vitesse
            elif event.type == AJOUTE_VITESSE:
                nouveau_vitesse = Vitesse()
                # Ajout du bouclier aux groupes
                les_vitesses.add(nouveau_vitesse)
                tous_sprites.add(nouveau_vitesse)

        # Remplissage de l'écran en noir
        ecran.fill((0, 0, 0))

        # Détection des collisions Vaisseau / Ennemi
        if pygame.sprite.spritecollideany(vaisseau, les_ennemis):
            if not vaisseau.bouclier:
                vaisseau.kill()
            explosion = Explosion(vaisseau.rect.center)
            les_explosions.add(explosion)
            tous_sprites.add(explosion)
            if not vaisseau.bouclier:
                game_over()
                pygame.time.delay(3000)
                vaisseau = Vaisseau()
                tous_sprites.add(vaisseau)
                text_bouclier = TextBouclier(vaisseau)
                vaisseau.set_text_bouclier(text_bouclier)
                tous_sprites.add(text_bouclier)
                text_vitesse = TextVitesse(vaisseau)
                vaisseau.set_text_vitesse(text_vitesse)
                tous_sprites.add(text_vitesse)
                score = Score()
                tous_sprites.add(score)
                accueil = True

        # Détection des collisions Vaisseau / Bouclier
        for bouclier in les_boucliers:
            liste_boucliers_touches = pygame.sprite.spritecollide(vaisseau, les_boucliers, False)
            if len(liste_boucliers_touches) > 0:
                vaisseau.reset_bonus()
                bouclier.kill()
                vaisseau.set_bouclier(True)

        # Détection des collisions Vaisseau / Vitesse x2
        for vitesse in les_vitesses:
            liste_vitesses_touches = pygame.sprite.spritecollide(vaisseau, les_vitesses, False)
            if len(liste_vitesses_touches) > 0:
                vaisseau.reset_bonus()
                vitesse.kill()
                vaisseau.set_vitesse(10)
                
        # Détection des collisions Missile / Ennemi
        for missile in le_missile:
            liste_ennemi_touches = pygame.sprite.spritecollide(missile, les_ennemis, True)
            if len(liste_ennemi_touches) > 0:
                missile.kill()
                score.incremente(len(liste_ennemi_touches)*100)
            for ennemi in liste_ennemi_touches:
                explosion = Explosion(ennemi.rect.center)
                les_explosions.add(explosion)
                tous_sprites.add(explosion)

        # Pile des touches appuyées
        touche_appuyee = pygame.key.get_pressed()

        # Mise à jour des éléments
        vaisseau.update(touche_appuyee)
        text_bouclier.update()
        text_vitesse.update()
        le_missile.update()
        les_ennemis.update()
        les_explosions.update()
        les_etoiles.update()
        les_boucliers.update()
        les_vitesses.update()
        score.update()

        # Les objets sont recopiés sur la surface écran
        for mon_sprite in tous_sprites:
            ecran.blit(mon_sprite.surf, mon_sprite.rect)

        ecran.blit(vaisseau.surf, vaisseau.rect)

        # Affichage de la surface
        pygame.display.flip()

        clock.tick(60)

pygame.quit()