if (__name__ == "__main__"):
    raise Exception("This is not the file you should start, you idiot!")

from .tortoise import Tortoise

class Worker (Tortoise):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.shapesize(0.1,0.1)
        self.setShape("circle")
        self.setColour("black")
        self.setSpeed(3)
        self.setPenSize(0)

    def markRacingField(self):
        self.setSpeed(0)
        self.penup()
        self.goto(-140, 140)

        for step in range(15):
            self.write(step, align='center')
            self.right(90)
            for num in range(8):
                self.forward(10)
                self.pendown()
                self.forward(10)
                self.penup()
            self.backward(160)
            self.left(90)
            self.forward(20)
