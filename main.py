from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import imageProcessor
import add_movie

width = 550
height = 650

with open('series_table.json') as f:  # initial reading of json data for series
    data = json.load(f)

series_dict = data


def main():

        # main tkinter window

    # Tkinter Functions
    def list_movies(lis):

        for k, v in sorted(lis.items()):
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
        """callback function for the treeview double click event"""
        curItem = treeview.focus()
        preview_box.window_create(index=1.0, window=Label(preview_box, text='', bg="white"))  # clear the preview box

        try:
            select_values = series_dict[curItem]
        except KeyError:
            try:
                select_values = series_dict[curItem.strip('#').strip()]
            except KeyError:
                messagebox.showinfo('INFO...', ' TRY AND SELECT A VALID OPTION ')

        # print(treeview.item(curItem))

        try:
            try:
                img = imageProcessor.convert_format(select_values[2])
                img = imageProcessor.resize_image(img)
                image = PhotoImage(file=img)
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
            except AttributeError:
                preview_box.delete(0.1, END)
                preview_box.window_create(index=1.0, window=Label(preview_box, text='No Preview '))
        except Exception:
            pass

    def selectitem_options(event):

        def delete():

            curitem = treeview.focus()
            print("deleting : ", curitem)

        def edit():

            curitem = treeview.focus().strip("#")
            select_values = series_dict[curitem]

            print(select_values)

            if curitem != "":
                edittop = Toplevel()

                editlab1 = Label(edittop, text="Current Tv-Series title : ")
                editlab1.grid(row=1, column=1, sticky=W)

                editent = Entry(edittop, textvariable=editentvar)
                editentvar.set(curitem)
                editent.grid(row=1, column=2, sticky=W)

                editlab2 = Label(edittop, text="Current Season {}, chance to : ".format(select_values[0]))
                editlab2.grid(row=2, column=1, sticky=W)

                editspin1 = Spinbox(edittop, from_=1, to=1000, width=5)
                editspin1.grid(row=2, column=2, sticky=W)

                editlab3 = Label(edittop, text="Current Episode {}, change to : ".format(select_values[1]))
                editlab3.grid(row=3, column=1, sticky=W)

                editspin2 = Spinbox(edittop, from_=1, to=1000, width=5)
                editspin2.grid(row=3, column=2, sticky=W)

                editlab4 = Label(edittop, text="Current image \"{}\", change to : ".format(select_values[2].split('/')[-1]))
                editlab4.grid(row=4, column=1, sticky=W)

                editent2 = Entry(edittop, textvariable=editent2var)
                editent2.grid(row=5, column=1, sticky=E)

                edittop.geometry("550x200+200+300")
                edittop.title("Edit properties of {} ".format(curitem).upper())

        popup_menu = Menu()

        popup_menu.add_command(label='Delete', command=delete)
        popup_menu.add_command(label='Edit', command=edit)


        popup_menu.post(event.x_root, event.y_root)

    def updatelist():

        pass


    mainWindow = Tk()

    screen_height = mainWindow.winfo_screenheight()
    screen_width = mainWindow.winfo_screenwidth()

    # Tkinter Variables
    searchentvar = StringVar()
    searchentvar.set('Search')
    searchimage = PhotoImage(file='thumbnails/search_ico.gif').subsample(15, 15)
    editentvar = StringVar()
    editent2var = StringVar()
    editent2var.set("image")

    # tkinter main menu bar

    menubar = Menu(mainWindow)

    filemenu = Menu(tearoff=0)
    filemenu.add_command(label='Exit', command=lambda: mainWindow.destroy())

    options_menu = Menu(tearoff=0)
    options_menu.add_command(label='update list', command=updatelist)

    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Options', menu=options_menu)

    # Widgets

    treeview = ttk.Treeview(mainWindow)
    tree_configure()
    list_movies(series_dict)
    treeview.bind('<Double-Button-1>', selectitem)
    treeview.bind('<Button-2>', selectitem_options)

    previewlb = LabelFrame(mainWindow, text=' PREVIEW ', bd=3, font='bold 11')
    preview_box = Text(previewlb, width=30, height=20, selectbackground='white', relief=SUNKEN,
                       bd=3, state='disabled')

    searchent = Entry(mainWindow, textvariable=searchentvar, width=28, font='italic 11')
    searchbut = Button(mainWindow, image=searchimage, relief=GROOVE, bd=3)

    addbut = Button(mainWindow, text=' ADD NEW ENTRY ', font='System 12 bold', command=add_movie.add_ui)


    # Packing Widgets

    previewlb.pack(side=LEFT, anchor=S, pady=20, padx=2)
    preview_box.pack(side=LEFT, padx=5, pady=5, anchor=S)
    treeview.pack(side=RIGHT, fill=Y)

    searchent.place(x=10, y=40)
    searchbut.place(x=242, y=40)

    addbut.place(x=65, y=115)

    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.config(menu=menubar)
    mainWindow.resizable(FALSE, FALSE)
    mainWindow.mainloop()


if __name__ == '__main__':
    main()
