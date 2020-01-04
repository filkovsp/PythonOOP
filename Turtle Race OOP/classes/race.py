if (__name__ == "__main__"):
    raise Exception("This is not the file you should start, you idiot!")

from random import randint
from .tortoise import Tortoise
from .worker import Worker
from .racer import Racer

class Race(object):
    def __init__(self):
        super().__init__()
        self.comspetitors = list()
    
    def addCompetitor(self, competitor:Tortoise=None):
        self.comspetitors.append(competitor)
    
    def prepareRaceField(self):
        worker = Worker()
        worker.markRacingField()
    
    def prepareCompetitors(self):
        self.ada = Racer(color="red", name="Ada")
        self.ada.goto(-160, 100)

        self.bob = Racer(color="blue", name="Bob")
        self.bob.goto(-160, 70)
        
        self.ivy = Racer(color="green", name="Ivy")
        self.ivy.goto(-160, 40)
        
        self.jim = Racer(color="orange", name="Jim")
        self.jim.goto(-160, 10)
    
    def startRace(self):
        for turn in range(100):
            self.ada.forward(randint(1,5))
            self.bob.forward(randint(1,5))
            self.ivy.forward(randint(1,5))
            self.jim.forward(randint(1,5))

    def stopRace(self):
        pass
