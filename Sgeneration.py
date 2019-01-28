import pygame,pickle,socket
f = open("sizes.txt","r")
g = f.read().split("\n")
f.close()
h = int(g[1]) # Defines the height of the grid
w = int(g[0]) # Defines the width of the grid
if h > w:
    div = h
else:
    div = w
global distance,offset,FP
FP = (0,0)
offset = (0,0)
distance = 4 # 250 divided by the width or height, whichever is larger
class init:
    def __init__(self):
        global cubes,timer,counter
        counter = 0
        timer = 0
        cubes = self
        cubes.distance = 500/div
        cubes.list = []
        generate.create(w,h)
class generate:
    def create(width,height):
        for h in range(height):
            for w in range(width):
                cubes.list.append([w,h,(255,255,255)])
    def draw(window):
        global cubes
        g = cubes.list
        for x in g:
            pygame.draw.rect(window,x[2],[(x[0]*distance+offset[0]),x[1]*distance+offset[1],distance,distance])
    def change(color,spot):
        global cubes
        cubes.list[spot][2] = color
