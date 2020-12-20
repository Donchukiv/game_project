#modules
import pygame
import spike
import bird
import game
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
BLUE = (0, 70, 225)

#parametrs
FPS = 50
WIN_WIDTH = 400
WIN_HEIGHT = 500

#objects
pygame.init()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)


b = bird.bird(40, 80)

#Create empty lists for spikes
spikes_up = []
spikes_down = []
spikes_left = []
spikes_right = []

spike.Create_Spikes(spikes_up, spikes_down, spikes_right, spikes_left)
Dead = []
score = []

def main():

	while 1:
		#First screen
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit() 
		sc.fill(WHITE)#window
		pygame.time.delay(20) #50 FPS


		spike.Draw_all_spikes(sc, spikes_up, spikes_down, spikes_right, spikes_left)		
		b.appear()
		pygame.display.update()
		#Game begins after pressing SPACE
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			if i.type == pygame.KEYUP:
				if i.key == pygame.K_SPACE:
					while 1:
						sc.fill(WHITE)#window
						pygame.time.delay(20) #50 FPS
						game.Check_wall_hit(b, spikes_right, spikes_left, score)
						spike.Draw_all_spikes(sc, spikes_up, spikes_down, spikes_right, spikes_left)		
						b.appear()
						b.move()

						game.Hittest(b, spikes_up, spikes_down, spikes_right, spikes_left)
						
						b.death()
						pygame.display.update()

if __name__ == '__main__':
	main()

