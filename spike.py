class Spike:
    
    def __init__(self, x, y, orient):
        self.x = x
        self.y = y
        self.orient = orient
        
#Draw spike (triangle), (self.x, self.y) - coords of spike's peak
    def draw(self):
        if self.orient = 'up':
            spike = canvas.create_polygon((self.x, self.y), (self.x + 5, self.y - 5),
                                          (self.x - 5, self.y - 5), fill='grey', width=2)
        if self.orient = 'down':
            spike = canvas.create_polygon((self.x, self.y), (self.x + 5, self.y + 5),
                                          (self.x - 5, self.y + 5), fill='grey', width=2)
        if self.orient = 'left':
            spike = canvas.create_polygon((self.x, self.y), (self.x + 5, self.y + 5),
                                          (self.x + 5, self.y - 5), fill='grey', width=2)
        if self.orient = 'right':
            spike = canvas.create_polygon((self.x, self.y), (self.x - 5, self.y + 5),
                                          (self.x - 5, self.y - 5), fill='grey', width=2)

#Spike appears on the wall (when bird knocks into opposite wall)
    def appear(self):
        if self.orient = 'left':
            canvas.move(spike, 5, 0)
        if self.orient = 'right':
            canvas.move(spike, -5, 0)

#Spike disappears on the wall (when bird knocks into it)
    def disappear(self):
        if self.orient = 'left':
            canvas.move(spike, -5, 0)
        if self.orient = 'right':
            canvas.move(spike, 5, 0)
