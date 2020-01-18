"""
	this is the file you should run to start the app.
"""
from classes.race import Race
import tkinter as tk

if (__name__ == "__main__"):
    race = Race()
    race.prepareRaceField ()
    race.prepareCompetitors({"Ada":"red", "Bob":"green", "Ivy":"blue", "Jim":"orange"})
    race.startRace()
    tk.mainloop()