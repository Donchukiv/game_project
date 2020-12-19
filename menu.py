import pygame

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)

#objects
WIN_WIDTH = 500
WIN_HEIGHT = 400
sc = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH), pygame.RESIZABLE)

pygame.init()

class menu:
	def __init__(self, x, y, h=5, w=20, click = False):
		self.x = x
		self.y = y
		self.click = click
		self.h = h #height
		self.w = w #width


	def create_button(self):
		pass

	def click(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.MOUSEBUTTONDOWN:
				self.click = True
		

start = menu(50, 60)

def main_menu():
	while click == False:
		sc.fill(LIGHT_BLUE)#window

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

		pygame.time.delay(20) #50 FPS

		start.create_button()

		pygame.display.update()




if __name__ == '__main_menu__':
	main_menu()
