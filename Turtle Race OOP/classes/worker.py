if (__name__ == "__main__"):
    raise Exception("This is not the file you should run, you stupid idiot!")

from .tortoise import Tortoise

class Worker (Tortoise):
    def __init__(self) :
        super ().__init__()
        self.setColour("black")
        self.setShape("turtle")
        self.setSpeed(0)
        self.setPenSize(0)
    
    def prepareRacingField(self):
        self.penup()
        self.goto(-140, 140)
        
        for step in range(15):
            self.write(step, align='center')
            self.right(90)
            for i in range(8):
                self.forward(10)
                self.pendown()
                self.forward(10)
                self.penup()
            
            self.backward(160)
            self.left(90)
            self.forward(20)
        
        self.right(90)