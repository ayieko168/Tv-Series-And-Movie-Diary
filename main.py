from tkinter import *
from tkinter import ttk
import os
import movies


width = 450
height = 650


def main():

    # main tkinter window

    # Tkinter Functions
    def list_movies():

        for k, v in movies.series_dict.items():
            treeview.insert('', END, '#{}'.format(k), text=k)
            treeview.set('#{}'.format(k), 'sn', v[0])
            treeview.set('#{}'.format(k), 'ep', v[1])


    def tree_configure():

        treeview.config(columns=('sn', 'ep'))
        treeview.column('#0', width=150, anchor=CENTER)
        treeview.column('sn', width=60, anchor=CENTER)
        treeview.column('ep', width=60, anchor=CENTER)

        treeview.heading('#0', text='Name')
        treeview.heading('sn', text='Season')
        treeview.heading('ep', text='Episode')

    mainWindow = Tk()

    # Tkinter variables

    # Widgets

    treeview = ttk.Treeview(mainWindow)
    tree_configure()
    list_movies()
    preview_box = Text(mainWindow, width=17, height=20)

    # Packing Widgets

    preview_box.pack(side=LEFT, padx=10, pady=20, anchor=S)
    treeview.pack(side=RIGHT, fill=Y)

    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.mainloop()


main()
