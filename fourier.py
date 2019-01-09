import pyglet
from pendulumMover import Pendulum
from circle import Circle
from curve import Curve
class Window(pyglet.window.Window):

    def __init__(self):
        super(Window,self).__init__()
        self.set_size(1500,600)
       
        #These are the declarations of the circles to be put in series
        #for the fourier series representaion
        #Here i have them coded in by hand but i could change
        #the code to have a selected amount of circles
        #and pre-defined lengths,rates to create
        #certain curves
        self.pendulum = Pendulum((300,300),150,5,0)
        self.circle = Circle((300,300),100)
        
        self.pendulum2 = Pendulum((self.pendulum.end_diff_x + self.pendulum.pivot_x,
                                   self.pendulum.end_diff_y + self.pendulum.pivot_y),
                                    75,5,0)
        self.circle2 = Circle((self.pendulum2.pivot_x,
                              self.pendulum2.pivot_y),
                              self.pendulum2.length)
        
        self.pendulum3 = Pendulum((self.pendulum2.end_diff_x + self.pendulum2.pivot_x,
                                   self.pendulum2.end_diff_y + self.pendulum2.pivot_y),
                                    50,5,0)
        self.circle3 = Circle((self.pendulum3.pivot_x,
                              self.pendulum3.pivot_y),
                              self.pendulum3.length) 

        self.pendulum4 = Pendulum((self.pendulum3.end_diff_x + self.pendulum3.pivot_x,
                                   self.pendulum3.end_diff_y + self.pendulum3.pivot_y),
                                    25,5,0)
        self.circle4 = Circle((self.pendulum4.pivot_x,
                              self.pendulum4.pivot_y),
                              self.pendulum4.length) 

        self.pendulum5 = Pendulum((self.pendulum4.end_diff_x + self.pendulum4.pivot_x,
                                   self.pendulum4.end_diff_y + self.pendulum4.pivot_y),
                                    12,5,0)
        self.circle5 = Circle((self.pendulum5.pivot_x,
                              self.pendulum5.pivot_y),
                              self.pendulum5.length) 
        
        #the curve resulting from the series
        self.curve = Curve(200)

        pyglet.clock.schedule_interval(self.update,1.0/40)

    def on_draw(self):
        self.clear()
        
        self.pendulum.draw()
        self.circle.draw()
        
        self.pendulum2.draw()
        self.circle2.draw()

        self.pendulum3.draw()
        self.circle3.draw()

        self.pendulum4.draw()
        self.circle4.draw()

        self.pendulum5.draw()
        self.circle5.draw()

        self.curve.draw()
       
    def update(self,dt):
        #3,2,10
        self.pendulum.movePendulum(10,(self.pendulum.pivot_x,self.pendulum.pivot_y))
      
        #9,15,20
        self.pendulum2.movePendulum(20,
                                (self.pendulum.end_diff_x + self.pendulum.pivot_x,
                                 self.pendulum.end_diff_y + self.pendulum.pivot_y))
        self.circle2.set_points((self.pendulum2.pivot_x,
                                 self.pendulum2.pivot_y))

        #15,27,30
        self.pendulum3.movePendulum(30,
                                (self.pendulum2.end_diff_x + self.pendulum2.pivot_x,
                                 self.pendulum2.end_diff_y + self.pendulum2.pivot_y))
        self.circle3.set_points((self.pendulum3.pivot_x,
                                 self.pendulum3.pivot_y))

        #21,39,40
        self.pendulum4.movePendulum(40,
                                (self.pendulum3.end_diff_x + self.pendulum3.pivot_x,
                                 self.pendulum3.end_diff_y + self.pendulum3.pivot_y))
        self.circle4.set_points((self.pendulum4.pivot_x,
                                 self.pendulum4.pivot_y))

        #27,51,50         
        self.pendulum5.movePendulum(50,
                                (self.pendulum4.end_diff_x + self.pendulum4.pivot_x,
                                 self.pendulum4.end_diff_y + self.pendulum4.pivot_y))
        self.circle5.set_points((self.pendulum5.pivot_x,
                                 self.pendulum5.pivot_y))
        
        self.curve.add_to_set(self.pendulum5.pivot_y + self.pendulum5.end_diff_y)

if __name__ == '__main__':
    window = Window()
    pyglet.app.run() 