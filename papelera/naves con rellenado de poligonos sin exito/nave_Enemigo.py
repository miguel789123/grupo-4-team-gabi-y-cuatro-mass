from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image, ImageDraw
from pygame.locals import *
import math
import random as rdn
import numpy as np
def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	pygame.display.flip()
	# print("{}\t{}".format(x, y))
	pygame.time.wait(1)

def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , 
						GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)

def DDA(x0, y0, x1, y1, r, g, b, size):
	points = []
	dx = x1 - x0
	dy = y1 - y0

	x = x0
	y = y0

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi = dx / steps
	yi = dy / steps

	set_pixel(round(x), round(y), r, g, b, size)
	points.append((round(x), round(y)))
	for k in range(int(steps)):
		x += xi
		y += yi
		set_pixel(round(x), round(y), r, g, b, size)
		points.append((round(x), round(y)))
    

	return points
  
  

def DrawPolygon_(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(0,len(vertices) - 1,2):
		# print(vertices[k])
		x0, y0 = vertices[k][:2]
		x1, y1 = vertices[k + 1][:2]
		DDA(x0, y0, x1, y1, r, g, b, size)
    
	vertices.pop()
### Draw
### Draw
def display_openGL(width, height, scale):
	#pygame.display.set_mode((width, height), pygame.OPENGL)
	window = pygame.display.set_mode((width, height), pygame.OPENGL)
	


	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)
	

def main():
        scale = 3
        width, height = scale * 200, scale * 200

        pygame.init()
        pygame.display.set_caption('C.G. I')

        display_openGL(width, height, scale)
        
        
        
        x = 0
        y = 0
        set_pixel(x, y, 255/255, 255/255, 255/255, scale)       

        vertices_p1 = [[-8, 0, 1], [-8, 20, 1],[-7, 0, 1], [-7,20,1],
                       [-6, 0, 1], [-6,20,1],[-5, 0, 1], [-5,20,1],
                       [-4, 0, 1], [-4,20,1],[-3, 0, 1], [-3,20,1],
                       [-2, 0, 1], [-2,20,1], [-1, 0, 1], [-1,20,1],
                       [0, 0, 1], [0,20,1],[1, 0, 1], [1,20,1],
                       [2, 0, 1], [2,20,1],[3, 0, 1], [3,20,1],
                       [4, 0, 1], [4,20,1],[5, 0, 1], [5,20,1],
                       [6, 0, 1], [6,20,1],[7, 0, 1], [7,20,1],
                       [8, 0, 1], [8,20,1]]
        DrawPolygon_(vertices_p1, 255/255, 255/255, 0/255, scale)
        vertices_p2 = [[-6, -7, 1], [6, -7, 1],[-6, -6, 1], [6,-6,1],
                       [-6, -5, 1], [6, -5, 1],[-6, -4, 1], [6,-4,1],
                       [-6, -3, 1], [6, -3, 1],[-6, -2, 1], [6,-2,1],
                       [-6, -1, 1], [6,-1,1],[-6, -8, 1], [6,-8,1],[-6, -9, 1], [6,-9,1],[-6, -10, 1], [6,-10,1],[-6, -11, 1], [6,-11,1],[-6, -12, 1], [6,-12,1]]
        DrawPolygon_(vertices_p2, 128/255, 128/255,128/255, scale)
        vertices_p3 = [[-16, 0, 1], [-16, 20, 1],[16, 0, 1], [16,20,1],
                       [-15, 0, 1], [-15,20,1],[15, 0, 1], [15,20,1],
                       [-14, 0, 1], [-14,20,1],[14, 0, 1], [14,20,1],
                       [-13, 0, 1], [-13,20,1], [13, 0, 1], [13,20,1],
                       [-12, 0, 1], [-12, 20, 1],[12, 0, 1], [12,20,1],
                       [-11, 0, 1], [-11,20,1],[11, 0, 1], [11,20,1],
                       [-10, 0, 1], [-10,20,1],[10, 0, 1], [10,20,1],
                       [-9, 0, 1], [-9,20,1], [9, 0, 1], [9,20,1],[-17, 0, 1], [-17, 20, 1],[17, 0, 1], [17,20,1],
                       [-18, 0, 1], [-18,20,1],[19, 0, 1], [19,20,1],
                       [-20, 0, 1], [-20,20,1],[20, 0, 1], [20,20,1],
                       [-21, 0, 1], [-21,20,1], [21, 0, 1], [21,20,1],
                       [-22, 0, 1], [-22, 20, 1],[22, 0, 1], [22,20,1],
                       [-23, 0, 1], [-23,20,1],[23, 0, 1], [23,20,1],
                       [-24, 0, 1], [-24,20,1],[24, 0, 1], [24,20,1],
                       [-25, 0, 1], [-25,20,1], [25, 0, 1], [25,20,1]]
                       
        DrawPolygon_(vertices_p3, 128/255, 128/255, 128/255, scale)
        vertices_p4 = [[-8, 21, 1], [-8, 35, 1],[-7, 21, 1], [-7,35,1],
                       [-6, 21, 1], [-6,35,1],[-5, 21, 1], [-5,35,1],
                       [-4, 21, 1], [-4,35,1],[-3, 21, 1], [-3,35,1],
                       [-2, 21, 1], [-2,35,1], [-1, 21, 1], [-1,35,1],
                       [0, 21, 1], [0,35,1],[1,21, 1], [1,35,1],
                       [2, 21, 1], [2,35,1],[3,21, 1], [3,35,1],
                       [4, 21, 1], [4,35,1],[5,21, 1], [5,35,1],
                       [6, 21, 1], [6,35,1],[7,21, 1], [7,35,1],
                       [8, 21, 1], [8,35,1]]
        DrawPolygon_(vertices_p4, 128/255, 128/255, 128/255, scale)
        vertices_p5=[[-25,0,1],[-25,-20,1],[-26,0,1],[-26,-20,1],[-27,0,1],[-27,-20,1],[-28,0,1],[-28,-20,1],[-29,0,1],[-29,-20,1],[-30,0,1],[-30,-20,1],[-31,0,1],[-31,-20,1],[-32,0,1],[-32,-20,1],[-33,0,1],[-33,-20,1],[-34,0,1],[-34,-20,1],[-35,0,1],[-35,-20,1],[-36,0,1],[-36,-20,1],[-37,0,1],[-37,-20,1],[-38,0,1],[-38,-20,1],[-39,0,1],[-39,-20,1],[-40,0,1],[-40,-20,1]]
        DrawPolygon_(vertices_p5, 128/255, 128/255, 128/255, scale)
        vertices_p6=[[25,0,1],[25,-20,1],[26,0,1],[26,-20,1],[27,0,1],[27,-20,1],[28,0,1],[28,-20,1],[29,0,1],[29,-20,1],[30,0,1],[30,-20,1],[31,0,1],[31,-20,1],[32,0,1],[32,-20,1],[33,0,1],[33,-20,1],[34,0,1],[34,-20,1],[35,0,1],[35,-20,1],[36,0,1],[36,-20,1],[37,0,1],[37,-20,1],[38,0,1],[38,-20,1],[39,0,1],[39,-20,1],[40,0,1],[40,-20,1]]
        DrawPolygon_(vertices_p6, 128/255, 128/255, 128/255, scale)        
        
           

        
      
        
if __name__ == '__main__':
        main()
