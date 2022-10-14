
"""
Question 3:
La programmation d’une émission dans la journée dépend du type 
d’émission mais se traduit par le fait de lui fixer une heure de 
début de diffusion et de calculer l’heure de fin.
"""

"""
Question 3.1:
Les divertissements durent systématiquement 2 heures, mais on ne peut les
programmer qu’entre 18h et 23h.
"""

"""
Question 3.2:
Les fictions qui ne sont pas des rediffusions ne se programment qu’en début de
soirée, c’est-à-dire qu’à 21h, alors qu’une rediffusion peut se programmer n’importe
quand dans la journée.
"""

"""
Question 3.3:
Enfin, les reportages ne se programment qu’à des heures creuses (14h –18h et 0h-
6h) et s’ils ont une durée inférieure, égale à 1heure. Proposer une solution fondée 
sur la notion de classe abstraite et de polymorphisme permettant de
décrire la programmation ou non de n’importe quelle émission à une heure donnée. 
Comment initialiser efficacement ces heures de début et de fin de diffusion.
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

	def affiche(self):
		print("-------      ------- ")
		print(f"L'émission est : {self.is_name}")
		if self.h_debut != -1:
			print(f"L'émission est programmée à : {self.h_debut} H")
	
class Divertissement(Emission):
	def __init__(self, is_name, is_animateur):	
		Emission.__init__(self, is_name)
		self.is_animateur = is_animateur
		self.duree = 2

	def affiche(self):
		super().affiche()
		print(f"L'animateur est : {self.is_animateur}")
		print(f"La durée est : {self.duree} H")

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
		print(f"La durée est : {self.duree} H")
		print(f"L'année de réalisation est : {self.annee}")
		if self.is_rediffusion:
			print("C'est la rédiffusion")
		else:
			print("La prémière diffusion")

	def programmer(self, heure):
		if self.is_rediffusion | heure == 21:
			self.h_debut = heure
			self.h_fin = heure + self.duree
			return True
		else:
			return False

class Reportage(Emission):
	theme = ["Information", "animateur", "Culturel"]
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
			print(f"Le theme est : {Reportage.theme[2]}")
		print(f"La duree est : {self.duree} H")

	def programmer(self, heure:int)->bool:
		if self.duree == 1 & (14 <= heure <= 18) | (0 <= heure <= 6):
			self.h_debut = heure
			self.h_fin = heure + self.duree
			return True
		else:
			return False

 	
if __name__ == '__main__':

	print("-------      ------- ")
	print("La question 2 ")
	print("-------      ------- ")
	
	emission1 = Divertissement("DEFEND TES 50 000", "ADAMA DAHICO")
	if emission1.programmer(20):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")

	emission2 = Fiction("LES COUPS DE LA VIE", "A+ IVOIRE", True, 3, 2018)
	if emission2.programmer(20):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")

	emission3 = Reportage("LABEL'IVOIRE", 2, 1)
	if emission3.programmer(17):
		print("Emission programmée")
	else:
		print("Emission pas encore programmée")

	print("-------      ------- ")
	print("La question 3")
	print("-------      ------- ")

	if emission1.programmee():
		emission1.affiche()
	if emission2.programmee():
		emission2.affiche()
	if emission3.programmee():
		emission3.affiche()



			











		
		
