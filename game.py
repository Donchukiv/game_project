import pygame
import bird
import spike
import random
import candy

#colors
WHITE =(255,255,255)
BLACK = (0,0,0) 
GREY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 150, 100)

pygame.init()

#Check if bird hits spike
def Hittest(bird, spikes_up, spikes_down, spikes_right, spikes_left):
    if bird.shape == 1:
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
    if bird.shape == 2:
        for i in range (len(spikes_up)):
            if spikes_up[i].work == True:
                if (bird.y - bird.r) <= spikes_up[i].y and (bird.x - bird.r) <= spikes_up[i].x and spikes_up[i].x <= (bird.x + bird.r):
                    bird.live = 0
        for i in range (len(spikes_down)):
            if spikes_down[i].work == True:
                if (bird.y + bird.r) >= spikes_down[i].y and (bird.x - bird.r) <= spikes_down[i].x and spikes_down[i].x <= (bird.x + bird.r):
                    bird.live = 0
        for i in range (len(spikes_right)):
            if spikes_right[i].work == True:
                if (bird.x + bird.r) >= spikes_right[i].x and (bird.y - bird.r) <= spikes_right[i].y and spikes_right[i].y <= (bird.y + bird.r):
                    bird.live = 0
        for i in range (len(spikes_left)):
            if spikes_left[i].work == True:
                if (bird.x - bird.r) <= spikes_left[i].x and (bird.y - bird.r) <= spikes_left[i].y and spikes_left[i].y <= (bird.y + bird.r):
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

#Put score on the screen
def Show_score(score, candyscore, sc):
    text_s = str(len(score))
    text_c = 'You\'ve collected ' + str(len(candyscore)) + ' candies!'
    surf = pygame.Surface((250, 280))
    surf.fill((255, 255, 255))
    surf.set_alpha(220)

    text_font = pygame.font.SysFont('arial', 300) 
    title = text_font.render(text_s, 1, (0, 0, 0))

    text_font_c = pygame.font.SysFont('arial', 30) 
    title_c = text_font_c.render(text_c, 1, (255, 0, 0))

    place_t = title.get_rect(center=(200, 250))
    place_s = surf.get_rect(center=(200, 250))
    place_c = title_c.get_rect(center=(200, 420))

    sc.blit(title, place_t)
    sc.blit(title_c, place_c)
    sc.blit(surf, place_s)
    
#Check if bird hits candy
def Hit_candy(candy, bird, candyscore):
    if bird.shape == 1:
        if (candy.x - bird.x)**2 + (candy.y - bird.y)**2 <= (bird.r + candy.r)**2:
            candyscore.append(1)
            candy.live = 0

    if bird.shape == 2:
        if candy.x <= bird.x + bird.r and candy.x >= bird.x - bird.r and candy.y <= bird.y + bird.r and candy.y >= bird.y - bird.r:
            candyscore.append(1)
            candy.live = 0

#Generates parametres of new candy
def New_candy():
    global cx, cy, ccolor, clive
    cx = random.randint(60, 340)
    cy = random.randint(60, 440)
    ccolor = random.choice([LIGHT_BLUE, GREEN, YELLOW, PINK, ORANGE])
    clive = 1

#Creates new candy
def Plus_candy(candy):
    global cx, cy, ccolor, clive
    if candy.live == 0:
        New_candy()
        candy.x = cx
        candy.y = cy
        candy.color = ccolor
        candy.live = 1


    
    
    
