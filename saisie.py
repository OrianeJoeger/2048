options = ['z', 'q', 's', 'd', '0']

def saisie_joueur():
	print("Veuillez saisir une touche")
	x = input()
	while (x not in options):
		print("Veuillez saisir une touche valide")
		x = input()
	return x