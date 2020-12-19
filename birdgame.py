#modules
import pygame
import spike
import bird
import menu
import game
import sys

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)
BLUE = (0, 70, 225)

#parametrs
FPS = 50
WIN_WIDTH = 500
WIN_HEIGHT = 400

#objects
pygame.init()
sc = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH), pygame.RESIZABLE)
b = bird.bird(40, 80)





def main():
	sc.fill(WHITE)#window

	while 1:
		sc.fill(WHITE)#window

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

		pygame.time.delay(20) #50 FPS

		b.appear()
		b.move()

		pygame.display.update()

		


		


if __name__ == '__main__':
	main()