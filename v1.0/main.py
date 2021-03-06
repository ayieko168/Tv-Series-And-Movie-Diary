#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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

# image paths
NoImageFilePath = "thumbnails/No_Image_Available.jpg"
SearchIconPath = "thumbnails/search_ico.png"
ShadowGuyImagePath = "thumbnails/Shadow-Guy-Shrugging.jpg"

# keyboard keys
ADD_TO_WISHLIST_KEY = "<F5>"
REFRESH_PROGARAM_KEY = "<F12>"
HELP_KEY = "<F1>"


print('starting...')
try:
    with open('series_table.json') as f:  # initial reading of json data for series
        data = json.load(f)
except FileNotFoundError:
    with open("series_table.json", "w") as f:
        json.dump({}, f, indent=2)
    with open('series_table.json') as f:  # initial reading of json data for series
        data = json.load(f)
except:
    with open("series_table.json", "w") as f:
        json.dump({}, f, indent=2)
    with open('series_table.json') as f:  # initial reading of json data for series
        data = json.load(f)


series_dict = data


def main():
    print('starting within')
    with open('series_table.json') as f:  # initial reading of json data for series
        series_dict = json.load(f)

    global mainWindow, treeview, complete_tereeview

    # main tkinter window

    # Tkinter Functions

    def search():

        search_item = searchent.get()
        searchent.delete(0, END)

        print("This feature is not available yet\n")

    def view_thumbnail_main(from_treeview):

        curItem = from_treeview.focus().strip('#')

        with open('series_table.json') as f:  # refresh serises data
            series_dict = json.load(f)
            select_values = series_dict[curItem]
        with open("images_url_dict.json", "r") as f:
            imgs_dict = json.load(f)

        print("using main viewer")
        print("online thumbs set to {}".format(online_thumbs.get()))

        if (online_thumbs.get() == 1):
            """view the thumbnail of the selected item in the complete list"""
            # if online thumb is True

            print("view thumbnail from online source")

            name = "-".join(curItem.lower().split())
            image_name = select_values[2]

            if (os.path.isfile("thumbnails/{}.jpg".format(name)) == 0) and (os.path.isfile(image_name) ==0):
                # check if there is an already downloaded image file
                try:
                    """look for entry info from local database"""
                    img_list = imgs_dict[name]
                    img_url = img_list[0]
                    print(img_list)
                    r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                    if r.status_code == 200:
                        with open("thumbnails/{}.jpg".format(name), 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
                    print("Done downloading image")
                    image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                    # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                    # edit dtored image data
                    select_values[2] = "thumbnails/{}.jpg".format(name)
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                except KeyError:
                    print("Failed series image list....")

                    name = curItem
                    try:
                        img_list = imgs_dict[name]
                        img_url = img_list[1]
                        print(img_list)
                        r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                        if r.status_code == 200:
                            with open("thumbnails/{}.jpg".format(name), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                        print("Done downloading file")
                        image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                        # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                        # edit dtored image data
                        select_values[2] = "thumbnails/{}.jpg".format(name)
                        with open('series_table.json', 'w') as f:
                            json.dump(series_dict, f, indent=2)

                    except Exception as error_ml:
                        print("Failed using movie list Error :: \n", error_ml)

                        image = ImageTk.PhotoImage(Image.open(imageProcessor.resize_image(NoImageFilePath)))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                        print("No previwe image availablen\n")

                except Exception as local_excep:

                    print("ERROR :: " + str(local_excep))

            else:
                print(" Using localy found image file")

                try:
                    image = ImageTk.PhotoImage(Image.open(image_name))
                except:
                    image = ImageTk.PhotoImage(Image.open("thumbnails/{}.jpg".format(name)))
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))

        elif online_thumbs.get() == 0:
            # callback when online thumbnails is False

            print("view thumbnail from local directory...")

            if series_dict[curItem][2].endswith("jpg"):
                # if the stored filename has the extension jpg set to LIP
                local_image_path = series_dict[curItem][2]

                try:
                    image = ImageTk.PhotoImage(Image.open(local_image_path))
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except FileNotFoundError:
                    print("No image file found relating to {}".format(curItem))
                    print("Suggestions:\n[Edit the file properties under >Edit>Change image to: ]\n[and input the name of the image file the press edit]")

            else:
                # if not try adding the extension manually
                try:
                    local_image_path = series_dict[curItem][2] + ".jpg"

                    try:
                        image = ImageTk.PhotoImage(Image.open(local_image_path))
                        Label.image = image
                        preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                    except FileNotFoundError:
                        print("No image file found relating to {}".format(curItem))
                        print("Suggestions:\n[Edit the file properties under >Edit>Change image to: ]\n[and input the name of the image file the press edit]")
                except:
                    # if not display:
                    print("Error: This is not a jpeg file please use\na jpeg image or download it from >Edit>DownloadImage")

    def clear_data():

        query = messagebox.askyesnocancel(" Delete all user data", "Are you sure you\nwant to delete all the user data from \nlocal disk?\n\nNOTE: It wont affect your cloud data")
        query_details = messagebox.askyesno("CLEAR DATA?", "Sorry, Do you also Want to\nclear your personal data? ")

        print(query_details)
        if query == 1:
            # default data
            other_data = {
                "complete": {},
                "wish_list": {},
                "movies": {},
                "on_break": {}
            }
            series_dict_data = {}
            details_data = {
                "use": "",
                "pas": [],
                "state": "False"
            }

            print("clearing other categories file...")
            with open("Other_title_categories.json", "w") as oth_fo:
                json.dump(other_data, oth_fo, indent=2)
            print("clearing the series file...")
            with open("series_table.json", "w") as ser_fo:
                json.dump(series_dict_data, ser_fo, indent=2)

            if query_details == 1:
                print("clearing the details file..")
                with open("details.json", "w") as det_fo:
                    json.dump(details_data, det_fo, indent=2)
                print("Reseting user login info...")
                gitup.signin("none", "none")
            else:
                pass

            print("clearing thumbnails...")
            files = os.listdir("thumbnails")
            for file in files:
                if (file == "No_Image_Available.jpg") or (file == "search_ico.png") or (file == "Shadow-Guy-Shrugging.jpg"):
                    print("not deleting {}".format(file))
                else:
                    prev_path = os.getcwd()
                    os.chdir("thumbnails")
                    print("deleting file {} ".format(file))
                    os.remove(file)
                    os.chdir(prev_path)

            print("Done with all operations.\n")

        elif query == 0:

            print("cancel deletion of data")

        elif query == "cancel":

            print("cancel deletion of data")

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

    def selectitem_double_click(a):
        """callback function for the main treeview double click event"""

        view_thumbnail_main(treeview)

    def selectitem_options_main(event):
        """call back function when right click on an item on the main tree-view"""
        with open('series_table.json') as f:  # re-reading data from json for series
            series_dict = json.load(f)

        curItem = treeview.focus().strip('#')

        def delete():
            """delete the selected item"""

            curitem = treeview.focus().strip().strip('#')
            print("deleting : ", curitem)

            del series_dict[curitem]

            with open('series_table.json', 'w') as f:
                json.dump(series_dict, f, indent=2)

            treeview.delete(treeview.focus())
            print("Done Deleting {} from watching list".format(curItem))

        def edit():
            """edit the properties of the selected item"""

            curitem = treeview.focus().strip("#")
            select_values = series_dict[curitem]
            editent2var.set("thumbnails\\")

            def raging_fire():
                """call back function for edit button in the edit window"""

                if editspin1.get() != '0':  # season
                    select_values[0] = int(editspin1.get())
                    select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editspin2.get() != '0':  # episode
                    select_values[1] = int(editspin2.get())
                    select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editentvar.get() != curitem:  # name
                    series_dict[editentvar.get().title()] = series_dict.pop(curitem)  # update the modify date
                    select_values[3] = "{}".format(datetime.datetime.now())
                    with open('series_table.json', 'w') as f:
                        json.dump(series_dict, f, indent=2)

                if editent2var.get() != select_values[2]:  # pic
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

                editspin1 = Spinbox(edittop, from_=0, to=1000, width=5)
                editspin1.grid(row=2, column=2, sticky=W, pady=4)

                editlab3 = Label(edittop, text="Current Episode {}, change to : ".format(select_values[1]))
                editlab3.grid(row=3, column=1, sticky=W, pady=4)

                editspin2 = Spinbox(edittop, from_=0, to=1000, width=5)
                editspin2.grid(row=3, column=2, sticky=W, pady=4)

                editlab4 = Label(edittop, text="Change image to : ")
                editlab4.grid(row=4, column=1, sticky=W, pady=4)

                editent2 = Entry(edittop, textvariable=editent2var, width=35)
                editent2var.set(select_values[2])
                editent2.grid(row=4, column=2, sticky=E, pady=4)

                editbut = Button(edittop, text='Edit', command=raging_fire)
                editbut.grid(row=5, column=1, sticky=W, pady=4, padx=20)

                download_thumbbut = Button(edittop, text="Download The thumbnail", command=download_thumb)
                download_thumbbut.grid(row=5, column=2, sticky=W, pady=4, padx=20)

                edittop.geometry("400x200+200+300")
                edittop.title("Edit properties of {} ".format(curitem).upper())

        def complete():
            curitem = treeview.focus().strip("#")

            with open("Other_title_categories.json", "r") as other_categories_fo:
                select_values = series_dict[curitem]
                other_file_data = json.load(other_categories_fo)
                complete_data = other_file_data["complete"]
                complete_data[curitem] = select_values  # add the selected title to "complete"
            with open("Other_title_categories.json", "w") as other_categories_fo2:
                json.dump(other_file_data, other_categories_fo2, indent=2)  # write the edited complete to the file

            print("done writing change to other json file")

            treeview.delete("#{}".format(curitem))

            with open("series_table.json", "r") as series_fo:
                series_fo_data = json.load(series_fo)
                del series_fo_data[curitem]

            with open("series_table.json", "w") as series_fo2:
                json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file

            print("done writing change to series json file\n")

        def onbreak():

            curitem = treeview.focus().strip("#")
            se, ep, img, _ = series_dict[curitem]

            # add selected item to others onbreak json file
            print("adding selection to on-break file...")
            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_file_data = json.load(other_categories_fo)
                onbraek_data = other_file_data["on_break"]
                onbraek_data[curitem] = [se, ep, img, "{}".format(datetime.datetime.now().date())]  # add the selected title to "complete"
                with open("Other_title_categories.json", "w") as other_categories_fo2:
                    json.dump(other_file_data, other_categories_fo2, indent=2)  # write the edited complete to the file

            print("done writing change to other json file")

            # remove selected item from main treeview
            treeview.delete(treeview.focus())

            # remove selected item from series dic
            print("writing new data to series table...")
            with open("series_table.json", "r") as series_fo:
                series_fo_data = json.load(series_fo)
                del series_fo_data[curitem]
                with open("series_table.json", "w") as series_fo2:
                    json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file

            print("done writing change to series json file")
            print("done all operations\n")

        def watch_online():
            curItem = treeview.focus().strip('#')
            prefered_site = watch_site_var.get()

            print('watch {} using the site {}'.format(curItem, prefered_site))

            if prefered_site == "Fmovies":
                webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))
            elif prefered_site == "IO-Movies":
                webbrowser.open_new_tab("https://www.iomovies.to/search?q={}".format(curItem))
            elif prefered_site == "Fmovies2":
                webbrowser.open_new_tab("https://www5.fmovies.to/search?keyword={}".format(curItem))
            elif prefered_site == "Putlocker":
                webbrowser.open_new_tab("https://www.putlockers.me/search/{}/".format(curItem))
            elif prefered_site == "9-Anime":
                webbrowser.open_new_tab("https://www2.9anime.to/search?keyword={}".format(curItem))
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
            elif prefered_site == "PiratesBay":
                webbrowser.open_new_tab("https://thepiratebay.org/search/{}/0/99/0".format(curItem))
            elif prefered_site == "yifi":
                webbrowser.open_new_tab("https://yts.am/browse-movies/{}/all/all/0/latest".format(curItem))
            else:
                # default
                webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem))

        def view_thumbnail():

            view_thumbnail_main(treeview)

            print("done\n")

        def download_thumb():
            """callback for Edit>DownloadThumbnailImage for the main treeview"""

            curItem = treeview.focus().strip('#')
            select_values = series_dict[curItem]
            print(curItem)
            with open("images_url_dict.json", "r") as f53:
                imgs_dict = json.load(f53)

            name = "-".join(curItem.lower().split())
            img_list = imgs_dict[name]
            img_url = img_list[0]

            r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
            path = "thumbnails\\{}.jpg".format(name)
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
        popup_menu.add_command(label='Edit', command=edit)
        popup_menu.add_separator()
        popup_menu.add_command(label="Complete", command=complete)
        popup_menu.add_command(label="On Break", command=onbreak)
        popup_menu.add_separator()
        popup_menu.add_command(label="View Thumbnail", command=view_thumbnail)
        popup_menu.add_separator()
        popup_menu.add_command(label='Download', command=download_it)
        popup_menu.add_command(label="Watch Trailer", command=watch_trailler)
        popup_menu.add_command(label="Watch Online", command=watch_online)
        popup_menu.add_command(label="View Details", command=view_details)
        popup_menu.add_separator()
        popup_menu.add_command(label='Delete', command=delete)

        if curItem == "":
            print("add some items my friend...")
        else:
            popup_menu.post(event.x_root, event.y_root)

    def wishlist_selectitem_options(event):
        global complete_tereeview

        curItem = wishlist_treeview.focus().strip('#')

        def download_it_wishliat():
            prefered_site = donwload_site_var.get()

            print('download {} from the site {}'.format(curItem, prefered_site))

            if prefered_site == "EZTV":
                webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem)) # default
            elif prefered_site == "Torrentcouch":
                webbrowser.open_new_tab("https://torrentcouch.net/?s={}".format(curItem))
            elif prefered_site == "PiratesBay":
                webbrowser.open_new_tab("https://thepiratebay.org/search/{}/0/99/0".format(curItem))
            elif prefered_site == "yifi":
                webbrowser.open_new_tab("https://yts.am/browse-movies/{}/all/all/0/latest".format(curItem))
            else:
                webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem))

        def start_watching_wishlist():

            curItem = wishlist_treeview.focus().strip('#')
            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                wishlistDict = other_categories_foData["wish_list"]
                selectetItemData_wishlist = wishlistDict[curItem]

            with open("series_table.json", "r") as series_fo:
                series_fo_data = json.load(series_fo)
                series_fo_data[curItem] = selectetItemData_wishlist

            with open("series_table.json", "w") as series_fo2:
                json.dump(series_fo_data, series_fo2, indent=2)  # write the edited wished to the file
                print(curItem + " succesfully added to the currenty watching tree...")

            with open("Other_title_categories.json", "w") as other_categories_fo2:
                del wishlistDict[curItem]
                other_categories_foData["wish_list"] = wishlistDict
                json.dump(other_categories_foData, other_categories_fo2, indent=2)  # write the edited wished to the file
                print("done writing relevent changes...")

            wishlist_treeview.delete(wishlist_treeview.focus())
            lis = {curItem : selectetItemData_wishlist}
            print(lis)
            list_movies(lis)

        def edit_the_selected_value_wishlist():
            """edit the properties of the selected item"""

            curItem = wishlist_treeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                completeDict = other_categories_foData["wish_list"]
                selectetItemData_complete = completeDict[curItem]

            select_values = selectetItemData_complete

            def raging_fire():
                """call back function for edit button in the edit window"""

                if editspin1.get() != '0':  # season
                    select_values[0] = int(editspin1.get()) # modify the change
                    select_values[3] = "{}".format(datetime.datetime.now().date())  # update the modify date
                    with open('Other_title_categories.json', 'w') as f:
                        completeDict[curItem] = select_values
                        json.dump(other_categories_foData, f, indent=2)
                        print("done writing changes")

                if editspin2.get() != '0':  # episode
                    select_values[1] = int(editspin2.get())
                    select_values[3] = "{}".format(datetime.datetime.now().date())  # update the modify date
                    with open('Other_title_categories.json', 'w') as f:
                        completeDict[curItem] = select_values
                        json.dump(other_categories_foData, f, indent=2)
                        print("done writing changes")

                if editentvar.get() != curItem:  # name
                    removed_values = completeDict.pop(curItem) # remove the previous title and write the new one
                    completeDict[editentvar.get()] = removed_values
                    select_values[3] = "{}".format(datetime.datetime.now().date())
                    with open('Other_title_categories.json', 'w') as f:
                        completeDict[editentvar.get()] = select_values  # set the values of the edited title
                        json.dump(other_categories_foData, f, indent=2)
                        print("done writing changes")

                edittop.destroy()

            if curItem != "":  # test if an item is highlighted first
                """the actual edit window widgets"""
                edittop = Toplevel()

                editlab1 = Label(edittop, text="Current Tv-Series title : ")
                editlab1.grid(row=1, column=1, sticky=W, pady=4)

                editent = Entry(edittop, textvariable=editentvar, width=30)
                editentvar.set(curItem)
                editent.grid(row=1, column=2, sticky=W, pady=4)

                editlab2 = Label(edittop, text="Current Season {}, chance to : ".format(select_values[0]))
                editlab2.grid(row=2, column=1, sticky=W, pady=4)

                editspin1 = Spinbox(edittop, from_=0, to=1000, width=5)
                editspin1.grid(row=2, column=2, sticky=W, pady=4)

                editlab3 = Label(edittop, text="Current Episode {}, change to : ".format(select_values[1]))
                editlab3.grid(row=3, column=1, sticky=W, pady=4)

                editspin2 = Spinbox(edittop, from_=0, to=1000, width=5)
                editspin2.grid(row=3, column=2, sticky=W, pady=4)

                editbut = Button(edittop, text='Edit', command=raging_fire)
                editbut.grid(row=5, column=1, sticky=W, pady=4, padx=20)

                edittop.geometry("400x200+200+300")
                edittop.title("Edit properties of {} ".format(curItem).upper())

        def complete_wishlist():

            curItem = wishlist_treeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_fo:
                other_Dictionary = json.load(other_fo)
                wishlist_Dictionary = other_Dictionary["wish_list"]
                selected_values_wishlisted = wishlist_Dictionary[curItem]
                del wishlist_Dictionary[curItem]
                wishlist_treeview.delete(wishlist_treeview.focus())
                # the sellected title is removed from wishlist
                with open("Other_title_categories.json", "w") as oth_fo2:
                    json.dump(other_Dictionary, oth_fo2, indent=2)

            with open("Other_title_categories.json", "r") as oth_fo3:
                other_Dictionary = json.load(oth_fo3)
                complete_Dictionary = other_Dictionary["complete"]
                complete_Dictionary[curItem] = selected_values_wishlisted
                with open("Other_title_categories.json", "w") as oth_fo4:
                    json.dump(other_Dictionary, oth_fo4, indent=2)

        def watch_online_wishlist():

            curItem = wishlist_treeview.focus().strip('#')
            prefered_site = watch_site_var.get()

            print('watch {} using the site {}'.format(curItem, prefered_site))

            if prefered_site == "Fmovies":
                webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))
            elif prefered_site == "IO-Movies":
                webbrowser.open_new_tab("https://www.iomovies.to/search?q={}".format(curItem))
            elif prefered_site == "Fmovies2":
                webbrowser.open_new_tab("https://www5.fmovies.to/search?keyword={}".format(curItem))
            elif prefered_site == "Putlocker":
                webbrowser.open_new_tab("https://www.putlockers.me/search/{}/".format(curItem))
            elif prefered_site == "9-Anime":
                webbrowser.open_new_tab("https://www2.9anime.to/search?keyword={}".format(curItem))
            else:
                webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))

        def watch_trailler_wishlist():
            curItem = wishlist_treeview.focus().strip('#')

            webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(curItem))

        def delete_item_wishlist():
            """delete the selected item"""
            curItem = wishlist_treeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                completeDict = other_categories_foData["wish_list"]
                selectetItemData_complete = completeDict[curItem]

            print("deleting : ", curItem)

            del completeDict[curItem]
            other_categories_foData["wish_list"] = completeDict

            with open('Other_title_categories.json', 'w') as f:
                json.dump(other_categories_foData, f, indent=2)
                print("done deleting the title ", curItem)

            wishlist_treeview.delete(wishlist_treeview.focus())

        def view_thumbnail_wishlist():

            curItem = wishlist_treeview.focus().strip('#')
            with open("images_url_dict.json", "r") as f:
                imgs_dict = json.load(f)

            name = "-".join(curItem.lower().split())
            try:
                """look for entry info from local database"""
                img_list = imgs_dict[name]
                img_url = img_list[0]
                print(img_list)
                r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                print("Done downloading")
                image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))

            except KeyError:
                print("Failed series image list....")
                with open("Movies_List.json", "r") as f:
                    imgs_dict = json.load(f)

                name = curItem
                try:
                    img_list = imgs_dict[name]
                    img_url = img_list[1]
                    print(img_list)
                    r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                    if r.status_code == 200:
                        with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
                    print("Done downloading")
                    image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                    # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except Exception as error_ml:
                    print("Failed using movie list Error :: \n", error_ml)


            except Exception as local_excep:

                print("ERROR :: " + str(local_excep))

        def onbreak_wishlist():

            curItem = wishlist_treeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_fo:
                other_Dictionary = json.load(other_fo)
                wishlist_Dictionary = other_Dictionary["wish_list"]
                selected_values_wishlisted = wishlist_Dictionary[curItem]
                del wishlist_Dictionary[curItem]
                wishlist_treeview.delete(wishlist_treeview.focus())
                # the sellected title is removed from wishlist
                with open("Other_title_categories.json", "w") as oth_fo2:
                    json.dump(other_Dictionary, oth_fo2, indent=2)

            with open("Other_title_categories.json", "r") as oth_fo3:
                other_Dictionary = json.load(oth_fo3)
                onbraek_Dictionary = other_Dictionary["on_break"]
                onbraek_Dictionary[curItem] = selected_values_wishlisted
                with open("Other_title_categories.json", "w") as oth_fo4:
                    json.dump(other_Dictionary, oth_fo4, indent=2)

        def view_details_wishlist():

            """callback for view deteails option in the complete list"""
            try:
                curItem = wishlist_treeview.focus().strip('#')

                with open("images_url_dict.json", "r") as images_dict_fo_complete:
                    imgs_dict = json.load(images_dict_fo_complete)
                name = "-".join(curItem.lower().split())

                _, title, ID = imgs_dict[name]

                webbrowser.open_new_tab("https://eztv.io/shows/{}/{}/".format(ID, title))
            except KeyError:
                print("Failed to use series list")

                webbrowser.open_new_tab("https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=tt".format(curItem))

        popup_menu = Menu(tearoff=0)
        popup_menu.add_command(label='Edit', command=edit_the_selected_value_wishlist)
        popup_menu.add_separator()
        popup_menu.add_command(label="Start watching", command=start_watching_wishlist)
        popup_menu.add_command(label="Complete", command=complete_wishlist)
        popup_menu.add_separator()
        popup_menu.add_command(label="View Thumbnail", command=view_thumbnail_wishlist)
        popup_menu.add_separator()
        popup_menu.add_command(label="Watch trailler", command=watch_trailler_wishlist)
        popup_menu.add_command(label="Watch online", command=watch_online_wishlist)
        popup_menu.add_command(label="Download It..", command=download_it_wishliat)
        popup_menu.add_command(label="On Beak", command=onbreak_wishlist)
        popup_menu.add_command(label="View Details", command=view_details_wishlist)
        popup_menu.add_separator()
        popup_menu.add_command(label='Delete', command=delete_item_wishlist)

        if curItem == "":
            print("add some items my friend...")
        else:
            popup_menu.post(event.x_root, event.y_root)

    def onbreak_selectitem_options(event):

        def restore_onbraek():

            curItem = onbreak_treeview.focus().strip('#')
            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                onbreakDict = other_categories_foData["on_break"]
                selectetItemData_complete = onbreakDict[curItem]

            with open("series_table.json", "r") as series_fo:
                series_fo_data = json.load(series_fo)
                series_fo_data[curItem] = selectetItemData_complete

            with open("series_table.json", "w") as series_fo2:
                json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file
                print(curItem + " succesfully added to the currenty watching tree...")

            with open("Other_title_categories.json", "w") as other_categories_fo2:
                del onbreakDict[curItem]
                other_categories_foData["on_break"] = onbreakDict
                json.dump(other_categories_foData, other_categories_fo2, indent=2)  # write the edited complete to the file
                print("done writing relevent changes...")

            onbreak_treeview.delete(onbreak_treeview.focus())
            lis = {curItem : selectetItemData_complete}
            print(lis)
            list_movies(lis)

        def complete_onbreak():
            curItem = onbreak_treeview.focus().strip('#')
            with open("Other_title_categories.json", "r") as other_fo:
                other_Dictionary = json.load(other_fo)
                onbreak_Dictionary = other_Dictionary["on_break"]
                selected_values_wishlisted = onbreak_Dictionary[curItem]
                del onbreak_Dictionary[curItem]
                onbreak_treeview.delete(onbreak_treeview.focus())
                # the sellected title is removed from wishlist
                with open("Other_title_categories.json", "w") as oth_fo2:
                    json.dump(other_Dictionary, oth_fo2, indent=2)

            with open("Other_title_categories.json", "r") as oth_fo3:
                other_Dictionary = json.load(oth_fo3)
                complete_Dictionary = other_Dictionary["complete"]
                complete_Dictionary[curItem] = selected_values_wishlisted
                with open("Other_title_categories.json", "w") as oth_fo4:
                    json.dump(other_Dictionary, oth_fo4, indent=2)

        def view_details_break():

            try:
                curItem = onbreak_treeview.focus().strip('#')

                with open("images_url_dict.json", "r") as images_dict_fo_complete:
                    imgs_dict = json.load(images_dict_fo_complete)
                name = "-".join(curItem.lower().split())

                _, title, ID = imgs_dict[name]

                webbrowser.open_new_tab("https://eztv.io/shows/{}/{}/".format(ID, title))
            except KeyError:
                print("Failed to use series list")

                webbrowser.open_new_tab("https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=tt".format(curItem))

        def view_thumbnail_break():

            """view the thumbnail of the selected item in the complete list"""
            curItem = onbreak_treeview.focus().strip('#')
            with open("images_url_dict.json", "r") as f:
                imgs_dict = json.load(f)

            name = "-".join(curItem.lower().split())
            try:
                """look for entry info from local database"""
                img_list = imgs_dict[name]
                img_url = img_list[0]
                print(img_list)
                r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                print("Done downloading")
                image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))

            except KeyError:
                print("Failed series image list....")
                with open("Movies_List.json", "r") as f:
                    imgs_dict = json.load(f)

                name = curItem
                try:
                    img_list = imgs_dict[name]
                    img_url = img_list[1]
                    print(img_list)
                    r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                    if r.status_code == 200:
                        with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
                    print("Done downloading")
                    image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                    # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except Exception as error_ml:
                    print("Failed using movie list Error :: \n", error_ml)


            except Exception as local_excep:

                print("ERROR :: " + str(local_excep))

        def delete_onbreak():

            """delete the selected item"""
            curItem = onbreak_treeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                onbreakDict = other_categories_foData["on_break"]

            print("deleting : ", curItem)

            del onbreakDict[curItem]
            other_categories_foData["on_break"] = onbreakDict

            with open('Other_title_categories.json', 'w') as f:
                json.dump(other_categories_foData, f, indent=2)
                print("done deleting the title ", curItem)

            onbreak_treeview.delete(onbreak_treeview.focus())

        # delete popup menu
        curItem = onbreak_treeview.focus().strip('#')
        popup_menu = Menu(tearoff=0)
        popup_menu.add_command(label='Restore', command=restore_onbraek)
        popup_menu.add_command(label="Complete", command=complete_onbreak)
        popup_menu.add_command(label="View Details", command=view_details_break)
        popup_menu.add_command(label="View thumbnail", command=view_thumbnail_break)
        popup_menu.add_separator()
        popup_menu.add_command(label='Delete', command=delete_onbreak)

        if curItem == "":
            print("add some items my friend...")
        else:
            popup_menu.post(event.x_root, event.y_root)

    def complete_selectitem_options(event):

        curItem = complete_tereeview.focus().strip('#')

        def continue_watching_comlete():

            curItem = complete_tereeview.focus().strip('#')
            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                completeDict = other_categories_foData["complete"]
                selectetItemData_complete = completeDict[curItem]

            with open("series_table.json", "r") as series_fo:
                series_fo_data = json.load(series_fo)
                series_fo_data[curItem] = selectetItemData_complete

            with open("series_table.json", "w") as series_fo2:
                json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file
                print(curItem + " succesfully added to the currenty watching tree...")

            with open("Other_title_categories.json", "w") as other_categories_fo2:
                del completeDict[curItem]
                other_categories_foData["complete"] = completeDict
                json.dump(other_categories_foData, other_categories_fo2, indent=2)  # write the edited complete to the file
                print("done writing relevent changes...")

            complete_tereeview.delete(complete_tereeview.focus())
            lis = {curItem : selectetItemData_complete}
            print(lis)
            list_movies(lis)

        def view_thumbnail_complete():
            """view the thumbnail of the selected item in the complete list"""
            curItem = complete_tereeview.focus().strip('#')
            with open("images_url_dict.json", "r") as f:
                imgs_dict = json.load(f)

            name = "-".join(curItem.lower().split())
            try:
                """look for entry info from local database"""
                img_list = imgs_dict[name]
                img_url = img_list[0]
                print(img_list)
                r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                print("Done downloading")
                image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                Label.image = image
                preview_box.window_create(index=1.0, window=Label(preview_box, image=image))

            except KeyError:
                print("Failed series image list....")
                with open("Movies_List.json", "r") as f:
                    imgs_dict = json.load(f)

                name = curItem
                try:
                    img_list = imgs_dict[name]
                    img_url = img_list[1]
                    print(img_list)
                    r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
                    if r.status_code == 200:
                        with open("thumbnails\\{}.jpg".format(name), 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
                    print("Done downloading")
                    image = ImageTk.PhotoImage(Image.open("thumbnails\\{}.jpg".format(name)))
                    # image = PhotoImage(file='thumbnails\\search_ico.png').subsample(12, 12)
                    Label.image = image
                    preview_box.window_create(index=1.0, window=Label(preview_box, image=image))
                except Exception as error_ml:
                    print("Failed using movie list Error :: \n", error_ml)


            except Exception as local_excep:

                print("ERROR :: " + str(local_excep))

        def view_details_complete():
            """callback for view deteails option in the complete list"""
            curItem = complete_tereeview.focus().strip('#')

            with open("images_url_dict.json", "r") as images_dict_fo_complete:
                imgs_dict = json.load(images_dict_fo_complete)
            name = "-".join(curItem.lower().split())

            url, title, ID = imgs_dict[name]

            webbrowser.open_new_tab("https://eztv.io/shows/{}/{}/".format(ID, title))

        def delete_item_complete():
            """delete the selected item"""
            curItem = complete_tereeview.focus().strip('#')

            with open("Other_title_categories.json", "r") as other_categories_fo:
                other_categories_foData = json.load(other_categories_fo)
                completeDict = other_categories_foData["complete"]
                selectetItemData_complete = completeDict[curItem]

            print("deleting : ", curItem)

            del completeDict[curItem]
            other_categories_foData["complete"] = completeDict

            with open('Other_title_categories.json', 'w') as f:
                json.dump(other_categories_foData, f, indent=2)
                print("done deleting the title ", curItem)

            complete_tereeview.delete(complete_tereeview.focus())

        # compete tab popup menu
        popup_menu = Menu(tearoff=0)
        popup_menu.add_command(label="Continue Watching", command=continue_watching_comlete)
        popup_menu.add_command(label="View thumbnail", command=view_thumbnail_complete)
        popup_menu.add_command(label="View details", command=view_details_complete)
        popup_menu.add_separator()
        popup_menu.add_command(label='Delete', command=delete_item_complete)

        if curItem == "":
            print("add some items my friend...")
        else:
            popup_menu.post(event.x_root, event.y_root)

    mainWindow = Tk()

    # Tkinter Variables
    searchentvar = StringVar()
    searchentvar.set('Search')
    searchimage = PhotoImage(file=SearchIconPath).subsample(12, 12)
    editentvar = StringVar()
    editent2var = StringVar()
    editent2var.set("image")
    signed_inlb_var = StringVar()
    online_thumbs = BooleanVar()
    watch_site_var = StringVar()
    watch_site_var.set("Fmovies")  # set default "watch online " site
    donwload_site_var = StringVar()
    donwload_site_var.set("EZTV")  # set default "download" site

    try:
        signed_inlb_var.set('Signed in as {}'.format(gitup.get_user()))
    except Exception:
        signed_inlb_var.set('Not Connected')

    # tkinter main menu bar

    menubar = Menu(mainWindow, font=(11))

    # watch_menu functions

    def set_watch_site(w_site):
        print(w_site)
        watch_site_var.set(w_site)

    def set_download_site(d_site):
        print(d_site)
        donwload_site_var.set(d_site)

    def change_view(what):

        if (what == "complete") and (view_compl_var.get() == False):
            """View the Complete treeview list"""
            print("view complete list")

            # the function
            global complete_tereeview

            treeview.forget()
            with open("Other_title_categories.json", "r") as other_fo:
                other_fo_data = json.load(other_fo)["complete"]
            try:
                complete_tereeview = ttk.Treeview(mainWindow)

                complete_tereeview.config(columns=('sn', 'ep'))
                complete_tereeview.column('#0', width=150, anchor=CENTER)
                complete_tereeview.column('sn', width=60, anchor=CENTER)
                complete_tereeview.column('ep', width=60, anchor=CENTER)

                complete_tereeview.heading('#0', text='Name')
                complete_tereeview.heading('sn', text='Season')
                complete_tereeview.heading('ep', text='Episode')

                for k, v in sorted(other_fo_data.items()):
                    complete_tereeview.insert('', END, '#{}'.format(k), text=k)
                    complete_tereeview.set('#{}'.format(k), 'sn', v[0])
                    complete_tereeview.set('#{}'.format(k), 'ep', v[1])

                complete_tereeview.pack(side=RIGHT, fill=Y)

                if operating_system == 'win32' or 'linux' or 'cygwin':
                    complete_tereeview.bind('<Button-3>', complete_selectitem_options)
                elif operating_system == 'darwin':
                    complete_tereeview.bind('<Button-2>', complete_selectitem_options)

            except Exception as e2:
                print(e2)

            # prevent re-packing
            view_compl_var.set(True)
            view_curren_var.set(False)

        elif (what == "current") and (view_curren_var.get() == False):
            """Show the Currently watching show list if this option is selected"""
            print("view current list")

            # the function
            try:
                complete_tereeview.forget()
                treeview.pack(side=RIGHT, fill=Y)
            except Exception as e3:
                print(e3)

            # prevent re-packing
            view_compl_var.set(False)
            view_curren_var.set(True)

        elif what == "wishlist":
            print("view my wish list")

            # code
            wishlist_toplevel = Toplevel(mainWindow)

            global wishlist_treeview

            with open("Other_title_categories.json", "r") as other_fo:
                other_fo_data = json.load(other_fo)["wish_list"]
            try:
                wishlist_treeview = ttk.Treeview(wishlist_toplevel)

                wishlist_treeview.config(columns=('sn', 'ep'))
                wishlist_treeview.column('#0', width=200, anchor=CENTER)
                wishlist_treeview.column('sn', width=50, anchor=CENTER)
                wishlist_treeview.column('ep', width=150, anchor=CENTER)

                wishlist_treeview.heading('#0', text='Name')
                wishlist_treeview.heading('sn', text='Season')
                wishlist_treeview.heading('ep', text='Date added')

                for k, v in sorted(other_fo_data.items()):
                    wishlist_treeview.insert('', END, '#{}'.format(k), text=k)
                    wishlist_treeview.set('#{}'.format(k), 'sn', v[0])
                    wishlist_treeview.set('#{}'.format(k), 'ep', v[3])
                wishlist_treeview.pack(fill=Y, padx=2, pady=5)

            except Exception as e2:
                print(e2)

            if operating_system == 'win32' or 'linux' or 'cygwin':
                wishlist_treeview.bind('<Button-3>', wishlist_selectitem_options)
            elif operating_system == 'darwin':
                wishlist_treeview.bind('<Button-2>', wishlist_selectitem_options)

            wishlist_toplevel.geometry("400x600")
            wishlist_toplevel.resizable(0, 0)
            wishlist_toplevel.title("Wish list")

        elif what == "onbreak":
            print("view shows on break")

            onbreak_topview = Toplevel(mainWindow)

            global onbreak_treeview

            with open("Other_title_categories.json", "r") as other_fo:
                other_fo_data = json.load(other_fo)["on_break"]
            try:
                onbreak_treeview = ttk.Treeview(onbreak_topview)

                onbreak_treeview.config(columns=('sn', 'ep'))
                onbreak_treeview.column('#0', width=200, anchor=CENTER)
                onbreak_treeview.column('sn', width=50, anchor=CENTER)
                onbreak_treeview.column('ep', width=150, anchor=CENTER)

                onbreak_treeview.heading('#0', text='Name')
                onbreak_treeview.heading('sn', text='Season')
                onbreak_treeview.heading('ep', text='Date added')

                for k, v in sorted(other_fo_data.items()):
                    onbreak_treeview.insert('', END, '#{}'.format(k), text=k)
                    onbreak_treeview.set('#{}'.format(k), 'sn', v[0])
                    onbreak_treeview.set('#{}'.format(k), 'ep', v[3])
                onbreak_treeview.pack(fill=Y, padx=2, pady=5)

            except Exception as e2:
                print(e2)

            if operating_system == 'win32' or 'linux' or 'cygwin':
                onbreak_treeview.bind('<Button-3>', onbreak_selectitem_options)
            elif operating_system == 'darwin':
                onbreak_treeview.bind('<Button-2>', onbreak_selectitem_options)

            onbreak_topview.geometry("400x600")
            onbreak_topview.resizable(0, 0)
            onbreak_topview.title("Shows on break")

    def add_to_wish_list(event):
        with open('Other_title_categories.json') as f:
            other_data = json.load(f)

        wishlist_data = other_data["wish_list"]

        def add_wish(event):

            title = movie_titleent.get()

            if title != "":
                print(title, " is being added to the wish list")
                wishlist_data[title.title()] = [0, 0, "thumbnails\\", "{}".format(datetime.datetime.now().date())]
                # write change to json file
                with open("Other_title_categories.json", "w") as othfo:
                    json.dump(other_data, othfo, indent=2)
                print("successful...")
            else:
                print("nothing")

            add_wishlist_window.destroy()

        add_wishlist_window = Toplevel(mainWindow)  # change to top view

        add_title = Label(add_wishlist_window, text=' Add a new Movie to your wish-list'.upper(), bg='white', anchor=CENTER)
        add_title.pack(side=TOP)

        movie_titlelb = Label(add_wishlist_window, text='Movie Title : '.upper(), bg='white', anchor=CENTER)
        movie_titlelb.pack(side=LEFT)

        movie_titleent = Entry(add_wishlist_window, bg='white', width=35, fg="black")
        movie_titleent.pack(side=LEFT, after=movie_titlelb)
        movie_titleent.focus_set()


        addbut = Button(add_wishlist_window, bg='white', text='add'.upper())
        addbut.bind('<Button-1>', add_wish)
        addbut.pack(side=LEFT, anchor=CENTER, padx=5)

        if operating_system == 'win32' or 'linux' or 'cygwin':
            add_wishlist_window.bind('<Return>', add_wish)
        elif operating_system == 'darwin':
            add_wishlist_window.bind('<Return>', add_wish)

        add_wishlist_window.geometry('400x100+500+300')
        add_wishlist_window.config(bg='white')
        add_wishlist_window.resizable(width=False, height=False)
        add_wishlist_window.title('ADD MOVIES TO WISH LIST')

    def watch_tutorials():

        print("watch tutorials")

        webbrowser.open_new_tab("https://www.youtube.com/watch?v=2lI5CvZjBPI&list=PLYBkj59Lkv1rtz6lrjRHIizK3kTTH41vB")

    def about_func(event):
        """About option menu brop down"""

        def about_right_click(event):
            """About Right click call back function"""
            popup_menu = Menu(tearoff=0)
            popup_menu.add_command(label='Copy')

            popup_menu.post(event.x_root, event.y_root)

        abt_topLevel = Toplevel(mainWindow)

        abt_text = Text(abt_topLevel, bg="black", fg="white", width=60, height=10)

        abt_text.insert(INSERT, """This simple Python GUI program helps youkeep track of\nTvSeries that you are watching.\nFollow thislink to github to find out\nmore :: \nhttps://github.com/ayieko168/Tv-Series-And-Movie-Diary.git \n ;)""")
        abt_text.insert(INSERT, "\n\n\n")
        abt_text.insert(INSERT, "Author : Antony Alen" )
        abt_text.pack()

        if operating_system == 'win32' or 'linux' or 'cygwin':
            abt_text.bind('<Button-3>', about_right_click)
        elif operating_system == 'darwin':
            abt_text.bind('<Button-2>', about_right_click)

        abt_text.config(exportselection=1, state=DISABLED)

    # menu bar

    watchsite_menu = Menu(tearoff=0)
    watchsite_menu.add_radiobutton(label="  Fmovies  ", background="white", foreground="black",
                                   command=lambda: set_watch_site("Fmovies"))
    watchsite_menu.add_radiobutton(label="  Fmovies2  ", background="white", foreground="black",
                                   command=lambda: set_watch_site("Fmovies2"))
    watchsite_menu.add_radiobutton(label="  IO-Movies  ", background="white", foreground="black",
                                   command=lambda: set_watch_site("IO-Movies"))
    watchsite_menu.add_radiobutton(label="  Putlocker  ", background="white", foreground="black",
                                   command=lambda: set_watch_site("Putlocker"))
    watchsite_menu.add_radiobutton(label="  9-Anime  ", background="white", foreground="black",
                                   command=lambda: set_watch_site("9-Anime"))

    doenloadsite_menu = Menu(tearoff=0)
    doenloadsite_menu.add_radiobutton(label="  EZTV  ", background="white", foreground="black",
                                      command=lambda: set_download_site("EZTV"))
    doenloadsite_menu.add_radiobutton(label=" Torrentcouch", background="white", foreground="black",
                                      command=lambda: set_download_site("Torrentcouch"))
    doenloadsite_menu.add_radiobutton(label=" Pirates Bay", background="white", foreground="black",
                                      command=lambda: set_download_site("PiratesBay"))
    doenloadsite_menu.add_radiobutton(label=" YiFi Movies ", background="white", foreground="black",
                                      command=lambda: set_download_site("yifi"))

    filemenu = Menu(tearoff=0)
    filemenu.add_command(label='Push My Data', command=lambda: gitup.push_up())
    filemenu.add_command(label='Pull My Data', command=lambda: gitup.pull_down())
    filemenu.add_separator()
    filemenu.add_cascade(label="Watching Sites", menu=watchsite_menu)
    filemenu.add_cascade(label="Download Sites", menu=doenloadsite_menu)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=lambda: mainWindow.destroy())

    options_menu = Menu(tearoff=0)
    options_menu.add_command(label='Update list', command=lambda: refresh("a"))
    options_menu.add_command(label="Account Login", command=LogIn.login_UI)
    options_menu.add_separator()
    options_menu.add_command(label="Add to wish list", command=lambda: add_to_wish_list("1"))
    options_menu.add_checkbutton(label='Online thumbs', variable=online_thumbs)
    options_menu.add_command(label="Clear All Data", command=clear_data)

    view_compl_var = BooleanVar()
    view_curren_var = BooleanVar()
    view_option_menu = Menu(tearoff=0)
    view_option_menu.add_radiobutton(label="  Currently watching list", command=lambda: change_view("current"))
    view_option_menu.add_radiobutton(label="  Complete Tv-Shows  ", command=lambda: change_view("complete"))
    view_option_menu.add_radiobutton(label="  Shows On Break", command=lambda: change_view("onbreak"))
    view_option_menu.add_radiobutton(label="  My Wish List ", command=lambda: change_view("wishlist"))
    view_menu = Menu(tearoff=0)
    view_menu.add_cascade(label="  view..  ", menu=view_option_menu)

    helpmenu = Menu(tearoff=0)
    helpmenu.add_command(label=" Video Tutorials", command=watch_tutorials)
    helpmenu.add_command(label=" About", command=lambda: about_func("a"))

    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Options', menu=options_menu)
    menubar.add_cascade(label="View", menu=view_menu)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Widgets

    signed_inlb = Label(mainWindow, textvariable=signed_inlb_var, bg="white", fg="black")
    treeview = ttk.Treeview(mainWindow)
    tree_configure()
    list_movies(series_dict)
    previewlb = LabelFrame(mainWindow, text=' PREVIEW ', bd=3, font='bold 11', bg="white", fg="black")
    preview_box = Text(previewlb, width=30, height=20, selectbackground='white', relief=SUNKEN,
                       bd=3, state='disabled', bg="white", fg="black")
    searchent = Entry(mainWindow, textvariable=searchentvar, width=28, font='italic 11', bg="white", fg="black")
    searchbut = Button(mainWindow, image=searchimage, relief=GROOVE, bd=3, bg="white", fg="black", command=search)

    addbut = Button(mainWindow, text=' ADD NEW ENTRY ', font='System 12 bold', command=add_movie.add_ui, bg="white",
                    fg="black")

    # Packing Widgets

    signed_inlb.place(x=10, y=3)
    previewlb.pack(side=LEFT, anchor=S, pady=20, padx=2)
    preview_box.pack(side=LEFT, padx=5, pady=5, anchor=S)
    treeview.pack(side=RIGHT, fill=Y)
    searchent.place(x=10, y=60)
    searchbut.place(x=242, y=60)
    addbut.place(x=65, y=115)

    # key board keys binding

    mainWindow.bind(ADD_TO_WISHLIST_KEY, add_to_wish_list)
    mainWindow.bind(REFRESH_PROGARAM_KEY, refresh)
    mainWindow.bind(HELP_KEY, about_func)
    # main tree view right click binging
    treeview.bind('<Double-Button-1>', selectitem_double_click)
    # popup menu binding for the main tree
    if operating_system == 'win32' or 'linux' or 'cygwin':
        treeview.bind('<Button-3>', selectitem_options_main)
    elif operating_system == 'darwin':
        treeview.bind('<Button-2>', selectitem_options_main)


    mainWindow.geometry("{}x{}+200+100".format(width, height))
    mainWindow.title("  Movie and Series Diary  ")
    mainWindow.config(menu=menubar, bg="white")
    mainWindow.resizable(FALSE, FALSE)
    mainWindow.mainloop()


if __name__ == '__main__':
    def refresh(event):
        print("Refreshing application...")
        mainWindow.destroy()
        main()


    main()
