import pygame
import bird
import spike
import random

pygame.init()

#Check if bird hits spike
def Hittest(bird, spikes_up, spikes_down, spikes_right, spikes_left):
    for i in range (len(spikes_up)):
        if spikes_up[i].work == True:
            if (spikes_up[i].x - bird.x)**2 + (spikes_up[i].y - bird.y)**2 <= bird.r**2:
                bird.live = 0
    for i in range (len(spikes_down)):
        if spikes_down[i].work == True:
            if (spikes_down[i].x - bird.x)**2 + (spikes_down[i].y - bird.y)**2 <= bird.r**2:
                bird.live = 0
    for i in range (len(spikes_right)):
        if spikes_right[i].work == True:
            if (spikes_right[i].x - bird.x)**2 + (spikes_right[i].y - bird.y)**2 <= bird.r**2:
                bird.live = 0
    for i in range (len(spikes_left)):
        if spikes_left[i].work == True:
            if (spikes_left[i].x - bird.x)**2 + (spikes_left[i].y - bird.y)**2 <= bird.r**2:
                bird.live = 0
    
            
#New spikes appear (when bird changes its orientation)
def Change_spikes(bird, spikes_right, spikes_left, score):
    Need_L = []
    if bird.orient == 1:
        Choice(score, spikes_right, Need_L)            
        for i in range (len(Need_L)):
            j = Need_L[i]
            spikes_right[j].work = True
        for i in range (len(spikes_left)):
            spikes_left[i].work = False
    if bird.orient == -1:
        Choice(score, spikes_left, Need_L)            
        for i in range (len(Need_L)):
            j = Need_L[i]
            spikes_left[j].work = True
        for i in range (len(spikes_right)):
            spikes_right[i].work = False

#Check if bird hits wall 
def Check_wall_hit(bird, spikes_right, spikes_left, score, Dead):
    if Dead == []:
        if bird.x + bird.r >= 400 or bird.x - bird.r <= 0:
            score.append(1)
            Change_spikes(bird, spikes_right, spikes_left, score)
        
#Create list of spike's numbers
def Choice(score, list_spikes, Need_L):
    LS = []
    for i in range (len(list_spikes)):
        LS.append(i)
    random.shuffle(LS)
    if (len(score)//5 + 1) <= (len(list_spikes) - 5):
        for i in range (len(score)//5 + 1):
            Need_L.append(LS[i])
    else:
        for i in range (len(list_spikes) - 5):
            Need_L.append(LS[i])

#When bird dies, it must stop
def Death(bird, Dead):
    if bird.live == 0:
        bird.vx = 0
        bird.vy = 0
        Dead.append(1)



    
    


    
    
    
