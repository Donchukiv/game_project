import pygame
import birdgame

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
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)



class menu:
	def __init__(self, x, y, text, h=50, w=200, click = False):
		self.x = x
		self.y = y
		self.click = click #if button was tapped indicator
		self.h = h #height
		self.w = w #width
		self.text = text

		# button creation(figure)
	def create_button(self, x, y, w, h):
		self.surf = pygame.Surface((h, w))
		self.surf.fill(GREEN)
		self.surf.set_alpha(150)
		place = self.surf.get_rect(center=(x, y))
		sc.blit(self.surf, place)

	def create_title(self, text, x, y):
		text_font = pygame.font.SysFont('arial', 36) #choosing text style
		self.title = text_font.render(text, 1, (0,0,0)) #rendering text(text, smoothing, color)
		place = self.title.get_rect(center=(x, y))
		sc.blit(self.title, place)
		
	def clickable_square(self, x, y):
		pos = pygame.mouse.get_pos()
		if pos[0] >= x-100 and pos[0] <= x+100 and pos[1] <= y+25 and pos[1] >= y-25:
			return True
			
		#check if button was tapped
	def clickbyte(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			if i.type == pygame.MOUSEBUTTONDOWN and self.clickable_square(self.x, self.y):
				if i.button == 1:
					self.click = True
		
#menu buttons and their coords, titles
start = menu(200, 100, 'START') #(center x, center y, title)
options = menu(200, 175, 'OPTIONS')
exit = menu(200, 250, 'EXIT')

#running menu function
def main():
		
	while 1:
		sc.fill(LIGHT_BLUE)#window

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
		pygame.time.delay(20) #50 FPS

		start.create_button(start.x, start.y, start.h, start.w)
		start.create_title(start.text, start.x, start.y)
		start.clickbyte()
		#print(not start.click) -  clickbyte is working!

		options.create_button(options.x, options.y, options.h, options.w)
		options.create_title(options.text, options.x, options.y)
		options.clickbyte()

		exit.create_button(exit.x, exit.y, exit.h, exit.w)
		exit.create_title(exit.text, exit.x, exit.y)
		exit.clickbyte()


		#почему-то сюда не доходит цикл
		if exit.click == True:
			exit()
		elif options.click == True:
			options.main()
			print(options.click)
		elif start.click == True:
			birdgame.main()
			print(pygame.mouse.get_pos())

		pygame.display.update()
		



if __name__ == '__main__':
	main()
