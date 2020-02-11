#!/usr/bin/python3
# -*- coding: utf-8 -*-

from affichage import *
from saisie import *
from mouvements import *

taille = 4
stat_4 = 20
objectif = 2048

def creer_grille():
	grille = []
	for i in range(taille):
		colonne = []
		for j in range(taille):
			colonne.append(0)
		grille.append(colonne)
	return grille

def loop(grille):
	saisie = None
	while (saisie != '0'):
		afficher_grille(grille, taille)
		saisie = saisie_joueur()
		action_joueur(saisie)
	print("Merci d'avoir joue avec nous !")

def game():
	bienvenue()
	grille = creer_grille()
	loop(grille)

game()