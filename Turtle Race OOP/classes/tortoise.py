if (__name__ == "__main__"):
    raise Exception("This is not the file you should run, you stupid idiot!")

import turtle

class Tortoise(turtle.Turtle):
    def __init__(self, color:str=None, speed:int=0, pensize:int=0):
        super ().__init__()
        self.setSpeed(speed)
        self.setPenSize(pensize)
        self.penup()

    def setPenSize(self, pensize:int=0):
        self.pensize(pensize)
    
    def setSpeed(self, speed:int=None):
        self.speed(speed)
    
    def setColour(self, color:str=None):
        self.color(color)
    
    def setShape(self, shape:str=None):
        self.shape(shape)