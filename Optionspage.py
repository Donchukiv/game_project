from Button import Button

class Optionspage:
	def __init__(self, game):
		self.game = game
		self.form1 = Button(self.game, 150, 100, (0, 0, 0), (0, 0, 0), image = self.game.image1, w=50, alpha = 0)
		self.form2 = Button(self.game, 250, 100, (0, 0, 0), (0, 0, 0), image = self.game.image2, w = 50)
		self.level = Button(self.game, 200, 175, (0, 0, 0), (0, 0, 0))
		self.back = Button(self.game, 200, 250, (0, 0, 0), (0, 0, 0), 'BACK')

	def draw(self):
		self.form1.draw()
		self.form2.draw()
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