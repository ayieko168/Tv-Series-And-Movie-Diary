from tkinter import *
from tkinter import filedialog
import os
import json

def add_ui():

    def add():

        movie_title = movie_titleent.get()
        season = seasoncom.get()
        episode = episodecom.get()
        pic = add_picent.get()

        print('movie_title = ', movie_title)
        print('season : ', season)
        print('episode : ', episode)
        print('pic : ', pic)

        # add_window.destroy()

    def browse_pics():

        pic_path = filedialog.askopenfilename(filetypes=(("GIF files", "*.gif"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")))

        pic_name = os.path.split(pic_path)[-1]

        print(pic_name)


    add_window = Tk()  # cange to top view

    add_title = Label(add_window, text=' Add a new Movie or Movie entry'.upper(), bg='white', anchor=CENTER)
    add_title.place(x=90, y=10)

    movie_titlelb = Label(add_window, text='Movie Title : '.upper(), bg='white', anchor=CENTER)
    movie_titlelb.place(x=10, y=30)

    movie_titleent = Entry(add_window, bg='white', width=35)
    movie_titleent.place(x=100, y=30)

    seasonlb = Label(add_window, text=' Season : '.upper(), bg='white', anchor=CENTER)
    seasonlb.place(x=10, y=60)

    seasoncom = Spinbox(add_window, bg='white', from_=1, to=1000)
    seasoncom.place(x=100, y=60)

    episodelb = Label(add_window, text=' Episode : '.upper(), bg='white', anchor=CENTER)
    episodelb.place(x=10, y=90)

    episodecom = Spinbox(add_window, bg='white', from_=1, to=1000)
    episodecom.place(x=100, y=90)

    add_piclb = Label(add_window, text=' Add a preview pic :'.upper(), bg='white', anchor=CENTER)
    add_piclb.place(x=10, y=120)

    add_picent = Entry(add_window, text='file path'.upper(), bg='white', width=30)
    add_picent.place(x=130, y=120)

    browsebut = Button(add_window, bg='white', text='browse', anchor=CENTER, command=browse_pics)
    browsebut.place(x=320, y=120, height=22)

    addbut = Button(add_window, bg='white', text='add'.upper(), command=add)
    addbut.place(x=150, y=150)

    add_window.geometry('400x200')
    add_window.config(bg='white')
    add_window.title('ADD MOVIES')
    add_window.mainloop()

add_ui()


