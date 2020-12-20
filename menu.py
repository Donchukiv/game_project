import pygame
import birdgame
#import options
import sys

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

pos = pygame.mouse.get_pos()
events = []


class Menu:
	def __init__(self, sc, x, y, text, h=50, w=200, click = False):
		self.x = x
		self.y = y
		self.click = click #if button was tapped indicator
		self.h = h #height
		self.w = w #width
		self.text = text
		self.sc = sc

		# button creation(figure)
	def create_button(self):
		self.surf = pygame.Surface((self.w, self.h))
		self.surf.fill(GREEN)
		self.surf.set_alpha(150)
		place = self.surf.get_rect(center=(self.x, self.y))
		self.sc.blit(self.surf, place)

	def create_title(self):
		text_font = pygame.font.SysFont('arial', 36) #choosing text style
		self.title = text_font.render(self.text, 1, (0,0,0)) #rendering text(text, smoothing, color)
		place = self.title.get_rect(center=(self.x, self.y))
		self.sc.blit(self.title, place)
		
		#defines clickable square
	def clickable_square(self):
		#pygame.draw.rect(sc, YELLOW, (pos[0] - 100, pos[1] - 25, 200, 50)) #check active square
		return pos[0] >= self.x-100 and pos[0] <= self.x+100 and pos[1] <= self.y+25 and pos[1] >= self.y-25
			
		#check if button was pressed
	def clickbyte(self):
		for i in events:
			
			if i.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if i.type == pygame.MOUSEBUTTONDOWN and self.clickable_square():
				if i.button == 1:
					self.click = True
		


#running menu function
def main():
	global pos, events

	pygame.init()
	sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)

	#menu buttons and their coords, titles
	start = Menu(sc, 200, 100, 'START') #(center x, center y, title)
	options = Menu(sc, 200, 175, 'OPTIONS')
	exit = Menu(sc, 200, 250, 'EXIT')

		
	while 1:
		sc.fill(LIGHT_BLUE)#window
		events = pygame.event.get()

		for i in events:
			if i.type == pygame.QUIT:
				pygame.quit()
		pygame.time.delay(20) #50 FPS

		pos = pygame.mouse.get_pos()
		
		start.create_button()
		start.create_title()
		start.clickbyte()

		if start.click == True:
			birdgame.main()

		
		options.create_button()
		options.create_title()
		options.clickbyte()

		if options.click == True:
			options.main()
		
		
		exit.create_button()
		exit.create_title()
		exit.clickbyte()

		if exit.click == True:
			pygame.quit()
			sys.exit()





		
			#pygame.quit()
			#sys.exit()
		
		
			#exit()
			#options.main()
		
		
		
		
			#birdgame.main()

		#print(options.click)

		pygame.display.update()
		

if __name__ == '__main__':
	main()
