import pygame
GREEN = (0, 200, 64)


class Button:
	def __init__(self, game, x, y, text = None, image = None, h=50, w=200, click = False, alpha = 150):
		self.x = x
		self.y = y
		self.click = click #if button was tapped indicator
		self.h = h #height
		self.w = w #width
		self.text = text
		self.image = image
		self.game = game
		self.surf = pygame.Surface((self.w, self.h))
		self.surf.fill(GREEN)
		self.surf.set_alpha(alpha)
		if text is not None:
			text_font = pygame.font.SysFont('arial', 36) #choosing text style
			self.title = text_font.render(self.text, 1, (0,0,0)) #rendering text(text, smoothing, color)

			



		# button creation(figure)
	def draw(self):
		place = self.surf.get_rect(center=(self.x, self.y))
		self.game.sc.blit(self.surf, place)
		if self.text is not None:
			self.game.sc.blit(self.title, place)
		if self.image is not None:
			self.game.sc.blit(self.image, place)


	def update(self):
		for i in self.game.events:
				
				if i.type == pygame.MOUSEBUTTONDOWN and self.clickable_square(self.game.pos):
					if i.button == 1:
						#print(1)
						self.click = True

		
		
		
			#defines clickable square
	def clickable_square(self, pos):

		#pygame.draw.rect(sc, YELLOW, (pos[0] - 100, pos[1] - 25, 200, 50)) #check active square
		return pos[0] >= self.x-self.w//2 and pos[0] <= self.x+self.w//2 and pos[1] <= self.y+self.h//2 and pos[1] >= self.y-self.h//2
				
			#check if button was pressed
		