from tkinter import messagebox
from github import Github
from ast import literal_eval
import urllib.request
import json
import checker

with open("details.json", "r") as f:
    details_data = json.load(f)
try:
    _pass = checker.decoder(details_data["pas"])
except ValueError :
    _pass = ''

use = details_data["use"]

g = Github(use, _pass, timeout=10)


def signin(username, password):

    global g

    g = Github(username, password)


def test_signin():

    global g

    for repo in g.get_user().get_repos():
        print(repo.name)


def get_user():

    global g

    up = g.get_user().login

    return up


def push_up():
    """call back function for pushing the json list to github"""
    global g

    q = messagebox.askquestion("QUESTION", "ARE YOU SURE YOU WANT TO MAKE THESE CHANGES PERMANENT")

    if q == 'yes':

        try:
            global g

            with open('series_table.json') as series_fo:  # initial reading of json data for series
                series_data = series_fo.read()
            with open("details.json") as details_fo:
                cur_details_data = details_fo.read()
            with open("Other_title_categories.json") as otherfo:
                other_category_data = otherfo.read()

            try:
                """try to update series and details json files in the tv-series-data repo"""
                print("initial try to push necessary file")
                user = g.get_user().login
                repo = g.get_repo("{}/Tv-series-data".format(user))
                # work on series table
                print("pushing seriaes table")
                series_json_content = repo.get_file_contents("series_table.json")
                repo.update_file("series_table.json", "update", str(series_data), sha=series_json_content.sha)
                # work on details json
                print("pushing details file")
                details_json_content = repo.get_file_contents("details.json")
                repo.update_file("details.json", "update", str(cur_details_data), sha=details_json_content.sha)
                # work on other categories
                print("pushing other categories table")
                other_json_content = repo.get_file_contents("Other_title_categories.json")
                repo.update_file("Other_title_categories.json", "update", str(other_category_data), sha=other_json_content.sha)

                print("done pushung\n")
                print("done all operations \n")
                messagebox.showinfo("DONE", 'DONE UPLOADING THE SERIES FILE')
            except Exception as e:
                e = literal_eval(str(e).strip('1234567890').strip())['message']
                if e == "Requires authentication":
                    print("Login first")
                    messagebox.showerror("LOGING CREDENTIALS ERROR",
                                         "Try And Log-In or Sign-In To Upload Your Data To Your Account".title())

                elif e == "Not Found":
                    try:
                        print("Not found exception")
                        user_login = g.get_user().login
                        user = g.get_user()
                        # create the repo and files with basic content
                        print("cerating TV-series-data repo for user : {}".format(user_login))
                        repo = user.create_repo("Tv-series-data")  # creating the new repo
                        print("repo now created as :: {}\nNow creatin files details and series table".format(
                            repo.full_name))
                        # create sereas json
                        repo.create_file("series_table.json", "First creation of files",
                                         series_data)
                        # create the details json
                        repo.create_file("details.json", "First creation of files",
                                         cur_details_data)
                        repo.create_file("Other_title_categories.json", "First creation of files",
                                         "{\"complete\": {}, \"wish_list\": {}, \"movies\": {}, \"on_break\": {}}")

                        print("done")

                        print("done all operations \n")
                    except Exception as e2:
                        e2 = literal_eval(str(e2).strip('1234567890').strip())["errors"][0]
                        if (e2["resource"] == "Repository") and (
                                e2["message"] == "name already exists on this account"):
                            print("repo exists,now inside e2")
                            user = g.get_user().login
                            # create the repo and files with basic content
                            repo = g.get_repo("{}/Tv-series-data".format(user))
                            print("Now creatin files details and series table")
                            try:
                                """create only the json files"""
                                repo.create_file("series_table.json", "First creation of files",
                                                 series_data)  # create the series_table json
                                repo.create_file("details.json", "First creation of files",
                                                 cur_details_data)  # create the details json
                                print("done")
                                print("done all operations \n")
                            except:
                                try:
                                    """now create ony series table"""
                                    repo.create_file("series_table.json", "First creation of files",
                                                     series_data)  # create the series_table json
                                    print("done")
                                    print("done configuring files and uploading\n")
                                except:
                                    try:
                                        """now create only deatils json"""
                                        repo.create_file("details.json", "First creation of files",
                                                         cur_details_data)  # create the details json
                                        print("done")
                                        print("done all operations \n")
                                    except:
                                        try:
                                            repo.create_file("Other_title_categories.json", "First creation of files",
                                                             "{\"complete\": {}, \"wish_list\": {}, \"movies\": {}, \"on_break\": {}}")
                                            print("done")
                                            print("done all operations \n")
                                        except Exception as allexcept:
                                            print(" end of all exceptions error :: ", allexcept)
                        else:
                            print("else exception : {}".format(e2))

                else:
                    print("exception error :: " + e)
        except Exception as epull:
                print(epull)

    elif q == 'no':
        print('no push')

    else:
        pass


def pull_down():
    """call back function that pulls available json list from github"""
    with open("details.json", "r") as pull_f:
        pull_details_data = json.load(pull_f)

    q = messagebox.askquestion("QUESTION", "DO YOU WANT TO\n PROCEED WITH THE DOWNLOAD")

    if q == 'yes':
        try:

            signin(pull_details_data["use"],
                   checker.decoder(pull_details_data["pas"]))  # SIGN IN TO GITHUB USING STORED USER CREDENTIALS

            try:
                """try to downlaod "details" and "series_table" json files from tv series data"""
                user = g.get_user().login
                repo = g.get_repo("{}/Tv-series-data".format(user))
                details_contents = repo.get_file_contents("details.json")
                details_contents_url = details_contents.download_url
                tv_series_contents = repo.get_file_contents("series_table.json")
                tv_series_contents_url = tv_series_contents.download_url
                other_categories_contents = repo.get_file_contents("Other_title_categories.json")
                other_categories_contents_url = other_categories_contents.download_url

                print("downloading files")
                urllib.request.urlretrieve(tv_series_contents_url, filename="series_table.json")
                urllib.request.urlretrieve(details_contents_url, filename="details.json")
                urllib.request.urlretrieve(other_categories_contents_url, filename="Other_title_categories.json")

                print("\nunder normal loop")
                print("done all operations")
            except Exception as e:
                e = literal_eval(str(e).strip('1234567890').strip())['message']
                if e == "Not Found":  # if The Tv-series-data repo doesent exist create one and add necessary json files
                    print("Not found exception")
                    user_login = g.get_user().login
                    user = g.get_user()
                    # create the repo and files with basic content
                    print("cerating TV-series-data repo for user : {}".format(user_login))
                    repo = user.create_repo("Tv-series-data")  # creating the new repo
                    print(
                        "repo now created as :: {}\nNow creatin files details and series table".format(repo.full_name))
                    # create the series_table json
                    repo.create_file("series_table.json", "First creation of files",
                                     "{}")
                    # create the series_table json
                    repo.create_file("details.json", "First creation of files",
                                     "{\"use\": \"\", \"pas\": [], \"state\": \"False\"}")
                    # create the other categories json
                    repo.create_file("Other_title_categories.json", "First creation of files",
                                     "{\"complete\": {}, \"wish_list\": {}, \"movies\": {}, \"on_break\": {}}")
                    print("done")
                    # download the files
                    details_contents = repo.get_file_contents("details.json")
                    details_contents_url = details_contents.download_url
                    tv_series_contents = repo.get_file_contents("series_table.json")
                    tv_series_contents_url = tv_series_contents.download_url
                    other_categories_contents = repo.get_file_contents("Other_title_categories.json")
                    other_categories_contents_url = other_categories_contents.download_url

                    # downloading the files
                    print("downloading files")
                    urllib.request.urlretrieve(tv_series_contents_url, filename="series_table.json")
                    urllib.request.urlretrieve(details_contents_url, filename="details.json")
                    urllib.request.urlretrieve(other_categories_contents_url, filename="Other_title_categories.json")

                    print("\nunder not found repo")
                    print("done all operations")

                    messagebox.showinfo("INFO", "DONE DOWNLOADING FILES")
                else:
                    if e == "Requires authentication":
                        print("Login first")
                        messagebox.showerror("LOGING CREDENTIALS ERROR",
                                             "Try And Log-In or Sign-In To Upload Your Data To Your Account".title())
                    else:
                        print("else statement exception :: {}".format(e))
        except Exception as epull:
            print(epull)

    elif q == 'no':
        print('no pull')
    else:
        pass




