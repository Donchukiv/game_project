import pygame

GRAY = (111, 111, 111)

class Spike:
#Orient - orientation of spike's peak, work - True/False, spike is seen or not.
    def __init__(self, x, y, orient, work):
        self.x = x
        self.y = y
        self.orient = orient
        self.work = work

#Draw spike (triangle), (self.x, self.y) - coords of spike's peak
    def draw(self, sc):
        if self.orient == 'up':
            spike = pygame.draw.polygon(sc, GRAY, [[self.x, self.y], [self.x + 20, self.y - 40],
                                                    [self.x - 20, self.y - 40]])
        if self.orient == 'down':
            spike = pygame.draw.polygon(sc, GRAY, [[self.x, self.y], [self.x + 20, self.y + 40],
                                                     [self.x - 20, self.y + 40]])
        if self.orient == 'left':
            spike = pygame.draw.polygon(sc, GRAY, [[self.x, self.y], [self.x - 40, self.y + 20],
                                                     [self.x - 40, self.y - 20]])
        if self.orient == 'right':
            spike = pygame.draw.polygon(sc, GRAY, [[self.x, self.y], [self.x + 40, self.y + 20],
                                                     [self.x + 40, self.y - 20]])

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
    for i in range (50, 490, 40):
            spike = Spike(40, i, 'left', False)
            spikes_left.append(spike)
    for i in range (50, 490, 40):
            spike = Spike(360, i, 'right', False)
            spikes_right.append(spike)

#Create lists of spikes
def Create_Spikes(spikes_up, spikes_down, spikes_right, spikes_left):
    Create_spikes_up_down(spikes_up, spikes_down)
    Create_spikes_right_left(spikes_right, spikes_left)

#Draw all spikes
def Draw_all_spikes(sc, spikes_up, spikes_down, spikes_right, spikes_left):
    for i in range (len(spikes_up)):
        spikes_up[i].draw(sc)
    for i in range (len(spikes_down)):
        spikes_down[i].draw(sc)
    for i in range (len(spikes_right)):
        if spikes_right[i].work == True:
            spikes_right[i].draw(sc)
    for i in range (len(spikes_left)):
        if spikes_left[i].work == True:
            spikes_left[i].draw(sc)
