from tkinter import *
from tkinter import ttk
import os
import movies
import imageProcessor


width = 550
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

    def selectitem(a):
        curItem = treeview.focus()
        preview_box.window_create(index=1.0, window=Label(preview_box, text=''))  # clear the preview box

        try:
            select_values = movies.series_dict[curItem]
        except KeyError:
            select_values = movies.series_dict[curItem.strip('#')]
        except Exception as e:
            print("ERROR {} ".format(e))

        # print(treeview.item(curItem))

        try:
            img = imageProcessor.convert_format(select_values[2])
            img = imageProcessor.resize_image(img)
            image = PhotoImage(file=img)
            Label.image = image
            preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
        except AttributeError:
            preview_box.delete(0.1, END)
            preview_box.window_create(index=1.0, window=Label(preview_box, text='No Preview '))

    mainWindow = Tk()

    # Tkinter variables
    searchentvar = StringVar()
    searchentvar.set('Search')
    searchimage = PhotoImage(file='search_ico.gif').subsample(15, 15)

    # Widgets

    treeview = ttk.Treeview(mainWindow)
    tree_configure()
    list_movies()
    treeview.bind('<Double-Button-1>', selectitem)

    previewlb = LabelFrame(mainWindow, text=' PREVIEW ', bd=3, font='bold 11')
    preview_box = Text(previewlb, width=30, height=20, selectbackground='white', relief=SUNKEN,
                       bd=3)

    searchent = Entry(mainWindow, textvariable=searchentvar, width=28, font='italic 11')
    searchbut = Button(mainWindow, image=searchimage, relief=GROOVE, bd=3)

    addbut = Button(mainWindow, text=' ADD NEW ENTRY ', font='System 12 bold')


    # Packing Widgets

    previewlb.pack(side=LEFT, anchor=S, pady=20, padx=2)
    preview_box.pack(side=LEFT, padx=5, pady=5, anchor=S)
    treeview.pack(side=RIGHT, fill=Y)

    searchent.place(x=10, y=40)
    searchbut.place(x=242, y=40)

    addbut.place(x=65, y=115)

    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.resizable(FALSE, FALSE)
    mainWindow.mainloop()


if __name__ == '__main__':
    main()
