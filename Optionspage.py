from Button import Button

YELLOW = (241, 224, 14)
ORANGE = (255, 128, 0)
RED = (236, 19, 19)
GREEN = (26, 225, 105)
LIGHT_BLUE = (31, 220, 216)
BLUE = (22, 48, 228)
PINK = (255, 0, 128)
PURPLE = (151, 16, 216)

aORANGE = (255, 200, 0)

PASTEL = (229, 229, 229)

class Optionspage:
	def __init__(self, game):
		self.game = game
		self.form1 = Button(self.game, 150, 100, PASTEL, aORANGE, image = self.game.image1, h = 90, w = 90, alpha = 120)
		self.form2 = Button(self.game, 250, 100, PASTEL, aORANGE, image = self.game.image2, h = 90, w = 90, alpha = 120)
		#self.level = Button(self.game, 200, 175, (0, 0, 0), (0, 0, 0))
		self.back = Button(self.game, 200, 350, ORANGE, aORANGE, 'BACK', w = 120)

		self.c1 = Button(self.game, 60, 200, YELLOW, PASTEL, h = 20, w = 20, alpha = 255)
		self.c2 = Button(self.game, 100, 200, ORANGE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c3 = Button(self.game, 140, 200, RED, PASTEL, h = 20, w = 20, alpha = 255)
		self.c4 = Button(self.game, 180, 200, GREEN, PASTEL, h = 20, w = 20, alpha = 255)
		self.c5 = Button(self.game, 220, 200, LIGHT_BLUE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c6 = Button(self.game, 260, 200, BLUE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c7 = Button(self.game, 300, 200, PINK, PASTEL, h = 20, w = 20, alpha = 255)
		self.c8 = Button(self.game, 340, 200, PURPLE, PASTEL, h = 20, w = 20, alpha = 255)

	def draw(self):
		self.form1.draw()
		self.form2.draw()
		self.c1.draw()
		self.c2.draw()
		self.c3.draw()
		self.c4.draw()
		self.c5.draw()
		self.c6.draw()
		self.c7.draw()
		self.c8.draw()
		self.back.draw()
		
	def update(self):
		self.form1.update()
		if self.form1.click:
			self.game.image = self.game.image1
			self.form1.click = False
		self.form2.update()
		if self.form2.click:
			self.game.image = self.game.image2
			self.form2.click = False
		self.back.update()
		if self.back.click:
			self.game.page = self.xxx(self.game)