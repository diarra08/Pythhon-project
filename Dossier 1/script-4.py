
"""
Quesion 4:
Définissez enfin un programme télé comme un ensemble fini (tableau) 
d’émissions hétérogènes que vous remplirez d’émission de votre choix, 
programmer à une heure de votre choix. Décrire puis implémenter les 
algorithmes vous permettant :
"""

"""
Quesion 4.1:
Afficher la liste des émissions programmées dans la journée
"""
"""
Quesion 4.2:
Tester s’il y a une superposition de programmation.
"""
"""
Quesion 4.4:
Afficher heure par heure les émissions programmées pour vérifier que 
tous les créneaux horaires ont bien été remplis.
"""

import abc

class Emission(metaclass=abc.ABCMeta):
	@abc.abstractmethod
 
	def __init__(self, is_name):
		self.is_name = is_name
		self.h_debut = -1
		self.h_fin = -1

	@abc.abstractmethod
 
	def programmer(self, heure:int)->bool:
		...

	def programmee(self):
		if self.h_debut != -1:
			return True
		else:
			return False
	def get_debut(self):
		return self.h_debut
	def get_fin(self):
		return self.h_debut

	def affiche(self):
		print("-------      ------- ")
		print(f"L'émission est : {self.is_name}")
		if self.h_debut != -1:
			print(f"L'émission est programmée à : {self.h_debut}H")
	
	
class Divertissement(Emission):
	def __init__(self, is_name, is_animateur):	
		Emission.__init__(self, is_name)
		self.is_animateur = is_animateur
		self.duree = 2

	def affiche(self):
		super().affiche()
		print(f"L'animateur est : {self.is_animateur}")
		print(f"La durée est : {self.duree}H")

	def programmer(self, heure):
		if 18 <= heure <= 21:
			self.h_debut = heure
			self.h_fin = heure + self.duree
			return True
		else:
			return False

class Fiction(Emission):
	def __init__(self, is_name, realisateur, rediffusion=False, duree=0, annee=0):
		Emission.__init__(self, is_name)
		self.is_realisateur = realisateur
		self.is_rediffusion = rediffusion
		self.duree = duree
		self.annee = annee

	def affiche(self):
		super().affiche()
		print(f"Le réalisateur est : {self.is_realisateur}")
		print(f"La durée est : {self.duree}H")
		print(f"L'année de réalisation est:{self.annee}")
		if self.is_rediffusion:
			print("C'est une rédiffusion")
		else:
			print("La prémière Diffusion !")

	def programmer(self, heure):
		if self.is_rediffusion | heure == 21:
			self.h_debut = heure
			self.h_fin = heure + self.duree
			return True
		else:
			return False

class Reportage(Emission):
	theme = ["Information", "Animalier", "Culturel"]
	def __init__(self, is_name, types_themes, duree):
		Emission.__init__(self, is_name)
		self.types_themes = types_themes
		self.duree = duree

	def affiche(self):
		super().affiche()
		if self.types_themes == 1:
			print(f"Le theme est : {Reportage.theme[0]}")
		elif self.types_themes == 2:
			print(f"Le theme est : {Reportage.theme[1]}")
		elif self.types_themes == 3:
			print(f"Le theme est: {Reportage.theme[2]}")
		print(f"La duree est : {self.duree}H")

	def programmer(self, heure:int)->bool:
		if self.duree == 1 & (14 <= heure <= 18) | (0 <= heure <= 6):
			self.h_debut = heure
			self.h_fin = heure + self.duree
			return True
		else:
			return False

if __name__ == '__main__':

	nb_emission = 4
	
	emission1 = Divertissement("DEFEND TES 50 000", "ADAMA DAHICO")
	if emission1.programmer(20):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")

	emission2 = Fiction("LES COUPS DE LA VIE", "A+ IVOIRE", True, 3)
	if emission2.programmer(21):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")

	emission3 = Reportage("LABEL'IVOIRE", 1, 1)
	if emission3.programmer(5):
		print("Ok Emission programmée")
	else:
		print("Emission non programmée")

	emission4 = Reportage("ON SE DIT LES GBE", 2, 1)
	if emission4.programmer(5):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")
	print(" ")

	print("-------      ------- ")
	print("La question 4.1")
	programme = []
	programme.append(emission1)
	programme.append(emission2)
	programme.append(emission3)
	programme.append(emission4)

	for i in range(nb_emission):
		if programme[i].programmee():
			programme[i].affiche()
		else:
			print("-------      ------- ")
			print(f"Programmer l'heure pour {programme[i].__class__}")
	print("        ")

	print("-------      ------- ")
	print("La question 4.2")
	print("-------      ------- ")

	plage = [False] * 24

	for i in range(nb_emission):
		if programme[i].programmee():
			print(f"Plage: {programme[i].get_debut()}H")
			j = programme[i].get_debut()
			while j < programme[i].get_fin():
				j += 1
			if plage[j] is False:
				plage[j] = True
			else:
				print(f"Attention: superposition {j}H")
	print("      ")

	print("-------      ------- ")
	print("La question 4.3")
	print("-------      ------- ")
	print("Pas de superposition ?")

	plage2 = [-1] * 24

	for i in range(nb_emission):
		if programme[i].programmee():
			print(f"Plage: {programme[i].get_debut()}H")
			j = programme[i].get_debut()
			while j < programme[i].get_fin():
				j += 1
			plage2[j] = i

	print("-------      ------- ")
	print("LE PLAN GENERAL")

	for i in range(24):
		print(f"Plage : {i}")
		if plage2[i] != -1:
			programme[plage2[i]].affiche()
		else:
			print("Pas d'émission pour le moment")










			











		
		
