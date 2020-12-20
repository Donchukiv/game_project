import pygame
from Menupage import Menupage
import bird

WIN_WIDTH = 400
WIN_HEIGHT = 500

LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
ORANGE = (255, 150, 100)

class Game:
	def __init__(self):
		pygame.init()
		self.sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
		self.page = Menupage(self)
		self.pos = pygame.mouse.get_pos()
		self.events = []
		self.image1 = pygame.Surface((50,50), pygame.SRCALPHA)
		self.image1.fill((0,0,0,0))
		self.image2 = pygame.Surface((50,50))
		self.image = self.image1
		pygame.draw.circle(self.image1, ORANGE, (25,25), 25)
		self.image2.fill(ORANGE)


	def draw(self):
		self.sc.fill(LIGHT_BLUE)
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
		
		game.update()
		game.draw()

		



if __name__ == '__main__':
	main()
