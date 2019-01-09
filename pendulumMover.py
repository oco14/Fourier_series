import pyglet
import math as mt

class Pendulum:

    def __init__(self,pivot,length,width,angle):
       
        #defining variables
        self.pivot_x = pivot[0]
        self.pivot_y = pivot[1]
        self.length = length
        self.width = width
        
        #done in degrees to keep numbers as integer values
        self.angle = angle

        self.setPoints()

    def setPoints(self):
        #center
        self.center_x = int(self.pivot_x + ((self.length / 2) * mt.cos( self.angle * mt.pi / 180)))
        self.center_y = int(self.pivot_y + ((self.length / 2) * mt.sin( self.angle * mt.pi / 180)))

        #end Point difference from pivot
        self.end_diff_x = int( self.length * mt.cos( self.angle * mt.pi / 180))
        self.end_diff_y = int( self.length * mt.sin( self.angle * mt.pi / 180))

        #close point difference from pivot
        self.close_diff_x = int ((self.width/2) * mt.sin( self.angle * mt.pi / 180))
        self.close_diff_y = int ((self.width/2) * mt.cos( self.angle * mt.pi / 180))
        
        
        #pivot corners
        self.inner_x_left  = int(self.pivot_x  - self.close_diff_x)
        self.inner_y_left  = int(self.pivot_y  + self.close_diff_y)
        self.inner_x_right = int(self.pivot_x  + self.close_diff_x)
        self.inner_y_right = int(self.pivot_y  - self.close_diff_y)

        #far conners

        self.bottom_x_left =  int(self.pivot_x + self.end_diff_x  - self.close_diff_x)
        self.bottom_y_left =  int(self.pivot_y + self.end_diff_y  + self.close_diff_y)
        self.bottom_x_right = int(self.pivot_x + self.end_diff_x  + self.close_diff_x)
        self.bottom_y_right = int(self.pivot_y + self.end_diff_y  - self.close_diff_y)

        #print(mt.sin(self.angle * mt.pi / 180),mt.cos(self.angle * mt.pi / 180))
        #print(self.bottom_x_left,self.bottom_y_left)

    def movePendulum(self,angle_change,piviot_change):
        self.angle += angle_change
        self.pivot_x = piviot_change[0]
        self.pivot_y = piviot_change[1]
        self.setPoints()
        

    def draw(self):

        pendulum_coords = (self.center_x,       self.center_y,
                           self.inner_x_left,   self.inner_y_left,
                           self.inner_x_right,  self.inner_y_right,
                           self.bottom_x_left,  self.bottom_y_left,
                           self.bottom_x_right, self.bottom_y_right)
        
        pyglet.graphics.draw_indexed(5,pyglet.gl.GL_TRIANGLES,
                                    [0,1,2,0,3,4,0,1,3,0,2,4],
                                    ('v2i',(pendulum_coords))) 
