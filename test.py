from tkinter import *

window = Tk()

canvas = Canvas(width=200, height=200, bg = "red")
canvas.pack()

def changeBlue():
    canvas.config(bg="blue")
    canvas.update()
def changeRed():
    canvas.config(bg="red")
    canvas.update()

window.after(1000, changeBlue)
window.after(1000, changeRed)
    
window.mainloop()