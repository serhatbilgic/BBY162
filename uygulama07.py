from tkinter import *
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

pencere = Tk()
pencere.geometry("900x600+150+50")
pencere.title("Fotoğraf Albümü")
pencere.configure(background="red")
hosgeldin = Label(text="\n\n\t\t Fotoğraf Albümüne Hoşgeldin! Ama fotoğraf yok:( \t\t\n\n", font="Times 28 bold",
                  fg="yellow", bg="red")
hosgeldin.pack()
mainloop()
