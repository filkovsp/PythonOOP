from classes.race import Race
import tkinter as tk

if (__name__ == "__main__"):
    race = Race()
    race.prepareRaceField()
    race.prepareCompetitors()
    race.startRace()
    tk.mainloop()