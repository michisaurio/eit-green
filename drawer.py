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
        img = Image.open("car.png")
        tkimage = ImageTk.PhotoImage(img.rotate(self.angle))
        canvas_obj = self.canvas.create_image(
            250, 250, image=tkimage)
        self.tk.after_idle(self.update)
        yield
        self.canvas.delete(canvas_obj)
        self.angle += 10
        self.angle %= 360

        pass #Draw all things
drawer = Drawer()
drawer.draw()
drawer.tk.mainloop()