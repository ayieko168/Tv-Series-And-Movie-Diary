from tkinter import *
from tkinter import ttk
import json
import sys
import webbrowser
import datetime
from PIL import Image, ImageTk
import shutil
import requests
import imageProcessor
import os
import add_movie
import gitup
import LogIn

operating_system = sys.platform

width = 550
height = 650

print('starting...')
try:
    with open('series_table.json') as f:  # initial reading of json data for series
        data = json.load(f)
except FileNotFoundError:
    with open("series_table.json", "w") as f:
        json.dump({}, f, indent=2)
    with open('series_table.json') as f:  # initial reading of json data for series
        data = json.load(f)

series_dict = data


def main():

    print('starting within')
    with open('series_table.json') as f:  # initial reading of json data for series
        series_dict = json.load(f)
    # with open("details.json", "r") as f:
    #     details_data = json.load(f)
    #
    # gitup.signin(details_data["use"], checker.decoder(details_data["pas"]))

    global mainWindow, treeview

    # main tkinter window

    # Tkinter Functions
    def list_movies(lis):

        try:
            for k, v in sorted(lis.items()):
                treeview.insert('', END, '#{}'.format(k), text=k)
                treeview.set('#{}'.format(k), 'sn', v[0])
                treeview.set('#{}'.format(k), 'ep', v[1])

        except Exception as e:
            pass

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
        try:
            curItem = treeview.focus().strip('#')
            name = "-".join(curItem.lower().split())

            local_image_path = series_dict[curItem][2]

            if jep.get() == 0:  # online thumbs is false
                try:
                    """ 1st try to load image from local thumbs directory """
                    # image = ImageTk.PhotoImage(Image.open(imageProcessor.resize_image("thumbnails/Shadow-Guy-Shrugging.jpg")))
                    image = ImageTk.PhotoImage(Image.open(imageProcessor.resize_image(local_image_path)))
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except Exception as e1:
                    print(type(e1), e1)
                    if str(type(e1)) == "<class 'PermissionError'>":
                        image = ImageTk.PhotoImage(Image.open("thumbnails/Shadow-Guy-Shrugging.jpg"))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                    elif str(type(e1)) == "<class 'FileNotFoundError'>":
                        image = ImageTk.PhotoImage(
                            Image.open(imageProcessor.resize_image("thumbnails/exclamation.jpg")))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
            else:  # if online thumbs is true
                curItem = treeview.focus().strip('#')
                with open("images_url_dict.json", "r") as f:
                    imgs_dict = json.load(f)

                name = "-".join(curItem.lower().split())
                img_list = imgs_dict[name]
                img_url = img_list[0]
                try:
                    """try to make temp file"""
                    os.mkdir("/Windows/Temp/tv_series_temp_thumbs")
                    try:
                        """try to load image without downloding"""
                        image = ImageTk.PhotoImage(Image.open(
                            imageProcessor.resize_image("/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name))))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                    except FileNotFoundError:
                        r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                        if r.status_code == 200:
                            with open(imageProcessor.resize_image(imageProcessor.resize_image(
                                    "/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name))), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                        print("Done downloading")

                        image = ImageTk.PhotoImage(Image.open(
                            imageProcessor.resize_image("/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name))))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except FileExistsError:
                    """if dir already available"""
                    try:
                        image = ImageTk.PhotoImage(Image.open(
                            imageProcessor.resize_image("/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name))))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                    except FileNotFoundError:
                        r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                        if r.status_code == 200:
                            with open(imageProcessor.resize_image(
                                    "/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name)), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                        print("Done downloading")

                        image = ImageTk.PhotoImage(
                            Image.open("/Windows/Temp/tv_series_temp_thumbs/{}.jpg".format(name)))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
        except Exception as e:
            print("nothing to show...")

    def selectitem_options(event):
        """call back function when right click on an item"""
        curItem = treeview.focus().strip('#')

        def delete():
            """delete the selected item"""

            curitem = treeview.focus().strip().strip('#')
            print("deleting : ", curitem)

            del series_dict[curitem]

            with open('series_table.json', 'w') as f:
                json.dump(series_dict, f, indent=2)

        def edit():
            """edit the properties of the selected item"""

            curitem = treeview.focus().strip("#")
            select_values = series_dict[curitem]

            def raging_fire():
                """call back function for edit button in the edit window"""

                if editspin1.get() != '1':  # season
                    select_values[0] = int(editspin1.get())
                    select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editspin2.get() != '1':  # episode
                    select_values[1] = int(editspin2.get())
                    select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editentvar.get() != curitem:  # name
                    series_dict[editentvar.get().title()] = series_dict.pop(curitem)  # update the modify date
                    select_values[3] = "{}".format(datetime.datetime.now())
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editent2var.get() != select_values[2].split('/')[1]:  # pic
                    select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
                    select_values[2] = editent2var.get()
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                edittop.destroy()

            if curitem != "":  # test if an item is highlighted first
                """the actual ecit window widgets"""
                edittop = Toplevel()

                editlab1 = Label(edittop, text="Current Tv-Series title : ")
                editlab1.grid(row=1, column=1, sticky=W, pady=4)

                editent = Entry(edittop, textvariable=editentvar, width=30)
                editentvar.set(curitem)
                editent.grid(row=1, column=2, sticky=W, pady=4)

                editlab2 = Label(edittop, text="Current Season {}, chance to : ".format(select_values[0]))
                editlab2.grid(row=2, column=1, sticky=W, pady=4)

                editspin1 = Spinbox(edittop, from_=1, to=1000, width=5)
                editspin1.grid(row=2, column=2, sticky=W, pady=4)

                editlab3 = Label(edittop, text="Current Episode {}, change to : ".format(select_values[1]))
                editlab3.grid(row=3, column=1, sticky=W, pady=4)

                editspin2 = Spinbox(edittop, from_=1, to=1000, width=5)
                editspin2.grid(row=3, column=2, sticky=W, pady=4)

                editlab4 = Label(edittop, text="Change image to : ")
                editlab4.grid(row=4, column=1, sticky=W, pady=4)

                editent2 = Entry(edittop, textvariable=editent2var, width=35)
                editent2var.set(select_values[2].split('/')[1])
                editent2.grid(row=4, column=2, sticky=E, pady=4)

                editbut = Button(edittop, text='Edit', command=raging_fire)
                editbut.grid(row=5, column=1, sticky=W, pady=4, padx=20)

                download_thumbbut = Button(edittop, text="Download The thumbnail", command=download_thumb)
                download_thumbbut.grid(row=5, column=2, sticky=W, pady=4, padx=20)

                edittop.geometry("400x200+200+300")
                edittop.title("Edit properties of {} ".format(curitem).upper())

        def complete():
            curitem = treeview.focus().strip("#")
            select_values = series_dict[curitem]

            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_cat_data = json.load(other_categories_fo)["complete"]

                print(curitem)
                print(other_cat_data)

        def watch_online():
            curItem = treeview.focus().strip('#')
            prefered_site = watch_site_var.get()

            print('watch {} using the site {}'.format(curItem, prefered_site))

            if prefered_site == "Fmovies":
                webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))
            elif prefered_site == "IO-Movies":
                webbrowser.open_new_tab("https://www.iomovies.to/search?q={}".format(curItem))
            elif prefered_site == "Putlocker":
                webbrowser.open_new_tab("http://putlockers.am/search-movies/{}.html".format(curItem))
            else:
                webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))

        def download_it():
            curItem = treeview.focus().strip('#')
            prefered_site = donwload_site_var.get()

            print('download {} from the site {}'.format(curItem, prefered_site))

            if prefered_site == "EZTV":
                webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem))
            elif prefered_site == "Torrentcouch":
                webbrowser.open_new_tab("https://torrentcouch.net/?s={}".format(curItem))

        def view_thumbnail():
            curItem = treeview.focus().strip('#')
            with open("images_url_dict.json", "r") as f:
                imgs_dict = json.load(f)

            name = "-".join(curItem.lower().split())
            img_list = imgs_dict[name]
            img_url = img_list[0]
            try:
                print(img_list)
                r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("thumbnails/{}.jpg".format(name), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                print("Done downloading")
                image = ImageTk.PhotoImage(Image.open("thumbnails/{}.jpg".format(name)))
                # image = PhotoImage(file='thumbnails/search_ico.png').subsample(12, 12)
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
            except KeyError :
                print("key error")
            #restart_but_img = ImageTk.PhotoImage(Image.open("icons/reload_32px.png"))
            #webbrowser.open_new_tab('{}'.format(curItem))

        def download_thumb():

            curItem = treeview.focus().strip('#')
            select_values = series_dict[curItem]
            print(curItem)
            with open("images_url_dict.json", "r") as f53:
                imgs_dict = json.load(f53)

            name = "-".join(curItem.lower().split())
            img_list = imgs_dict[name]
            img_url = img_list[0]

            r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
            path = "thumbnails/{}.jpg".format(name)
            if r.status_code == 200:
                with open(path, 'wb') as f3:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f3)
            print("Done downloading")
            select_values = series_dict[curItem]
            editent2var.set(path)
            with open('series_table.json', 'w') as f5:
                json.dump(series_dict, f5, indent=2)

        def watch_trailler():
            curItem = treeview.focus().strip('#')

            webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(curItem))

        def view_details():
            curitem = treeview.focus().strip("#")

            with open("images_url_dict.json", "r") as f23:
                imgs_dict = json.load(f23)
            name = "-".join(curitem.lower().split())

            url, title, ID = imgs_dict[name]

            webbrowser.open_new_tab("https://eztv.io/shows/{}/{}/".format(ID, title))

        # right-click menu

        popup_menu = Menu(tearoff=0)
        popup_menu.add_command(label='Delete', command=delete)
        popup_menu.add_command(label='Edit', command=edit)
        popup_menu.add_command(label="Complete", command=complete)
        popup_menu.add_command(label="View Thumbnail", command=view_thumbnail)
        popup_menu.add_separator()
        popup_menu.add_command(label="Watch Trailer", command=watch_trailler)
        popup_menu.add_command(label="Watch Online", command=watch_online)
        popup_menu.add_command(label='Download', command=download_it)
        popup_menu.add_command(label="View Details", command=view_details)

        if curItem == "":
            print("add some items my friend...")
        else:
            popup_menu.post(event.x_root, event.y_root)


    mainWindow = Tk()

    screen_height = mainWindow.winfo_screenheight()
    screen_width = mainWindow.winfo_screenwidth()

    # Tkinter Variables
    searchentvar = StringVar()
    searchentvar.set('Search')
    searchimage = PhotoImage(file='thumbnails/search_ico.png').subsample(12, 12)
    editentvar = StringVar()
    editent2var = StringVar()
    editent2var.set("image")
    signed_inlb_var = StringVar()
    auto_refresh_var = BooleanVar()
    jep = BooleanVar()
    watch_site_var = StringVar()
    watch_site_var.set("Fmovies")  # set default "watch online " site
    donwload_site_var = StringVar()
    donwload_site_var.set("EZTV")  # set default "download" site

    try:
        signed_inlb_var.set('Signed in as {}'.format(gitup.get_user()))
    except Exception as e:
        signed_inlb_var.set('Not Connected')

    # tkinter main menu bar

    menubar = Menu(mainWindow)

    # watch_menu functions

    def set_watch_site(w_site):
        print(w_site)
        watch_site_var.set(w_site)

    def set_download_site(d_site):
        print(d_site)
        donwload_site_var.set(d_site)

    watchsite_menu = Menu(tearoff=0)
    watchsite_menu.add_radiobutton(label="  Fmovies  ", background="white", foreground="black", command=lambda: set_watch_site("Fmovies"))
    watchsite_menu.add_radiobutton(label="  IO-Movies  ", background="white", foreground="black", command=lambda: set_watch_site("IO-Movies"))
    watchsite_menu.add_radiobutton(label="  Putlocker  ", background="white", foreground="black", command=lambda: set_watch_site("Putlocker"))

    doenloadsite_menu = Menu(tearoff=0)
    doenloadsite_menu.add_radiobutton(label="  EZTV  ", background="white", foreground="black", command=lambda: set_download_site("EZTV"))
    doenloadsite_menu.add_radiobutton(label=" Torrentcouch", background="white", foreground="black", command=lambda: set_download_site("Torrentcouch"))

    filemenu = Menu(tearoff=0)
    filemenu.add_command(label='Exit', command=lambda: mainWindow.destroy())
    filemenu.add_command(label='Push My Data', command=lambda: gitup.push_up())
    filemenu.add_command(label='Pull My Data', command=lambda: gitup.pull_down())
    filemenu.add_separator()
    filemenu.add_cascade(label="Watching Sites", menu=watchsite_menu)
    filemenu.add_cascade(label="Download Sites", menu=doenloadsite_menu)

    options_menu = Menu(tearoff=0)
    options_menu.add_command(label='update list', command=refresh)
    options_menu.add_checkbutton(label='Online thumbs', variable=jep, command=lambda: print(jep.get()))
    options_menu.add_command(label="Account Login", command=LogIn.login_UI)
    options_menu.add_checkbutton(label="Auto-refresh", variable=auto_refresh_var, command=lambda: print(auto_refresh_var.get()))

    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Options', menu=options_menu)

    # Widgets

    signed_inlb = Label(mainWindow, textvariable=signed_inlb_var, bg="white", fg="black")
    treeview = ttk.Treeview(mainWindow)
    tree_configure()
    list_movies(series_dict)
    treeview.bind('<Double-Button-1>', selectitem)
    if operating_system == 'win32' or 'linux' or 'cygwin':
        treeview.bind('<Button-3>', selectitem_options)
    elif operating_system == 'darwin':
        treeview.bind('<Button-2>', selectitem_options)

    previewlb = LabelFrame(mainWindow, text=' PREVIEW ', bd=3, font='bold 11', bg="white", fg="black")
    preview_box = Text(previewlb, width=30, height=20, selectbackground='white', relief=SUNKEN,
                       bd=3, state='disabled', bg="white", fg="black")

    searchent = Entry(mainWindow, textvariable=searchentvar, width=28, font='italic 11', bg="white", fg="black")
    searchbut = Button(mainWindow, image=searchimage, relief=GROOVE, bd=3, bg="white", fg="black")

    addbut = Button(mainWindow, text=' ADD NEW ENTRY ', font='System 12 bold', command=add_movie.add_ui, bg="white", fg="black")

    # Packing Widgets

    signed_inlb.place(x=10, y=3)
    previewlb.pack(side=LEFT, anchor=S, pady=20, padx=2)
    preview_box.pack(side=LEFT, padx=5, pady=5, anchor=S)
    treeview.pack(side=RIGHT, fill=Y)

    searchent.place(x=10, y=60)
    searchbut.place(x=242, y=60)

    addbut.place(x=65, y=115)

    # canv = Canvas(mainWindow, bg="red")
    # canv.pack(side=TOP, fill=X)

    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.config(menu=menubar, bg="white")
    mainWindow.resizable(FALSE, FALSE)
    mainWindow.mainloop()


if __name__ == '__main__':
    
    def refresh():
        mainWindow.destroy()
        main()

    main()




