import pygame
import sys
from Optionspage import Optionspage
from Button import Button

L_RED = (255, 0, 255)
L_YELLOW = (255, 255, 0)
L_BLUE = (0, 255, 255)

aL_RED = (255, 175, 255)
aL_YELLOW = (255, 255, 175)
aL_BLUE = (175, 255, 255)

class Menupage:
	def __init__(self, game):
		self.game = game
		self.start = Button(self.game, 200, 125, L_RED, aL_RED, 'START', alpha = 255)
		self.options = Button(self.game, 200, 250, L_YELLOW, aL_YELLOW, 'OPTIONS', alpha = 255)
		self.exit = Button(self.game, 200, 375, L_BLUE, aL_BLUE, 'EXIT', alpha = 255)


	def draw(self):
		self.start.draw()
		self.options.draw()
		self.exit.draw()
		
	def update(self):
		self.start.update()
		if self.start.click:
			import importlib
			import birdgame
			importlib.reload(birdgame)
			birdgame.main()
		self.options.update()
		if self.options.click:
			self.game.page = Optionspage(self.game)
		self.exit.update()
		if self.exit.click:
			pygame.quit()
			sys.exit()


Optionspage.xxx = Menupage