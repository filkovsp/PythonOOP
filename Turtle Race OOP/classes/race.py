if (__name__ == "__main__"):
    raise Exception("This is not the file you should run, you stupid idiot!")

import random as rnd
from .tortoise import Tortoise
from .worker import Worker
from .racer import Racer

class Race(object):
    def __init__(self) :
        super().__init__()
        self.comspetitors = list()

    def addCompetitor(self, competitor:Tortoise=None):
        self.comspetitors.append(competitor)

    def prepareRaceField(self):
        worker = Worker()
        worker.prepareRacingField()
    
    def prepareCompetitors(self, competitors:dict=None):
        if competitors is None:
            raise Exception("Oh Nooo!!! No one to participate in the racing. Show's been cancelled!")
        
        startigposition = 100
        for name in competitors.keys():
            # print ("Name:{0} - colour:(1)".format (name, competitors[name]))
            competitor = Racer(color=str(competitors[name]).lower(), name=name)
            competitor.goto(-160, startigposition)
            competitor.showOff(rnd.choice([10, 60, 72, 30, 90]))
            self.comspetitors.append(competitor)
            startigposition -= 30

    def startRace(self):
        for turn in range(100):
            for comspetitor in self.comspetitors:
                comspetitor.moveForward(rnd.randint(1,5))
    
    def checkwinner(self):
        pass