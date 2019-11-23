import os, json, time

# try:
#     x = os.path.abspath("utils\\data_base.json")
#     with open(x) as p:
#         pass
# except FileNotFoundError:
#     x = os.path.abspath("v2.0\\utils\\data_base.json")
#     with open(x) as p:
#         pass

# print(x)

# print(os.path.isfile(x))


with open("utils\data_base - Copy.json") as data_baseFo:
    data_base = json.load(data_baseFo)

    ## Individual data Dictionaries
    currently_watching_Dict = data_base["currently_watching"]
    complete_tv_shows_Dict = data_base["complete_tv_shows"]
    shows_on_break_Dict = data_base["shows_on_break"]
    wish_list_Dict = data_base["wish_list"]
    seen_movies_Dict = data_base["seen_movies"]
    details_Dict = data_base["details"]
    watch_sites_Dict = data_base["watch_sites"]
    download_sites_Dict = data_base["download_sites"]
    search_dict = data_base["search_dict"]

# title, type, season, episode, datecomplete, datebrake, dateadded, dateseen

editKey = "seen_movies"
editDict = seen_movies_Dict

newDict = {}
date = time.strftime("%Y/%m/%d :: %H:%M", time.gmtime(time.time()))
for title, values in editDict.items():
    print(values)
    title = title.title()

    # if (values[0] == "") or (values[0] == 0) or (values[0] == "0"):

    values[0] = 1

    newDict[title] = [
                    title,
                    str(values[1]), 
                    str(values[2]), 
                    str(values[3]),
                    date
                    ]

data_base[editKey] = newDict

with open("utils\data_base - Copy.json", "w") as data_baseFo:
    json.dump(data_base, data_baseFo, indent=2, separators=(',', ':  '))


print("done.")