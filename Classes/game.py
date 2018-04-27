import random

class person:
	def __init__(self,hp,mp,atk,df,magic):
		self.maxhp=hp
		self.hp=hp
		self.maxmp = mp
		self.mp = mp
		self.atkl = atk - 10
		self.atkh = atk + 10
		self.df = df
		self.magic = magic
		self.actions = ["Attack", "Magic"]

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)