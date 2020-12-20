from Button import Button
import pygame
import spike

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
	def __init__(self, game, spike):
		self.game = game

		self.form1 = Button(self.game, 150, 100, PASTEL, aORANGE, image = self.game.image1, h = 90, w = 90, alpha = 120)
		self.form2 = Button(self.game, 250, 100, PASTEL, aORANGE, image = self.game.image2, h = 90, w = 90, alpha = 120)
		self.back = Button(self.game, 200, 350, ORANGE, aORANGE, 'BACK', w = 120)

		#color buttons
		self.c1 = Button(self.game, 60, 240, YELLOW, PASTEL, h = 20, w = 20, alpha = 255)
		self.c2 = Button(self.game, 100, 240, ORANGE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c3 = Button(self.game, 140, 240, RED, PASTEL, h = 20, w = 20, alpha = 255)
		self.c4 = Button(self.game, 180, 240, GREEN, PASTEL, h = 20, w = 20, alpha = 255)
		self.c5 = Button(self.game, 220, 240, LIGHT_BLUE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c6 = Button(self.game, 260, 240, BLUE, PASTEL, h = 20, w = 20, alpha = 255)
		self.c7 = Button(self.game, 300, 240, PINK, PASTEL, h = 20, w = 20, alpha = 255)
		self.c8 = Button(self.game, 340, 240, PURPLE, PASTEL, h = 20, w = 20, alpha = 255)

		self.form = Button(self.game, 200, 240, (255, 255, 255), (255, 255, 255), h = 50, w = 400, alpha = 120)

		self.font = pygame.font.SysFont('arial', 30)
		self.title1 = self.font.render('CHOOSE BIRD SHAPE', 1, (0, 0, 0))
		self.place_1 = self.title1.get_rect(center=(200, 35))
		self.title2 = self.font.render('CHOOSE BIRD COLOR', 1, (0, 0, 0))
		self.place_2 = self.title2.get_rect(center=(200, 195))

	def draw(self):

		self.game.sc.blit(self.title1, self.place_1)
		self.game.sc.blit(self.title2, self.place_2)

		self.form1.draw()
		self.form2.draw()

		self.form.draw()

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
			self.game.page = self.xxx(self.game, spike)

		self.c1.update()
		if self.c1.click:
			self.game.color = YELLOW
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c1.click = False
		self.c2.update()
		if self.c2.click:
			self.game.color = ORANGE
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c2.click = False
		self.c3.update()
		if self.c3.click:
			self.game.color = RED
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c3.click = False
		self.c4.update()
		if self.c4.click:
			self.game.color = GREEN
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c4.click = False
		self.c5.update()
		if self.c5.click:
			self.game.color = LIGHT_BLUE
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c5.click = False
		self.c6.update()
		if self.c6.click:
			self.game.color = BLUE
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c6.click = False
		self.c7.update()
		if self.c7.click:
			self.game.color = PINK
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c7.click = False
		self.c8.update()
		if self.c8.click:
			self.game.color = PURPLE
			pygame.draw.circle(self.game.image1, self.game.color, (25,25), 25)
			self.game.image2.fill(self.game.color)
			self.c8.click = False
