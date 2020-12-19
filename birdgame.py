#birdgame, Python3,
# 18.11.19

import tkinter as tk
import math as m
import random as *

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('300x400')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class bird:
	def __init__(self):
		self.live = 1
		self.color = choice(['pink','blue','green'])
		self.x = x
		self.y = y
		self.vx = 5
		self.vy = 0
		self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color, 
                tag = 'a')