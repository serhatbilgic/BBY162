import tkinter as tk
import random
class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=600, width=616, bg="gray")
        self.canvas.pack()
        self.dark = {"k": "cyan", "s": "forest green", "y": "gold1", "m": "darkslategray"}
        self.light = {"k": "white", "s": "white", "y": "white", "m": "white"}

        self.squares = {"k": self.canvas.create_rectangle(0, 0, 200, 200, fill="cyan", outline="cyan"),
                        "s": self.canvas.create_rectangle(200, 0, 400, 200, fill="forest green",
                                                          outline="forest green"),
                        "y": self.canvas.create_rectangle(0, 200, 200, 400, fill="gold1",
                                                          outline="gold1"),
                        "m": self.canvas.create_rectangle(200, 200, 400, 400, fill="darkslategray",
                                                          outline="darkslategray")}

        self.ids = {v: k for k, v in self.squares.items()}
        self.high_score = 0
        self.status = tk.Label(root, text="Simon's Game Ramadan Version v1.4!\nİyi Eğlenceler <3", font="verdana 12 bold", fg="maroon", bg="orange")
        self.status.pack()
        self.parent.bind("<h>", self.score)
        self.draw_board()

    def draw_board(self):
        self.pattern = random.choice("ksym")
        self.selections = ""
        self.parent.after(1000, self.animate)

    def animate(self, idx=0):
        c = self.pattern[idx]
        self.canvas.itemconfig(self.squares[c], fill=self.light[c], outline=self.light[c])
        self.parent.after(500, lambda: self.canvas.itemconfig(self.squares[c], fill=self.dark[c],
                                                              outline=self.dark[c]))

        idx += 1
        if idx < len(self.pattern):
            self.parent.after(1000, lambda: self.animate(idx))
        else:
            self.canvas.bind("<1>", self.select)

    def select(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        color = self.ids[id]
        self.selections += color
        self.canvas.itemconfig(id, fill=self.light[color], outline=self.light[color])
        self.parent.after(800,
                          lambda: self.canvas.itemconfig(id, fill=self.dark[color], outline=self.dark[color]))

        if self.pattern == self.selections:
            self.canvas.unbind("<1>")
            self.status.config(text="DEVAM ET!")
            self.parent.after(2000, lambda: self.status.config(text=""))
            self.pattern += random.choice("ksym")
            self.selections = ""
            self.high_score = max(self.high_score, len(self.pattern))
            self.parent.after(2000, self.animate)
        elif self.pattern[len(self.selections) - 1] != color:  # yanlış şeye tıklayınca
            self.canvas.unbind("<1>")
            self.status.config(text="TEKRAR DENE!")
            self.parent.after(2000, lambda: self.status.config(text=""))
            self.parent.after(2000, self.draw_board)

    def score(self, event=None):
        self.status.config(text=self.high_score)
        self.parent.after(2000, lambda: self.status.config(text=""))


root = tk.Tk()
simon = Simon(root)
root.mainloop()
