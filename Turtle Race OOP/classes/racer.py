if (__name__ == "__main__"):
    raise Exception("This is not the file you should start, you idiot!")

from .tortoise import Tortoise

class Racer (Tortoise):
    def __init__(self, color:str=None, name:str=None):
        super().__init__()
        self.setColour(color)
        self.shape("turtle")
        self.name = name


