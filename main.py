from tkinter import *
import os
import movies


width = 450
height = 650


def main():

    # main tkinter window

    # Tkinter Functions
    def list_movies():

        movie_list.insert(END, " # | Name  |    Season  |   Episode  ")
        movie_list.insert(END, "=====================================")

        for name, val in movies.series_dict.items():
            movie_list.insert(END, name)
            x = movie_list.index
            print(x)
            print(name)
            print(val)

    mainWindow = Tk()

    # Tkinter variables

    # Widgets

    movie_list = Listbox(mainWindow, bg='white', bd=3, relief=SUNKEN, width=30)
    list_movies()

    preview_box = Text(mainWindow, width=17, height=20)

    # Packing Widgets

    movie_list.pack(side=RIGHT, fill=Y, anchor=SW, padx=10, pady=30)
    preview_box.pack(side=LEFT, padx=10, pady=20)

    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.mainloop()


main()
