import math as mt
import pyglet

#creates a circle object with center and a radius
class Circle:
    def __init__(self,pivot,radius):
        self.radius = radius
        self.set_points(pivot)

    #setting the points for the circle   
    def set_points(self,pivot):
        self.pivot_x = pivot[0]
        self.pivot_y = pivot[1]
        self.outerPoints = []
        for angel in range(360):
            xp = int(self.pivot_x + self.radius * mt.cos(angel * mt.pi / 180))
            yp = int(self.pivot_y + self.radius * mt.sin(angel * mt.pi / 180)) 
            self.outerPoints.append((xp,yp))
    
    def draw(self):
        for x in self.outerPoints:
            coords = (x[0],x[1],x[0],x[1])
            pyglet.graphics.draw(2,pyglet.gl.GL_POINTS,
                                        ('v2i',(coords))) 
    