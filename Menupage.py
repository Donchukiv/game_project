import pygame
# import birdgame
import sys
from Optionspage import Optionspage
from Button import Button

LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)




class Menupage:
	def __init__(self, game):
		self.game = game
		self.start = Button(self.game, 200, 100, 'START')
		self.options = Button(self.game, 200, 175, 'OPTIONS')
		self.exit = Button(self.game, 200, 250, 'EXIT')


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