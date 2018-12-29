"""import json

di = {'The big bang theory': [2, 10, 'thumbnails/bigbang.gif'], 'Two broke girls': [4, 20, 'thumbnails/2-broke-girls-539.gif'], 'Game of thrones': [7, 6, 'thumbnails/game-of-thrones-481.gif '], 'Breaking Bad': [5, 1, 'thumbnails/breaking-bad-2583.gif '], 'Scorpion': [3, 2, 'thumbnails/scorpion-1111.gif ']}

with open('series_table.json', 'w+') as f:

    json.dump(di, f, indent=2)


"""

try:
    # python 2.x
    import Tkinter as tk
except ImportError:
    # python 3.x
    import tkinter as tk


class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.popupMenu = tk.Menu(self, tearoff=0)
        self.popupMenu.add_command(label="One", command=self.menu_one)
        self.popupMenu.add_command(label="Two", command=self.menu_two)
        self.popupMenu.add_command(label="Three", command=self.menu_three)

        self.bind("<Button-2>", self.popup)

    def menu_one(self):
        print ("one...")

    def menu_two(self):
        print ("two...")

    def menu_three(self):
        print ("three...")

    def popup(self, event):
        self.popupMenu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    root =tk.Tk()
    frame = Example(root, width=200, height=200)
    frame.pack(fill="both", expand=True)
    root.mainloop()



