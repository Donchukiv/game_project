import pygame
from Menupage import Menupage
import bird

WIN_WIDTH = 400
WIN_HEIGHT = 500

YELLOW = (241, 224, 14)
ORANGE = (255, 128, 0)
RED = (236, 19, 19)
GREEN = (26, 225, 105)
LIGHT_BLUE = (31, 220, 216)
BLUE = (22, 48, 228)
PINK = (255, 0, 128)
PURPLE = (151, 16, 216)

PASTEL = (229, 229, 229)

COLORS = [YELLOW, ORANGE, RED, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE]

class Game:
	def __init__(self):
		pygame.init()
		self.sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
		self.page = Menupage(self)
		self.pos = pygame.mouse.get_pos()
		self.events = []
		self.image1 = pygame.Surface((50,50), pygame.SRCALPHA)
		#self.image1.fill((0,0,0,0))
		self.image2 = pygame.Surface((50,50))
		self.image = self.image1
		self.color = RED
		pygame.draw.circle(self.image1, self.color, (25,25), 25) #!!!!!!!!!!!
		self.image2.fill(self.color)


	def draw(self):
		self.sc.fill(PASTEL)
		self.page.draw()
		pygame.display.update()

	def update(self):
		self.pos = pygame.mouse.get_pos()
		self.events = pygame.event.get()
		for i in self.events:
			if i.type == pygame.QUIT:
				pygame.quit()
		pygame.time.delay(20) #50 FPS

		self.page.update()


def main(x=0):


	game = Game()
	bird.bird.game = game
	bird.bird.yyy = main

	while 1:
		
		game.draw()
		game.update()
		

		



if __name__ == '__main__':
	main()
