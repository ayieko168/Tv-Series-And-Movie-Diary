
from tkinter import *
from tkinter import ttk, messagebox
import gitup
from github import Github
from ast import literal_eval
import urllib.request
import webbrowser
import json
import checker


def login_UI():

    with open('details.json') as f:
        details_dict = json.load(f)

    login_window = Toplevel(bg="white")

    global user_nameent_var, passwordent_var

    remember_mecheck_var = BooleanVar()
    remember_mecheck_var.set(True)
    user_nameent_var = StringVar()
    passwordent_var = StringVar()

    # bind functions
    def download_data():
        g = Github(user_nameent_var, passwordent_var)
        try:
            """try to downlaod "series_table" json files from tv series data"""
            user = g.get_user().login
            repo = g.get_repo("{}/Tv-series-data".format(user))
            tv_series_contents = repo.get_file_contents("series_table.json")
            tv_series_contents_url = tv_series_contents.download_url

            print("downloading files")
            urllib.request.urlretrieve(tv_series_contents_url, filename="series_table.json")

            print("done downloading")
        except Exception as e:
            e = literal_eval(str(e).strip('1234567890').strip())['message']
            print(e)

    def showpass():
        """call back for show and hide button"""

        if password_showbut.cget('text') == 'show':

            passwordent.config(show='')
            password_showbut.config(text='hide')

        elif password_showbut.cget('text') == 'hide':

            passwordent.config(show='*')
            password_showbut.config(text='show')

    def signin():
        """call back for sign in button"""

        global signed_inlb_var, user_nameent_var, passwordent_var

        with open('series_table.json') as f:  # initial reading of json data for series
            data = json.load(f)

        if len(user_nameent.get()) and len(passwordent.get()) >= 1:  # test if all fields are filled
            user_nameent_var = user_nameent.get()
            passwordent_var = passwordent.get()

            try:
                """try to sign in to github using provided cridentials"""
                gitup.signin(user_nameent_var, passwordent_var)
                gitup.test_signin()

                if remember_mecheck_var.get() == True:
                    """if rememer me is true, store the cridentials in details json file"""
                    details_dict["use"] = user_nameent_var
                    details_dict["pas"] = checker.encoder(passwordent_var)

                    with open('details.json', "w") as f:
                        json.dump(details_dict, f, indent=2)

                login_window.destroy()
                print("downloading the series list")
                download_data()

            except Exception as e:
                gitup.signin(gitup.use, gitup._pass)
                e = literal_eval(str(e).strip('1234567890').strip())['message']
                print(e)
                if e == 'Bad credentials':
                    messagebox.showerror(' LOGIN ERROR ', 'Try Again \n You Entered {}'.format(e), parent=login_window)

        elif len(user_nameent.get()) and len(passwordent.get()) <= 1:  # if not :

            print(None)
            return None

    def sign_up():

        info = messagebox.askokcancel("NOTE", "After creation of the account,\ndont forget to VERIFY your account,\nvia the used email address", parent=login_window)
        print(info)
        if info == True:
            webbrowser.open_new_tab('https://github.com/join')
            messagebox.showinfo("INFO",
                                "I Just Cant Stress Enough\nHow Important It is That You Verify Your Email Address",
                                parent=login_window)

    # widgets
    user_namelb = Label(login_window, text='UserName/Email : ', bg="white")
    user_namelb.grid(row=1, column=1, padx=10, pady=20)

    user_nameent = Entry(login_window, width=40, bg="white")
    user_nameent.grid(row=1, column=2)

    passwordlb = Label(login_window, text='Password : ', bg="white")
    passwordlb.grid(row=2, column=1, sticky=E, ipadx=10)

    passwordent = Entry(login_window, width=30, show='*', bg="white")
    passwordent.grid(row=2, column=2, sticky=W)

    password_showbut = Button(login_window, text='show', command=showpass, bg="white")
    password_showbut.grid(row=2, column=2, sticky=E)

    sep1 = ttk.Separator(login_window)
    sep1.grid(row=3, column=1, columnspan=4, padx=5, pady=5, sticky=E+W)

    remember_melb = Label(login_window, text='Remember Me', bg="white")
    remember_melb.grid(row=4, column=2, sticky=W, padx=28)

    remember_mecheck = Checkbutton(login_window, variable=remember_mecheck_var, bg="white")
    remember_mecheck.grid(row=4, column=2, sticky=W)

    sign_inlb = Button(login_window, text='Sign In', command=signin, bg="white")
    sign_inlb.grid(row=5, column=2, sticky=W, ipadx=10, pady=10, padx=30)

    sign_uplb = Button(login_window, text='Sign Up', command=sign_up, bg="white")
    sign_uplb.grid(row=5, column=2, sticky=E, ipadx=10, pady=10, padx=30)

    login_window.geometry('400x200')
    login_window.title("account details")
    login_window.resizable(width=0, height=0)


