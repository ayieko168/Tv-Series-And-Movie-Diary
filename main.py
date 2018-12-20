from tkinter import *


def main():

    # main tkinter window

    # Tkinter Functions
    def list_movies():

        movie_list.insert(END, " Movies  |    Season  |   Episode  ")

        for item in ["one", "two", "three", "four"]:
            movie_list.insert(END, item)

    mainWindow = Tk()

    # Tkinter variables

    # Widgets

    movie_list = Listbox(mainWindow, bg='grey')
    list_movies()

    # Packing Widgets

    movie_list.grid(sticky=E + W)

    mainWindow.geometry("400x650")
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.mainloop()


main()
