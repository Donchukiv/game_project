import pygame
import random
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
        if self.orient == 'left':
            spike = pygame.draw.polygon(sc, 'grey', [[self.x - 40, self.y], [self.x, self.y + 20],
                                                     [self.x, self.y - 20]])
        if self.orient == 'right':
            spike = pygame.draw.polygon(sc, 'grey', [[self.x + 40, self.y], [self.x, self.y + 20],
                                                     [self.x, self.y - 20]])

#Create empty lists for spikes
spikes_up = []
spikes_down = []
spikes_left = []
spikes_right = []

#Add spikes into lists (up, down)
def Create_spikes_up_down(spikes_up, spikes_down):
    for i in range (20, 420, 40):
            spike = Spike(i, 40, 'up', True)
            spikes_up.append(spike)
    for i in range (20, 420, 40):
            spike = Spike(i, 460, 'down', True)
            spikes_down.append(spike)

#Add spikes into lists (right, left)
def Create_spikes_right_left(spikes_right, spikes_left):
    for i in range (20, 520, 40):
            spike = Spike(40, i, 'left', False)
            spikes_left.append(spike)
    for i in range (20, 520, 40):
            spike = Spike(360, i, 'right', False)
            spikes_right.append(spike)

#Create lists of spikes
def Create_Spikes(spikes_up, spikes_down, spikes_right, spikes_left):
    Create_spikes_up_down(spikes_up, spikes_down)
    Create_spikes_right_left(spikes_right, spikes_left)

#Draw spikes up and down
def Draw_Spikes_up_down(spikes_up, spikes_down):
    for i in range (len(spikes_up)):
        spikes_up[i].draw()
    for i in range (len(spikes_down)):
        spikes_down[i].draw()

#Draw random spikes on the right    
def Draw_Spikes_right(spikes_right):
    for i in range (len(spikes_right)):
        spikes_right[i].work = random.choice(True, False)
        if spikes_right[i].work == True:
            spikes_right[i].draw()

#Draw random spikes on the left
def Draw_Spikes_left(spikes_left):
    for i in range (len(spikes_left)):
        spikes_left[i].work = random.choice(True, False)
        if spikes_left[i].work == True:
            spikes_left[i].draw()
