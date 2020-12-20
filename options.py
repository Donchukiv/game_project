#modules
import pygame
import menu

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GREY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)

#parametrs
WIN_WIDTH = 400
WIN_HEIGHT = 500

#objects
pygame.init()
sc1 = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)


class Options(menu.Menu):
	def __init__(self, x, y, h=100, w=100, click=False):
		super().__init__(sc, x, y, h, w, click)
		self.sc = sc1

		'''
class Options:
	def __init__(self, x, y, h=50, w=200, click = False):
		self.x = x
		self.y = y
		self.click = click #if button was tapped indicator
		self.h = h #height
		self.w = w #width
		'''



#initiallizing button
kvadrat = Options(150, 350)
krug = Options(250, 350)

def main():
	while 1:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit() 
		sc1.fill(WHITE)#window
		pygame.time.delay(20) #50 FPS

		krug.create_button()


		pygame.display.update()


if __name__ == '__main__':
	main()