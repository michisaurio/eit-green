from tkinter import *
from PIL import ImageTk, Image

class Drawer:

    def __init__(self):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()
        self.angle = 0


    def drawCar(self, position, rotation):
        pass #Add a car with correct rotation to the canvas

    def draw(self):
        pass #Draw all things