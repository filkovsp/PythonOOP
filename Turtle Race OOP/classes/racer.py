if (__name__ == "__main__"):
    raise Exception("This is not the file you should run, you stupid idiot!")

from .tortoise import Tortoise
import random as rnd

class Racer (Tortoise):
    def __init__(self, color:str=None, name:str="Anonymus"):
        super().__init__()
        self.setColour(color)
        self.setShape("turtle")
        self.setSpeed(3)
        self.name = name
        self.listeners = list()

    def showOff(self, angle:int=0):
        if angle > 0:
            turns = int(360 / angle)
            if (rnd.random() > 0.5):
                for turn in range(turns):
                    self.right(angle)
            else:
                for turn in range(turns):
                    self.left(angle)
        else:
            pass
    
    def moveForward(self, steps:int=1):
        self.forward(steps)