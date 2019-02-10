
# import urllib.request
# from bs4 import BeautifulSoup
# import json
# from ast import literal_eval
#
# details_dict = {}
#
#
# url = "https://eztv.io/showlist/"
#
# url_ing_lis = []
#
# hdr = {"User-Agent": "Mozila/5.0"}
# req = urllib.request.Request(url, headers=hdr)
# page = urllib.request.urlopen(req)
#
# soup = BeautifulSoup(page, "html.parser")
#
# so = soup.find_all("a", {"class": "thread_link"})
#
# # https://eztv.io/ezimg/thumbs/the-100-2029.jpg
#
# for link in so:
#     c = link.get("href")
#     q, w, index, name, e = c.split("/")
#     u = "https://eztv.io/ezimg/thumbs/{}-{}.jpg".format(name, index)
#     url_ing_lis.append(u)
#
# with open("tesults.txt", "w") as f:
#     f.write(str(url_ing_lis))
#
#
# with open("tesults.txt", "r") as f:
#     lis = literal_eval(f.read())
#
#     for img in lis:
#         length = len(img.split("/")[5].split(".")[0].rsplit("-"))
#         index = img.split("/")[5].split(".")[0].rsplit("-")[-1]
#         name_title = " ".join(img.split("/")[5].split(".")[0].rsplit("-")[:length-1]).title()
#         name = "-".join(img.split("/")[5].split(".")[0].rsplit("-")[:length-1])
#         img_url = "https://eztv.io/ezimg/thumbs/{}-{}.jpg".format(name, index)
#         #print(index, name_title, img_url)
#
#         details_dict[name] = [img_url, name_title, index]
#
#
# with open("images_url_dict.json", "w") as f:
#     json.dump(details_dict, f, indent=2)
#
#
# from github import Github
#
# g = Github("ayieko168", "joshuambago1230Q#")

# for repo in g.get_user().get_repos():
#     print(repo)
#
# from LogIn import get_credentials
#
# print(get_credentials())
#
# {"complete": {}, "wish_list": {}, "movies": {}, "on_break": {}}
#
# import os
#
# files = os.listdir("thumbnails")
#
# for file in files:
#     if (file == "exclamation.jpg") or (file == "search_ico.png") or (file == "Shadow-Guy-Shrugging.jpg"):
#         print("not deleting {}".format(file))
#     else:
#         prev_path = os.getcwd()
#         os.chdir("thumbnails")
#         print("deleting file {} ".format(file))
#         os.remove(file)
#         os.chdir(prev_path)

