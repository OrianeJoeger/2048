def bienvenue():
	print("\nBIENVENUE AU 2048\n")
	print("Touches :")
	print("\tz --> haut")
	print("\tq --> gauche")
	print("\ts --> bas")
	print("\td --> droite")
	print("\t0 --> arreter la partie")

def afficher_grille(grille, taille):
	separator = '+'
	for i in range(len(grille)):
		separator += str('-').rjust(taille + 2, '-')
		separator += '+'

	for ligne in grille:
		display = ''
		for cell in ligne:
			display += '| '
			if cell > 0:
				display += str(cell).rjust(taille, ' ')
			else:
				display += str('').rjust(taille, ' ')
			display += ' '

		print(separator)
		print(display + '|')
	print(separator)