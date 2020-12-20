import pygame
import bird
import spike
import random

pygame.init()

#Check if bird hits spike
def Hittest(bird, spikes_up, spikes_down, spikes_right, spikes_left):
    for i in range (len(spikes_up)):
        if (spikes_up[i].x - bird.x)**2 + (spikes_up[i].y - bird.y)**2 == bird.r**2:
            bird.live = 0
    for i in range (len(spikes_down)):
        if (spikes_down[i].x - bird.x)**2 + (spikes_down[i].y - bird.y)**2 == bird.r**2:
            bird.live = 0
    for i in range (len(spikes_right)):
        if (spikes_right[i].x - bird.x)**2 + (spikes_right[i].y - bird.y)**2 == bird.r**2:
            bird.live = 0
    for i in range (len(spikes_left)):
        if (spikes_left[i].x - bird.x)**2 + (spikes_left[i].y - bird.y)**2 == bird.r**2:
            bird.live = 0
            
#New spikes appear (when bird changes its orientation)
def Change_spikes(bird, spikes_right, spikes_left):
    if bird.orient == 1:
        for i in range (len(spikes_right)):
            spikes_right[i].work = random.choice([True, False])
        for i in range (len(spikes_left)):
            spikes_left[i].work = False
    if bird.orient == -1:
        for i in range (len(spikes_left)):
            spikes_left[i].work = random.choice([True, False])
        for i in range (len(spikes_right)):
            spikes_right[i].work = False

#Check if bird hits wall 
def Check_wall_hit(bird, spikes_right, spikes_left):
    if bird.x + bird.r >= 400 or bird.x - bird.r <= 0:
        Change_spikes(bird, spikes_right, spikes_left)

#dend-game function
def Death(bird, spikes_right, spikes_left):
    pass
        
    


    
    
    
