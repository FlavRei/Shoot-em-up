import pygame
from pygame import *
from sprites import *
from vaisseau import Vaisseau
from bouclier import Bouclier, TextBouclier
from vitesse import Vitesse, TextVitesse
from tir_infini import TirInfini, TextTirInfini
from explosion import Explosion, ExplosionBouclier
from ennemi import Ennemi
from score import Score
from vie import Vie
from etoile import Etoile
from meteorite import Meteorite
from boss import Boss
from vague import Vague


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

# # Événement création d'un ennemi
AJOUTE_ENNEMI = pygame.USEREVENT + 1
pygame.time.set_timer(AJOUTE_ENNEMI, 750)
# Événement création d'une étoile
AJOUTE_ETOILE = pygame.USEREVENT + 2
pygame.time.set_timer(AJOUTE_ETOILE, 50)
# Événement création d'un bouclier
AJOUTE_BOUCLIER = pygame.USEREVENT + 3
pygame.time.set_timer(AJOUTE_BOUCLIER, 27000)
# Événement création d'un vitesse x2
AJOUTE_VITESSE = pygame.USEREVENT + 4
pygame.time.set_timer(AJOUTE_VITESSE, 45000)
# Événement création d'un tir infini
AJOUTE_TIR_INFINI = pygame.USEREVENT + 5
pygame.time.set_timer(AJOUTE_TIR_INFINI, 64000)
# Événement création d'une météorite
AJOUTE_METEORITE = pygame.USEREVENT + 6
pygame.time.set_timer(AJOUTE_METEORITE, 5000)

# Création de la surface principale
ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])

# Création du vaisseau
vaisseau = Vaisseau()
tous_sprites.add(vaisseau)

coeur_0 = Vie((-15, 15))
coeur_1 = Vie((20, 15))
coeur_2 = Vie((55, 15))
coeur_3 = Vie((90, 15))
coeurs = [coeur_0, coeur_1, coeur_2, coeur_3]
les_vies.add(coeur_1)
les_vies.add(coeur_2)
les_vies.add(coeur_3)
tous_sprites.add(coeur_1)
tous_sprites.add(coeur_2)
tous_sprites.add(coeur_3)

score = Score()
tous_sprites.add(score)

vague = Vague(ecran)


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
    pygame.time.delay(3000)


# Game Loop
cpt_fantome = 100
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
            # Création d'un nouveau tir infini
            elif event.type == AJOUTE_TIR_INFINI:
                nouveau_tir_infini = TirInfini()
                # Ajout du tir infini aux groupes
                les_tirs_infini.add(nouveau_tir_infini)
                tous_sprites.add(nouveau_tir_infini)
            # Création d'une nouvelle météorite
            elif event.type == AJOUTE_METEORITE:
                nouvelle_meteorite = Meteorite()
                # Ajout de la météorite aux groupes
                les_meteorites.add(nouvelle_meteorite)
                tous_sprites.add(nouvelle_meteorite)

            # Gestion des vagues
            if not vague.is_full_loaded():
                # Création d'un nouvel ennemi
                if event.type == AJOUTE_ENNEMI:
                    nouvel_ennemi = Ennemi()
                    # Ajout de l'ennemi aux groupes
                    les_ennemis.add(nouvel_ennemi)
                    tous_sprites.add(nouvel_ennemi)
            else:
                if len(les_boss) == 0:
                    # Création d'une nouveau boss
                    nouveau_boss = Boss(ecran)
                    # Ajout du boss aux groupes
                    les_boss.add(nouveau_boss)
                    tous_sprites.add(nouveau_boss)


        # Remplissage de l'écran en noir
        ecran.fill((0, 0, 0))

        # Détection des collisions Vaisseau / Ennemi - Vaisseau / Météorite - Vaisseau / Boss
        if vaisseau.fantome:
            cpt_fantome -= 1
            vaisseau.surf = pygame.image.load('img/vaisseau_fantome.png')
            vaisseau.surf = pygame.transform.scale(vaisseau.surf, (70, 70))
            vaisseau.surf.convert()
            vaisseau.surf.set_colorkey((255, 255, 255), RLEACCEL)
            if cpt_fantome <= 0:
                vaisseau.surf = pygame.image.load('img/vaisseau.png')
                vaisseau.surf = pygame.transform.scale(vaisseau.surf, (70, 70))
                vaisseau.surf.convert()
                vaisseau.surf.set_colorkey((255, 255, 255), RLEACCEL)
                vaisseau.fantome = False
                cpt_fantome = 100
        else:
            if pygame.sprite.spritecollideany(vaisseau, les_ennemis, pygame.sprite.collide_circle) or pygame.sprite.spritecollideany(vaisseau, les_meteorites, pygame.sprite.collide_circle) or pygame.sprite.spritecollideany(vaisseau, les_boss, pygame.sprite.collide_circle):
                if vaisseau.bouclier:
                    explosion = ExplosionBouclier(vaisseau.rect.center)
                    les_explosions.add(explosion)
                    tous_sprites.add(explosion)
                if not vaisseau.bouclier:
                    explosion = Explosion(vaisseau.rect.center, 150)
                    les_explosions.add(explosion)
                    tous_sprites.add(explosion)
                    coeurs[-1].tuer()
                    coeurs.remove(coeurs[-1])
                    vaisseau.vie -= 1
                    vaisseau.fantome = True
                    if vaisseau.vie < 0:
                        pygame.time.delay(1000)
                        game_over()
                        vaisseau = Vaisseau()
                        tous_sprites.add(vaisseau)
                        coeur_0 = Vie((-15, 15))
                        coeur_1 = Vie((20, 15))
                        coeur_2 = Vie((55, 15))
                        coeur_3 = Vie((90, 15))
                        coeurs = [coeur_0, coeur_1, coeur_2, coeur_3]
                        les_vies.add(coeur_1)
                        les_vies.add(coeur_2)
                        les_vies.add(coeur_3)
                        tous_sprites.add(coeur_1)
                        tous_sprites.add(coeur_2)
                        tous_sprites.add(coeur_3)
                        score = Score()
                        tous_sprites.add(score)
                        accueil = True     
                        if len(les_boss) == 0:
                            vague.reset_percent()

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

        # Détection des collisions Vaisseau / Tir Infini
        for tir in les_tirs_infini:
            liste_tirs_touches = pygame.sprite.spritecollide(vaisseau, les_tirs_infini, False)
            if len(liste_tirs_touches) > 0:
                vaisseau.reset_bonus()
                tir.kill()
                vaisseau.set_tir_infini(True)
                
        # Détection des collisions Missile / Ennemi
        for missile in les_missiles:
            liste_ennemi_touches = pygame.sprite.spritecollide(missile, les_ennemis, True)
            if len(liste_ennemi_touches) > 0:
                missile.kill()
                score.incremente(100)
            for ennemi in liste_ennemi_touches:
                explosion = Explosion(ennemi.rect.center, 150)
                les_explosions.add(explosion)
                tous_sprites.add(explosion)

        # Détection des collisions Missile / Boss
        for missile in les_missiles:
            liste_boss_touches = pygame.sprite.spritecollide(missile, les_boss, False)
            if len(liste_boss_touches) > 0:
                missile.kill()
            for boss in liste_boss_touches:
                explosion = Explosion((missile.rect.right, missile.rect.centery), 100)
                les_explosions.add(explosion)
                tous_sprites.add(explosion)
                boss.damages()
                if boss.is_dead():
                    explosion = Explosion(boss.rect.center, 250)
                    les_explosions.add(explosion)
                    tous_sprites.add(explosion)
                    boss.kill()
                    score.incremente(500)
                    vague.reset_percent()

        # Pile des touches appuyées
        touche_appuyee = pygame.key.get_pressed()

        # Mise à jour des éléments
        vaisseau.update(touche_appuyee) 
        les_missiles.update()
        les_ennemis.update()
        les_explosions.update()
        les_etoiles.update()
        les_boucliers.update()
        les_vitesses.update()
        les_tirs_infini.update()
        score.update()
        les_meteorites.update()
        les_boss.update()  
        vague.update_bar(ecran)

        # Les objets sont recopiés sur la surface écran
        for mon_sprite in tous_sprites:
            ecran.blit(mon_sprite.surf, mon_sprite.rect)

        ecran.blit(vaisseau.surf, vaisseau.rect)

        # Affichage de la surface
        pygame.display.flip()

        clock.tick(60)

pygame.quit()