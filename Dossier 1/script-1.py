
"""
Question 1:
Proposer une solution fondée sur les héritages entre classe pour représenter 
toutes les émissions possibles. Donner pour chaque classe, la liste de ses 
attributs et les paramètres de ses constructeurs. Comment coderiez-vous le 
fait que le thème d’un reportage soit prédéfini ?
"""

import abc

class Emission(metaclass=abc.ABCMeta):
	@abc.abstractmethod
 
	def __init__(self, name, h_debut=0, h_fin=0):
		self.is_name = name
		self.h_debut = h_debut
		self.h_fin = h_fin
	
class Divertissement(Emission):
	def __init__(self, name, animateur):	
		Emission.__init__(self, name)
		self.is_animateur = animateur
		self.duree = 2

class Fiction(Emission):
	def __init__(self, name, realisateur, rediffusion, d):
		Emission.__init__(self, name)
		self.is_realisateur = realisateur
		self.is_rediffusion = rediffusion
		self.duree = d

class Reportage(Emission):
	theme = ["Information", "Animalier", "Culturel"]
	def __init__(self, name, themes, d):
		Emission.__init__(self, name)
		self.types_themes = themes
		self.duree = d





