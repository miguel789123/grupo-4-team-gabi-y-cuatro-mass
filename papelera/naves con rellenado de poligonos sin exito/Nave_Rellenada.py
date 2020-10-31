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


        vertices_p1 = [[-8, 0, 1], [-8, 35, 1],[-7, 0, 1], [-7,35,1],
                       [-6, 0, 1], [-6,35,1],[-5, 0, 1], [-5,35,1],
                       [-4, 0, 1], [-4,35,1],[-3, 0, 1], [-3,35,1],
                       [-2, 0, 1], [-2,35,1], [-1, 0, 1], [-1,35,1],
                       [0, 0, 1], [0,35,1],[1, 0, 1], [1,35,1],
                       [2, 0, 1], [2,35,1],[3, 0, 1], [3,35,1],
                       [4, 0, 1], [4,35,1],[5, 0, 1], [5,35,1],
                       [6, 0, 1], [6,35,1],[7, 0, 1], [7,35,1],
                       [8, 0, 1], [8,35,1]]
        DrawPolygon_(vertices_p1, 255/255, 255/255, 0/255, scale)
        vertices_p2 = [[-8, -7, 1], [8, -7, 1],[-8, -6, 1], [8,-6,1],
                       [-8, -5, 1], [8, -5, 1],[-8, -4, 1], [8,-4,1],
                       [-8, -3, 1], [8, -3, 1],[-8, -2, 1], [8,-2,1],
                       [-8, -1, 1], [8,-1,1]]
        DrawPolygon_(vertices_p2, 128/255, 128/255,128/255, scale)
        vertices_p3 = [[-16, 0, 1], [-16, 35, 1],[16, 0, 1], [16,35,1],
                       [-15, 0, 1], [-15,35,1],[15, 0, 1], [15,35,1],
                       [-14, 0, 1], [-14,35,1],[14, 0, 1], [14,35,1],
                       [-13, 0, 1], [-13,35,1], [13, 0, 1], [13,35,1],
                       [-12, 0, 1], [-12, 35, 1],[12, 0, 1], [12,35,1],
                       [-11, 0, 1], [-11,35,1],[11, 0, 1], [11,35,1],
                       [-10, 0, 1], [-10,35,1],[10, 0, 1], [10,35,1],
                       [-9, 0, 1], [-9,35,1], [9, 0, 1], [9,35,1],
                       [-24, 0, 1], [-24, 17, 1],[24, 0, 1], [24,17,1],
                       [-23, 0, 1], [-23,17,1],[23, 0, 1], [23,17,1],
                       [-22, 0, 1], [-22,17,1],[22, 0, 1], [22,17,1],
                       [-21, 0, 1], [-21,17,1], [21, 0, 1], [21,17,1],
                       [-20, 0, 1], [-20,17, 1],[20, 0, 1], [20,17,1],
                       [-19, 0, 1], [-18,17,1],[19, 0, 1], [19,17,1],
                       [-18, 0, 1], [-18,17,1],[18, 0, 1], [18,17,1],
                       [-17, 0, 1], [-17,17,1], [17, 0, 1], [17,17,1]]
        DrawPolygon_(vertices_p3, 128/255, 128/255, 128/255, scale)
        vertices_p3 = [[-32, 0, 1], [-32, 17, 1],[32, 0, 1], [32,17,1],
                       [-31, 0, 1], [-31,17,1],[31, 0, 1], [31,17,1],
                       [-30, 0, 1], [-30,17,1],[30, 0, 1], [30,17,1],
                       [-29, 0, 1], [-29,17,1], [29, 0, 1], [29,17,1],
                       [-28, 0, 1], [-28,17, 1],[28, 0, 1], [28,17,1],
                       [-27, 0, 1], [-27,17,1],[27, 0, 1], [27,17,1],
                       [-26, 0, 1], [-26,17,1],[26, 0, 1], [26,17,1],
                       [-25, 0, 1], [-25,17,1], [25, 0, 1], [25,17,1]]
        DrawPolygon_(vertices_p3, 255/255, 255/255, 0/255, scale)
        vertices_p4 = [[-8, 36, 1], [-8, 56, 1],[-7, 36, 1], [-7,56,1],
                       [-6, 36, 1], [-6,56,1],[-5, 36, 1], [-5,56,1],
                       [-4, 36, 1], [-4,56,1],[-3, 36, 1], [-3,56,1],
                       [-2, 36, 1], [-2,56,1], [-1, 36, 1], [-1,56,1],
                       [0, 36, 1], [0,56,1],[1,36, 1], [1,56,1],
                       [2, 36, 1], [2,56,1],[3,36, 1], [3,56,1],
                       [4, 36, 1], [4,56,1],[5,36, 1], [5,56,1],
                       [6, 36, 1], [6,56,1],[7,36, 1], [7,56,1],
                       [8, 36, 1], [8,56,1]]
        DrawPolygon_(vertices_p4, 128/255, 128/255, 128/255, scale)        
        
           

        
      
        
if __name__ == '__main__':
        main()
