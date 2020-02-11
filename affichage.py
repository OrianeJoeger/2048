def bienvenue():
	print("\nBIENVENUE AU 2048\n")
	print("Touches :")
	print("\tz --> haut")
	print("\tq --> gauche")
	print("\ts --> bas")
	print("\td --> droite")
	print("\t0 --> arreter la partie")

def afficher_separateur(taille):
	separator = '+'
	for i in range(taille):
		separator += str('-').rjust(taille + 2, '-')
		separator += '+'
	print(separator)

def afficher_ligne_vide(taille):
	affichage = ''
	for i in range(taille):
		affichage += '|'
		affichage += str('').rjust(taille + 2, ' ')
	print(affichage + '|')

def afficher_ligne_rempli(taille, ligne):
	display = ''
	for cell in ligne:
		display += '| '
		if cell > 0:
			display += str(cell).rjust(taille, ' ')
		else:
			display += str('').rjust(taille, ' ')
		display += ' '
	print(display + '|')

def afficher_grille(grille, taille):
	for ligne in grille:
		afficher_separateur(taille)
		afficher_ligne_vide(taille)
		afficher_ligne_rempli(taille, ligne)
		afficher_ligne_vide(taille)
	afficher_separateur(taille)