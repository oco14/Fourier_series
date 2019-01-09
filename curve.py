import pyglet

#creates a curve object for use in drawing the curve
#resulting from the fourier series
class Curve:
    
    def __init__(self,size_limit):
        self.set = []
        self.size_lim = size_limit

    #since there is a size limit, i added this method
    #to make sure the list doesn't grow to large
    def add_to_set(self,point):
        if len(self.set) >= self.size_lim:
           del  self.set[-1]
            #print(1)
        self.set.insert(0,point)
        #print(len(self.set))

    def draw(self):
        for count,point in enumerate(self.set):
            if not len(self.set) == 1 and not count == len(self.set) - 1:        
                coords = (600 + count*5, point,
                         600 + (count+1)*5, self.set[count+1])
                pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
                                            ('v2i',(coords))) 