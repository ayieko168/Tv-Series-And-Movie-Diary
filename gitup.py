from tkinter import messagebox
from github import Github
from ast import literal_eval
import urllib.request

g = Github("ayieko168", "joshuambago1230Q#", timeout=10)

use = 'ayieko168'
pa = 'joshuambago1230Q#'


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

        with open('series_table.json') as f:  # initial reading of json data for series
            data = f.read()

        signin(use, pa)

        try:
            """try to create a new repo called tv series data"""
            user = g.get_user()
            repo = user.create_repo('Tv-series-data')
        except Exception as e:

            e = literal_eval(str(e).strip('1234567890').strip())['errors'][0]['message']
            if e == 'name already exists on this account':

                try:
                    """now try and create the json file"""
                    u = g.get_user().login
                    repo = g.get_repo("{}/Tv-series-data".format(u))
                    repo.create_file("series_table.json", "test", data, branch="test")
                except Exception:

                    try:
                        repo = g.get_repo("{}/Tv-series-data".format(u))
                        contents = repo.get_contents("series_table.json")
                        repo.update_file(contents.path, "more tests", data, contents.sha, branch="test")
                    except Exception:
                        pass

        messagebox.showinfo("DONE", 'DONE UPLOADING THE SERIES FILE')

    elif q == 'no':

        print('no push')

    else:

        pass


def pull_down():
    """call back function that pulls available json list from github"""

    with open('series_table.json') as f:  # initial reading of json data for series
        data = f.read()

    q = messagebox.askquestion("QUESTION", "ARE YOU SURE YOU WANT TO MAKE THESE CHANGES PERMANENT")

    if q == 'yes':

        signin(use, pa)

        try:
            """try to create a new repo called tv series data"""
            user = g.get_user()
            repo = user.create_repo('Tv-series-data')
        except Exception as e:

            try:
                """now try and create the json file"""
                u = g.get_user().login
                repo = g.get_repo("{}/Tv-series-data".format(u))
                repo.create_file("series_table.json", "test", data, branch="test")
            except Exception:
                try:
                    """download the json file"""

                    u = g.get_user().login  # login username
                    repo = g.get_repo("{}/Tv-series-data".format(u))
                    file_contents = repo.get_file_contents('series_table.json')

                    url = file_contents.download_url
                    urllib.request.urlretrieve(url, 'series_table.json')

                    messagebox.showinfo("DONE", 'DONE DOWNLOADING THE SERIES FILE')

                except Exception as e:
                    print(e)
                    messagebox.showerror("ERROR DOWNLOADING", "PLEASE CHECK YOUR INTERNET CONNECTION ")

    elif q == 'no':

        print('no push')

    else:

        pass




