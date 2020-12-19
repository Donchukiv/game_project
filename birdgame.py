import pygame
import sys

pygame.init()



def main():
	pygame.display.set_mode((400, 500), pygame.RESIZABLE) #window

	while 1:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.time.delay(20) #50 FPS

if __name__ == '__main__':
	main()