
"""
Question 2: 
Implanter cette solution sous python et tester tout d’abord les 
classes que vous avez imaginées en instanciant différents objets de 
votre choix (avec les constructeurs) pour chacune de celles-ci.
"""

import abc

class Emission(metaclass=abc.ABCMeta):
	@abc.abstractmethod
 
	def __init__(self, name, h_debut=0, h_fin=0):
		self.is_name = name
		self.h_debut = h_debut
		self.h_fin = h_fin
	
	def __str__(self):
		return self.is_name

class Divertissement(Emission):
	def __init__(self, name, animateur):
	
		Emission.__init__(self, name)
		self.is_animateur = animateur
		self.duree = 2
	def __str__(self):
		return f"Divertissement: {super().__str__()} animateuré par: {self.is_animateur}"

class Fiction(Emission):
	def __init__(self, name, realisateur, rediffusion, d):
		Emission.__init__(self, name)
		self.is_realisateur = realisateur
		self.is_rediffusion = rediffusion
		self.duree = d
	def __str__(self):
		return f"Fiction: {super().__str__()} realisateurisé par: {self.is_realisateur}"

class Reportage(Emission):
	def __init__(self, name, themes, d):
		Emission.__init__(self,name)
		self.theme = themes
		self.duree = d

	def __str__(self):
		return f"Reportage: {super().__str__()} sur: {self.theme}"

if __name__ == '__main__':
	
	emission1 = Divertissement("DEFEND TES 50 000", "ADAMA DAHICO")
	print(emission1)
	emission2 = Fiction("LES COUPS DE LA VIE", "A+ IVOIRE", True, 3)
	print(emission2)
	emission3 = Reportage("LABEL'IVOIRE", "YANN BAHOU", 4)
	print(emission3)





