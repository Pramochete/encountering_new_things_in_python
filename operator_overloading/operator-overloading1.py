# However, the good news is that we can teach this to Python through operator overloading. 
# But first, let's get a notion about special functions.

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)

p1=Point(2,3)
p2=Point(2,3)
print(p1+p2)       