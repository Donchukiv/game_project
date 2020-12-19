import pygame

pygame.init()

class Spike:
#Orient - orientation of spike's peak, work - True/False, spike is seen or not.
    def __init__(self, x, y, orient, work):
        self.x = x
        self.y = y
        self.orient = orient
        self.work = work

#Draw spike (triangle), (self.x, self.y) - coords of spike's peak
    def draw(self):
        if self.orient == 'up':
            spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 5, self.y - 5],
                                                    [self.x - 5, self.y - 5]])
        if self.orient == 'down':
            spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 5, self.y + 5],
                                                     [self.x - 5, self.y + 5]])
        if self.work == False:
            if self.orient == 'left':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 5, self.y + 5],
                                                         [self.x + 5, self.y - 5]])
            if self.orient == 'right':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x - 5, self.y + 5],
                                                         [self.x - 5, self.y - 5]])
        if self.work == True:
            if self.orient == 'left':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x - 5, self.y], [self.x, self.y + 5],
                                                         [self.x, self.y - 5]])
            if self.orient == 'right':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x + 5, self.y], [self.x, self.y + 5],
                                                         [self.x, self.y - 5]])

    
