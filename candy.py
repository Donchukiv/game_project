#modules
import pygame

class candy:
	def __init__(self, cx, cy, ccolor_1, ccolor_2, r1 = 10, r2 = 6):
		self.x = cx
		self.y = cy
		self.r1 = r1
		self.r2 = r2
		self.color_1 = ccolor_1
		self.color_2 = ccolor_2
		self.live = 1

	def appear(self, sc):
		pygame.draw.polygon(sc, self.color_1, [[self.x, self.y], [self.x + 20, self.y + 10], [self.x + 20, self.y - 10]])
		pygame.draw.polygon(sc, self.color_1, [[self.x, self.y], [self.x - 20, self.y + 10], [self.x - 20, self.y - 10]])

		pygame.draw.polygon(sc, self.color_2, [[self.x, self.y], [self.x + 15, self.y + 8], [self.x + 15, self.y - 8]])
		pygame.draw.polygon(sc, self.color_2, [[self.x, self.y], [self.x - 15, self.y + 8], [self.x - 15, self.y - 8]])

		pygame.draw.circle(sc, self.color_1, (self.x, self.y), self.r1)
		pygame.draw.circle(sc, self.color_2, (self.x, self.y), self.r2)
		