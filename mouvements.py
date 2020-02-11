def action_joueur(saisie):
	if (saisie == 'z'):
		mouvement_haut()
	elif (saisie == 'q'):
		mouvement_gauche()
	elif (saisie == 's'):
		mouvement_bas()
	elif (saisie == 'd'):
		mouvement_droit()

def mouvement_haut():
	print("Mouvement haut")

def mouvement_gauche():
	print("Mouvement gauche")

def mouvement_bas():
	print("Mouvement bas")

def mouvement_droit():
	print("Mouvement droit")