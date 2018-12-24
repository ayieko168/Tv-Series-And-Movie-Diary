from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import json
import main


pat = 'thumbnails/'


def add_ui():

    def add():
        """ callback function called when add button is clicked """

        movie_title = str(movie_titleent.get()).title()
        season = int(seasoncom.get())
        episode = int(episodecom.get())
        pic = str(add_picent.get())

        print('movie_title = ', movie_title)
        print('season : ', season)
        print('episode : ', episode)
        print('pic : ', pic)

        if (len(movie_title) != 0) and (len(str(episode)) != 0) and (len(str(season)) != 0):
            """check if all the important info is given"""

            with open('series_table.json', 'r') as f:  # get the current list of data from the series json file
                series_dict = json.load(f)

            if movie_title in series_dict:
                '''check if the added title is in the database'''
                choise = messagebox.askquestion('QUESTION', 'The title {} already exists in your list,\nDo you want to update it instead'.format(movie_title.upper()))
                print(choise)
                if choise == 'yes':
                    print('updating')
                    series_dict[movie_title] = [season, episode, pat+pic]  # add the users entry
                    messagebox.showinfo('RE RUN NEEDED',
                                        'IN ORDER FOR THE NEW ENTRY TO BE \n'
                                        'UPDATED YOU NEED TO RESTART THE APP ')
                else:
                    print('skipping')
                    pass
            else:
                series_dict[movie_title] = [season, episode, pat + pic]  # add the users entry
                messagebox.showinfo('RE RUN NEEDED',
                                    'IN ORDER FOR THE NEW ENTRY TO BE \n'
                                    'UPDATED YOU NEED TO RESTART THE APP ')

            with open('series_table.json', 'w') as f:  # append the entry to the json file
                json.dump(series_dict, f, indent=4)

        add_window.destroy()

    def browse_pics():
        """ clallback function called when brouswe button is clicked """

        pic_path = filedialog.askopenfilename(filetypes=(("GIF files", "*.gif"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")))

        pic_name = os.path.split(pic_path)[-1]

        add_picent.delete(0, END)  # clear entry and insert the selected picture
        add_picent.insert(0, pic_name)

    add_window = Toplevel()  # change to top view

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

    add_window.geometry('400x200+500+300')
    add_window.config(bg='white')
    add_window.title('ADD MOVIES')
#     add_window.mainloop()
#
# add_ui()


