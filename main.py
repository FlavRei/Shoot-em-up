import pygame
from pygame import *
import sqlite3
from sprites import *
from vaisseau import Vaisseau
from bouclier import Bouclier, LogoBouclier
from vitesse import Vitesse, LogoVitesse
from tir_infini import TirInfini, LogoTirInfini
from explosion import Explosion, ExplosionBouclier
from ennemi import Ennemi
from score import Score
from vie import BonusVie, Vie
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
start_font = pygame.font.SysFont('Comic Sans MS', 40)
start = start_font.render("START", 1, (0, 0, 40))
highscores_font = pygame.font.SysFont('Comic Sans MS', 40)
highscores = highscores_font.render("HIGHSCORES", 1, (0, 0, 40))
title_font = pygame.font.Font("font/title_font.ttf", 80)
title = title_font.render("Shoot'Em Up", 1, (255, 255, 255))

# Importer les images et fonts de l'écran de game over
bouton_continue = pygame.image.load('img/continue.png')
bouton_continue = pygame.transform.scale(bouton_continue, (100, 100))
continue_rect = bouton_continue.get_rect()
continue_rect.x = LARGEUR_ECRAN / 2 - 50
continue_rect.y = HAUTEUR_ECRAN / 1.3
username_font = pygame.font.Font("font/title_font.ttf", 30)
username = username_font.render("Enter Your Name :", 1, (255, 255, 255))
input_font = pygame.font.Font("font/title_font.ttf", 30)
input = ""
game_over_font = pygame.font.Font("font/title_font.ttf", 60)
over = game_over_font.render("Game Over", 1, (255, 255, 255))

# Importer les fonts de l'écran des meilleurs scores
bouton_retour = pygame.image.load('img/back.png')
bouton_retour = pygame.transform.scale(bouton_retour, (70, 70))
retour_rect = bouton_retour.get_rect()
retour_rect.x = 25
retour_rect.y = 15
classement_font = pygame.font.Font("font/title_font.ttf", 60)
classement = classement_font.render("Highscores", 1, (255, 255, 255))
ligne_font = pygame.font.SysFont('Comic Sans MS', 60)


# Initialisation de la librairie
pygame.init()
pygame.display.set_caption("Shoot'em up")

# # Événement création d'un ennemi
AJOUTE_ENNEMI = pygame.USEREVENT + 1
pygame.time.set_timer(AJOUTE_ENNEMI, 750)
# Événement création d'une étoile
AJOUTE_ETOILE = pygame.USEREVENT + 2
pygame.time.set_timer(AJOUTE_ETOILE, 50)
# Événement création d'un bonus bouclier
AJOUTE_BOUCLIER = pygame.USEREVENT + 3
pygame.time.set_timer(AJOUTE_BOUCLIER, 27000)
# Événement création d'un bonus vitesse x2
AJOUTE_VITESSE = pygame.USEREVENT + 4
pygame.time.set_timer(AJOUTE_VITESSE, 45000)
# Événement création d'un bonus tir infini
AJOUTE_TIR_INFINI = pygame.USEREVENT + 5
pygame.time.set_timer(AJOUTE_TIR_INFINI, 64000)
# Événement création d'un bonus vie
AJOUTE_VIE = pygame.USEREVENT + 6
pygame.time.set_timer(AJOUTE_VIE, 100000)
# Événement création d'une météorite
AJOUTE_METEORITE = pygame.USEREVENT + 7
pygame.time.set_timer(AJOUTE_METEORITE, 5000)

# Création de la surface principale
ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])

# Création du vaisseau
vaisseau = Vaisseau()
tous_sprites.add(vaisseau)

logo_bouclier = LogoBouclier(vaisseau)
logo_vitesse = LogoVitesse(vaisseau)
logo_tir_infini = LogoTirInfini(vaisseau)
les_logos.add(logo_bouclier)
les_logos.add(logo_vitesse)
les_logos.add(logo_tir_infini)
tous_sprites.add(logo_bouclier)
tous_sprites.add(logo_vitesse)
tous_sprites.add(logo_tir_infini)

score = Score()
tous_sprites.add(score)

vague = Vague(ecran)

# Connection à la base de données
connection = sqlite3.connect("scoreboard.db")

# Game Loop
cpt_fantome = 100
accueil = True
scores = False
game_over = False
game_on = False
continuer = True
while continuer:

    # Écran d'accueil
    if accueil:
        game_over = False
        # Appliquer le background
        ecran.blit(background, (0, -150))
        start_rect = pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(290, 290, 220, 70), 0, 20)
        highscores_rect = pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(290, 380, 220, 70), 0, 20)
        ecran.blit(start, (start_rect.x + 65, start_rect.y + 24))
        ecran.blit(highscores, (highscores_rect.x + 18, highscores_rect.y + 24))
        ecran.blit(title, (LARGEUR_ECRAN / 8, HAUTEUR_ECRAN / 5))

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
                    game_on = True
                if highscores_rect.collidepoint(event.pos):
                    accueil = False
                    scores = True
            # Utilisateur appuie sur espace ou entrer
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    pygame.quit()
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    accueil = False
                    game_on = True
                if event.key == pygame.K_TAB:
                    accueil = False
                    scores = True

    # Écran des Meilleurs Scores
    if scores:
        # Appliquer le background
        ecran.fill((0, 0, 0))
        ecran.blit(bouton_retour, retour_rect)
        ecran.blit(classement, (LARGEUR_ECRAN / 4, HAUTEUR_ECRAN / 10))

        # Récupération des données
        cursor = connection.cursor()
        cursor.execute('SELECT username, score FROM scoreboard order by score DESC')
        request = cursor.fetchall()
        longueur = min(len(request), 5)
        for i in range(longueur):
            ligne_name = ligne_font.render(request[i][0], 1, (255, 255, 255))
            ligne_score = ligne_font.render(str(request[i][1]), 1, (255, 255, 255))
            ecran.blit(ligne_name, (LARGEUR_ECRAN / 4, HAUTEUR_ECRAN / 3 + 60*i))
            ecran.blit(ligne_score, (LARGEUR_ECRAN / 1.7, HAUTEUR_ECRAN / 3 + 60*i))

        # Affichage de la surface
        pygame.display.flip()

        for event in pygame.event.get():
            # Utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
            # Utilisateur clique sur le bouton retour
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_rect.collidepoint(event.pos):
                    accueil = True
                    scores = False
            # Utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    pygame.quit()
                if event.key == pygame.K_BACKSPACE:
                    accueil = True
                    scores = False

    # Écran Game Over
    if game_over:
        # Gestion de l'input de l'username
        input_surface = input_font.render(input, 1, (0, 255, 255))

        # Appliquer le background
        ecran.fill((0, 0, 0))
        text_score = score.showScore()
        pos_score = text_score.get_rect()
        pos_score.x = LARGEUR_ECRAN / 2.1 - text_score.get_width() / 2
        pos_score.y = HAUTEUR_ECRAN / 3.7 - text_score.get_height() / 2 + 50
        ecran.blit(text_score, pos_score)
        ecran.blit(bouton_continue, continue_rect)
        ecran.blit(username, (LARGEUR_ECRAN / 11, HAUTEUR_ECRAN / 2))
        ecran.blit(input_surface, (LARGEUR_ECRAN / 1.92, HAUTEUR_ECRAN / 2))
        ecran.blit(over, (LARGEUR_ECRAN / 4, HAUTEUR_ECRAN / 9))

        # Affichage de la surface
        pygame.display.flip()

        for event in pygame.event.get():
            # Utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()
            # Utilisateur clique sur Continuer
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    # Insertion en base de données
                    cursor = connection.cursor()
                    new_score = (cursor.lastrowid, input, score.getScore())
                    cursor.execute('INSERT INTO scoreboard VALUES(?, ?, ?)', new_score)
                    connection.commit()
                    accueil = True
                    # Réinitialisation du jeu
                    input = ""
                    vaisseau = Vaisseau()
                    tous_sprites.add(vaisseau)
                    logo_bouclier = LogoBouclier(vaisseau)
                    logo_vitesse = LogoVitesse(vaisseau)
                    logo_tir_infini = LogoTirInfini(vaisseau)
                    les_logos.add(logo_bouclier)
                    les_logos.add(logo_vitesse)
                    les_logos.add(logo_tir_infini)
                    tous_sprites.add(logo_bouclier)
                    tous_sprites.add(logo_vitesse)
                    tous_sprites.add(logo_tir_infini)
                    score = Score()
                    tous_sprites.add(score)
                    if len(les_boss) == 0:
                        vague.reset_percent()
            # Utilisateur tape sur le clavier
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    pygame.quit()
                # Utilisateur appuie sur entrer
                if event.key == pygame.K_RETURN:
                    # Insertion en base de données
                    cursor = connection.cursor()
                    new_score = (cursor.lastrowid, input, score.getScore())
                    cursor.execute('INSERT INTO scoreboard VALUES(?, ?, ?)', new_score)
                    connection.commit()
                    accueil = True
                    # Réinitialisation du jeu
                    input = ""
                    vaisseau = Vaisseau()
                    tous_sprites.add(vaisseau)
                    logo_bouclier = LogoBouclier(vaisseau)
                    logo_vitesse = LogoVitesse(vaisseau)
                    logo_tir_infini = LogoTirInfini(vaisseau)
                    les_logos.add(logo_bouclier)
                    les_logos.add(logo_vitesse)
                    les_logos.add(logo_tir_infini)
                    tous_sprites.add(logo_bouclier)
                    tous_sprites.add(logo_vitesse)
                    tous_sprites.add(logo_tir_infini)
                    score = Score()
                    tous_sprites.add(score)
                    if len(les_boss) == 0:
                        vague.reset_percent()
                # Utilisateur appuie sur retour
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                else:
                    input += event.unicode


    # Jeu
    if game_on:
        for event in pygame.event.get():
            # Utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    pygame.quit()

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
            # Création d'une nouvelle vie
            elif event.type == AJOUTE_VIE:
                nouvelle_vie = BonusVie()
                # Ajout de la vie aux groupes
                les_bonus_vie.add(nouvelle_vie)
                tous_sprites.add(nouvelle_vie)
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
            vaisseau.set_mode_fantome(True)
            if cpt_fantome <= 0:
                vaisseau.set_mode_fantome(False)
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
                    vaisseau.coeurs[-1].tuer()
                    vaisseau.coeurs.remove(vaisseau.coeurs[-1])
                    vaisseau.vie -= 1
                    vaisseau.fantome = True
                    if vaisseau.vie == 0:
                        pygame.time.delay(1000)
                        for sprite in tous_sprites:
                            sprite.kill()
                        game_over = True
                        game_on = False

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

        # Détection des collisions Vaisseau / Vie
        for vie in les_bonus_vie:
            liste_vies_touches = pygame.sprite.spritecollide(vaisseau, les_bonus_vie, False)
            if len(liste_vies_touches) > 0:
                vie.kill()
                vaisseau.add_vie()
                
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
        les_etoiles.update()
        vaisseau.update(touche_appuyee) 
        les_missiles.update()
        les_ennemis.update()
        les_meteorites.update()
        les_boss.update() 

        les_explosions.update()
        
        les_boucliers.update()
        les_vitesses.update()
        les_tirs_infini.update()
        les_bonus_vie.update()

        score.update()
        vague.update_bar(ecran)
         
        les_logos.update()

        # Les objets sont recopiés sur la surface écran
        for mon_sprite in tous_sprites:
            ecran.blit(mon_sprite.surf, mon_sprite.rect)

        ecran.blit(vaisseau.surf, vaisseau.rect)

        # Affichage de la surface
        pygame.display.flip()

        clock.tick(60)

connection.close()
pygame.quit()
