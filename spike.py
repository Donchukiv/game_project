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
            spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 20, self.y - 40],
                                                    [self.x - 20, self.y - 40]])
        if self.orient == 'down':
            spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 20, self.y + 40],
                                                     [self.x - 20, self.y + 40]])
        if self.work == False:
            if self.orient == 'left':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x + 40, self.y + 20],
                                                         [self.x + 40, self.y - 20]])
            if self.orient == 'right':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x, self.y], [self.x - 40, self.y + 20],
                                                         [self.x - 40, self.y - 20]])
        if self.work == True:
            if self.orient == 'left':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x - 40, self.y], [self.x, self.y + 20],
                                                         [self.x, self.y - 20]])
            if self.orient == 'right':
                spike = pygame.draw.polygon(sc, 'grey', [[self.x + 40, self.y], [self.x, self.y + 20],
                                                         [self.x, self.y - 20]])

#Create lists of spikes
def Create_Spikes():
    global spikes_up = [], spikes_down = [], spikes_left = [], spikes_right = []

    def Create_spikes_up_down(spikes_up, spikes_down):
        for i in range (20, 420, 40):
                spike = Spike(i, 460, 'up', True)
                spikes_up.append(spike)
        for i in range (20, 420, 40):
                spike = Spike(i, 40, 'down', True)
                spikes_down.append(spike)

    def Create_spikes_right_left(spikes_right, spikes_left):
        for i in range (20, 520, 40):
                spike = Spike(0, i, 'right', False)
                spikes_right.append(spike)
        for i in range (20, 520, 40):
                spike = Spike(0, i, 'left', False)
                spikes_left.append(spike)

    Create_spikes_up_down(spikes_up, spikes_down)
    Create_spikes_right_left(spikes_right, spikes_left)
    
