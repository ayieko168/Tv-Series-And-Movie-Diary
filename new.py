
# # import urllib.request
# # from bs4 import BeautifulSoup
# # import json
# # from ast import literal_eval
# #
# # details_dict = {}
# #
# #
# # url = "https://eztv.io/showlist/"
# #
# # url_ing_lis = []
# #
# # hdr = {"User-Agent": "Mozila/5.0"}
# # req = urllib.request.Request(url, headers=hdr)
# # page = urllib.request.urlopen(req)
# #
# # soup = BeautifulSoup(page, "html.parser")
# #
# # so = soup.find_all("a", {"class": "thread_link"})
# #
# # # https://eztv.io/ezimg/thumbs/the-100-2029.jpg
# #
# # for link in so:
# #     c = link.get("href")
# #     q, w, index, name, e = c.split("/")
# #     u = "https://eztv.io/ezimg/thumbs/{}-{}.jpg".format(name, index)
# #     url_ing_lis.append(u)
# #
# # with open("tesults.txt", "w") as f:
# #     f.write(str(url_ing_lis))
# #
# #
# # with open("tesults.txt", "r") as f:
# #     lis = literal_eval(f.read())
# #
# #     for img in lis:
# #         length = len(img.split("/")[5].split(".")[0].rsplit("-"))
# #         index = img.split("/")[5].split(".")[0].rsplit("-")[-1]
# #         name_title = " ".join(img.split("/")[5].split(".")[0].rsplit("-")[:length-1]).title()
# #         name = "-".join(img.split("/")[5].split(".")[0].rsplit("-")[:length-1])
# #         img_url = "https://eztv.io/ezimg/thumbs/{}-{}.jpg".format(name, index)
# #         #print(index, name_title, img_url)
# #
# #         details_dict[name] = [img_url, name_title, index]
# #
# #
# # with open("images_url_dict.json", "w") as f:
# #     json.dump(details_dict, f, indent=2)
# #
# #
# # from github import Github
# #
# # g = Github("ayieko168", "joshuambago1230Q#")

# # for repo in g.get_user().get_repos():
# #     print(repo)
# #
# # from LogIn import get_credentials
# #
# # print(get_credentials())
# #
# # {"complete": {}, "wish_list": {}, "movies": {}, "on_break": {}}
# #
# # import os
# #
# # files = os.listdir("thumbnails")
# #
# # for file in files:
# #     if (file == "exclamation.jpg") or (file == "search_ico.png") or (file == "Shadow-Guy-Shrugging.jpg"):
# #         print("not deleting {}".format(file))
# #     else:
# #         prev_path = os.getcwd()
# #         os.chdir("thumbnails")
# #         print("deleting file {} ".format(file))
# #         os.remove(file)
# #         os.chdir(prev_path)

# def delete_item_complete():
#     """delete the selected item"""
#     curItem = complete_tereeview.focus().strip('#')

#     with open("Other_title_categories.json", "r") as other_categories_fo:
#         other_categories_foData = json.load(other_categories_fo)
#         completeDict = other_categories_foData["complete"]
#         selectetItemData_complete = completeDict[curItem]

#     print("deleting : ", curItem)

#     del completeDict[curItem]
#     other_categories_foData["complete"] = completeDict

#     with open('Other_title_categories.json', 'w') as f:
#         json.dump(series_dict, f, indent=2)
#         print("done deleting the title ", curItem)

#     complete_tereeview.delete(complete_tereeview.focus())

# def edit():
#     """edit the properties of the selected item"""

#     curitem = treeview.focus().strip("#")
#     select_values = series_dict[curitem]

#     def raging_fire():
#         """call back function for edit button in the edit window"""

#         if editspin1.get() != '1':  # season
#             select_values[0] = int(editspin1.get())
#             select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
#             with open('series_table.json', 'w') as f:
#                 json.dump(series_dict, f, indent=2)

#         if editspin2.get() != '1':  # episode
#             select_values[1] = int(editspin2.get())
#             select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
#             with open('series_table.json', 'w') as f:
#                 json.dump(series_dict, f, indent=2)

#         if editentvar.get() != curitem:  # name
#             series_dict[editentvar.get().title()] = series_dict.pop(curitem)  # update the modify date
#             select_values[3] = "{}".format(datetime.datetime.now())
#             with open('series_table.json', 'w') as f:
#                 json.dump(series_dict, f, indent=2)

#         if editent2var.get() != select_values[2].split('/')[1]:  # pic
#             select_values[3] = "{}".format(datetime.datetime.now())  # update the modify date
#             select_values[2] = editent2var.get()
#             with open('series_table.json', 'w') as f:
#                 json.dump(series_dict, f, indent=2)

#         edittop.destroy()

#     if curitem != "":  # test if an item is highlighted first
#         """the actual ecit window widgets"""
#         edittop = Toplevel()

#         editlab1 = Label(edittop, text="Current Tv-Series title : ")
#         editlab1.grid(row=1, column=1, sticky=W, pady=4)

#         editent = Entry(edittop, textvariable=editentvar, width=30)
#         editentvar.set(curitem)
#         editent.grid(row=1, column=2, sticky=W, pady=4)

#         editlab2 = Label(edittop, text="Current Season {}, chance to : ".format(select_values[0]))
#         editlab2.grid(row=2, column=1, sticky=W, pady=4)

#         editspin1 = Spinbox(edittop, from_=1, to=1000, width=5)
#         editspin1.grid(row=2, column=2, sticky=W, pady=4)

#         editlab3 = Label(edittop, text="Current Episode {}, change to : ".format(select_values[1]))
#         editlab3.grid(row=3, column=1, sticky=W, pady=4)

#         editspin2 = Spinbox(edittop, from_=1, to=1000, width=5)
#         editspin2.grid(row=3, column=2, sticky=W, pady=4)

#         editlab4 = Label(edittop, text="Change image to : ")
#         editlab4.grid(row=4, column=1, sticky=W, pady=4)

#         editent2 = Entry(edittop, textvariable=editent2var, width=35)
#         editent2var.set(select_values[2].split('/')[1])
#         editent2.grid(row=4, column=2, sticky=E, pady=4)

#         editbut = Button(edittop, text='Edit', command=raging_fire)
#         editbut.grid(row=5, column=1, sticky=W, pady=4, padx=20)

#         download_thumbbut = Button(edittop, text="Download The thumbnail", command=download_thumb)
#         download_thumbbut.grid(row=5, column=2, sticky=W, pady=4, padx=20)

#         edittop.geometry("400x200+200+300")
#         edittop.title("Edit properties of {} ".format(curitem).upper())


# def complete():
#     curitem = treeview.focus().strip("#")
#     select_values = series_dict[curitem]

#     with open("Other_title_categories.json", "r") as other_categories_fo:
#         other_file_data = json.load(other_categories_fo)
#         complete_data = other_file_data["complete"]
#         complete_data[curitem] = select_values  # add the selected title to "complete"
#     with open("Other_title_categories.json", "w") as other_categories_fo2:
#         json.dump(other_file_data, other_categories_fo2, indent=2)  # write the edited complete to the file

#     print("done writing change to other json file")

#     treeview.delete("#{}".format(curitem))

#     with open("series_table.json", "r") as series_fo:
#         series_fo_data = json.load(series_fo)
#         del series_fo_data[curitem]

#     with open("series_table.json", "w") as series_fo2:
#         json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file

#     print("done writing change to series json file\n")


# def onbreak():
#     curitem = treeview.focus().strip("#")
#     se, ep, img, dte = series_dict[curitem]

#     # add selected item to others onbreak json file
#     print("adding selection to on-break file...")
#     with open("Other_title_categories.json", "r") as other_categories_fo:
#         other_file_data = json.load(other_categories_fo)
#         onbraek_data = other_file_data["on_break"]
#         onbraek_data[curitem] = [se, ep, "NO Preview",
#                                  "{}".format(datetime.datetime.now().date())]  # add the selected title to "complete"
#     with open("Other_title_categories.json", "w") as other_categories_fo2:
#         json.dump(other_file_data, other_categories_fo2, indent=2)  # write the edited complete to the file

#     print("done writing change to other json file")

#     # remove selected item from main treeview
#     treeview.delete("#{}".format(curitem))

#     # remove selected item from series dic
#     print("writing new data to series table...")
#     with open("series_table.json", "r") as series_fo:
#         series_fo_data = json.load(series_fo)
#         del series_fo_data[curitem]

#     with open("series_table.json", "w") as series_fo2:
#         json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file

#     print("done writing change to series json file")
#     print("done all operations\n")


# def watch_online():
#     curItem = treeview.focus().strip('#')
#     prefered_site = watch_site_var.get()

#     print('watch {} using the site {}'.format(curItem, prefered_site))

#     if prefered_site == "Fmovies":
#         webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))
#     elif prefered_site == "IO-Movies":
#         webbrowser.open_new_tab("https://www.iomovies.to/search?q={}".format(curItem))
#     elif prefered_site == "Fmovies2":
#         webbrowser.open_new_tab("https://www5.fmovies.to/search?keyword={}".format(curItem))
#     elif prefered_site == "Putlocker":
#         webbrowser.open_new_tab("http://putlockers.am/search-movies/{}.html".format(curItem))
#     elif prefered_site == "9-Anime":
#         webbrowser.open_new_tab("https://www2.9anime.to/search?keyword={}".format(curItem))
#     else:
#         webbrowser.open_new_tab("http://fmovies.pm/search-movies/{}.html".format(curItem))


# def download_it():
#     curItem = treeview.focus().strip('#')
#     prefered_site = donwload_site_var.get()

#     print('download {} from the site {}'.format(curItem, prefered_site))

#     if prefered_site == "EZTV":
#         webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem))
#     elif prefered_site == "Torrentcouch":
#         webbrowser.open_new_tab("https://torrentcouch.net/?s={}".format(curItem))
#     elif prefered_site == "PiratesBay":
#         webbrowser.open_new_tab("https://thepiratebay.org/search/{}/0/99/0".format(curItem))
#     elif prefered_site == "yifi":
#         webbrowser.open_new_tab("https://yts.am/browse-movies/{}/all/all/0/latest".format(curItem))
#     else:
#         # default
#         webbrowser.open_new_tab('https://eztv.io/search/{}'.format(curItem))


# def view_thumbnail():
#     curItem = treeview.focus().strip('#')
#     with open("images_url_dict.json", "r") as f:
#         imgs_dict = json.load(f)

#     name = "-".join(curItem.lower().split())
#     try:
#         """look for entry info from local database"""
#         img_list = imgs_dict[name]
#         img_url = img_list[0]
#         print(img_list)
#         r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
#         if r.status_code == 200:
#             with open("thumbnails/{}.jpg".format(name), 'wb') as f:
#                 r.raw.decode_content = True
#                 shutil.copyfileobj(r.raw, f)
#         print("Done downloading")
#         image = ImageTk.PhotoImage(Image.open("thumbnails/{}.jpg".format(name)))
#         # image = PhotoImage(file='thumbnails/search_ico.png').subsample(12, 12)
#         Label.image = image
#         preview_box.window_create(index=1.0, window=Label(preview_box, image=image))

#     except KeyError:
#         print("Error :: KeyError")
#         print("try checking and editing the show title spelling.")

#     except Exception as local_excep:

#         print("ERROR :: " + str(local_excep))


# # def download_thumb():
# #     curItem = treeview.focus().strip('#')
# #     select_values = series_dict[curItem]
# #     print(curItem)
# #     with open("images_url_dict.json", "r") as f53:
# #         imgs_dict = json.load(f53)

# #     name = "-".join(curItem.lower().split())
# #     img_list = imgs_dict[name]
# #     img_url = img_list[0]

# #     r = requests.get(img_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
# #     path = "thumbnails/{}.jpg".format(name)
# #     if r.status_code == 200:
# #         with open(path, 'wb') as f3:
# #             r.raw.decode_content = True
# #             shutil.copyfileobj(r.raw, f3)
# #     print("Done downloading")
# #     select_values = series_dict[curItem]
# #     editent2var.set(path)
# #     with open('series_table.json', 'w') as f5:
# #         json.dump(series_dict, f5, indent=2)


# def watch_trailler():
#     curItem = treeview.focus().strip('#')

#     webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(curItem))


# def view_details_complete():
#     """callback for view deteails option in the complete list"""
#     curItem = complete_tereeview.focus().strip('#')

#     with open("images_url_dict.json", "r") as images_dict_fo_complete:
#         imgs_dict = json.load(images_dict_fo_complete)
#     name = "-".join(curItem.lower().split())

#     url, title, ID = imgs_dict[name]

#     webbrowser.open_new_tab("https://eztv.io/shows/{}/{}/".format(ID, title))

# def continue_watching_comlete():

#             curItem = complete_tereeview.focus().strip('#')
#             with open("Other_title_categories.json", "r") as other_categories_fo:
#                 other_categories_foData = json.load(other_categories_fo)
#                 completeDict = other_categories_foData["complete"]
#                 selectetItemData_complete = completeDict[curItem]

#             with open("series_table.json", "r") as series_fo:
#                 series_fo_data = json.load(series_fo)
#                 series_fo_data[curItem] = selectetItemData_complete

#             with open("series_table.json", "w") as series_fo2:
#                 json.dump(series_fo_data, series_fo2, indent=2)  # write the edited complete to the file
#                 print(curItem + " succesfully added to the currenty watching tree...")

#             with open("Other_title_categories.json", "w") as other_categories_fo2:
#                 del completeDict[curItem]
#                 other_categories_foData["complete"] = completeDict
#                 json.dump(other_categories_foData, other_categories_fo2, indent=2)  # write the edited complete to the file
#                 print("done writing relevent changes...")

#             complete_tereeview.delete(complete_tereeview.focus())
#             lis = {curItem : selectetItemData_complete}
#             print(lis)
#             list_movies(lis)

x = "S02E18"
print(x.replace("S", "").split("E"))
