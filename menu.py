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

#parametrs
WIN_WIDTH = 500
WIN_HEIGHT = 400

#objects
pygame.init()
sc = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH), pygame.RESIZABLE)




class menu:
	def __init__(self, x, y, h=50, w=100, click = False):
		self.x = x
		self.y = y
		self.click = click
		self.h = h #height
		self.w = w #width


	def create_button(self, x, y, w, h):
		surf = pygame.Surface((h, w))
		surf.fill(GREEN)
		surf.set_alpha(150)
		sc.blit(surf, (x, y))


	def clickbyte(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.MOUSEBUTTONDOWN:
				self.click = True
		

start = menu(150, 100)


def main():
		
	while 1:
		sc.fill(LIGHT_BLUE)#window

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
		pygame.time.delay(20) #50 FPS

		start.create_button(start.x, start.y, start.h, start.w)
		start.clickbyte()

		pygame.display.update()
		



if __name__ == '__main__':
	main()
