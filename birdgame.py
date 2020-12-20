#modules
import pygame
import random
import spike
import bird
import game
import sys
from candy import candy


#colors
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

#parametrs
FPS = 50
WIN_WIDTH = 400
WIN_HEIGHT = 500

#objects
#pygame.init()
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

#All for candy
candyscore = []
cx = random.randint(60, 340)
cy = random.randint(60, 440)
ccolor_1 = random.choice(COLORS)
ccolor_2 = random.choice(COLORS)
while ccolor_1 == ccolor_2:
	ccolor_2 = random.choice(COLORS)
clive = 1

c = candy(cx, cy, ccolor_1, ccolor_2)

def main():

	while 1:
		#First screen
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit() 
		sc.fill(PASTEL)#window
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
						sc.fill(PASTEL)#window
						game.Show_score(score, candyscore, sc)
						pygame.time.delay(20) #50 FPS
						game.Hittest(b, spikes_up, spikes_down, spikes_right, spikes_left)
						game.Death(b, Dead)
						game.Check_wall_hit(b, spikes_right, spikes_left, score, Dead)
						spike.Draw_all_spikes(sc, spikes_up, spikes_down, spikes_right, spikes_left)	
						c.appear(sc)
						game.Hit_candy(c, b, candyscore)
						game.Plus_candy(c)
						b.appear()
						b.move()
						b.death()
						
						
						pygame.display.update()

if __name__ == '__main__':
	main()          

