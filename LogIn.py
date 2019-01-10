
from tkinter import *
from tkinter import ttk, messagebox
import gitup
from ast import literal_eval
import webbrowser
import json
import checker


def login_UI():

    with open('details.json') as f:
        details_dict = json.load(f)

    login_window = Toplevel()

    remember_mecheck_var = BooleanVar()

    # bind functions
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

        global signed_inlb_var

        with open('series_table.json') as f:  # initial reading of json data for series
            data = json.load(f)

        if len(user_nameent.get()) and len(passwordent.get()) >= 1:  # test if all fields are filled

            user_nameent_var = user_nameent.get()
            passwordent_var = passwordent.get()

            try:
                gitup.signin(user_nameent_var, passwordent_var)
                gitup.test_signin()

                if remember_mecheck_var.get() == True:
                    details_dict["use"] = user_nameent_var
                    details_dict["pas"] = checker.encoder(passwordent_var)

                    with open('details.json', "w") as f:
                        json.dump(details_dict, f, indent=4)

                    login_window.destroy()

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

        webbrowser.open_new_tab('https://github.com/join')


    # widgets
    user_namelb = Label(login_window, text='UserName/Email : ')
    user_namelb.grid(row=1, column=1, padx=10, pady=20)
    
    user_nameent = Entry(login_window, width=40)
    user_nameent.grid(row=1, column=2)
    
    passwordlb = Label(login_window, text='Password : ')
    passwordlb.grid(row=2, column=1, sticky=E, ipadx=10)

    passwordent = Entry(login_window, width=30, show='*')
    passwordent.grid(row=2, column=2, sticky=W)

    password_showbut = Button(login_window, text='show', command=showpass)
    password_showbut.grid(row=2, column=2, sticky=E)

    sep1 = ttk.Separator(login_window)
    sep1.grid(row=3, column=1, columnspan=4, padx=5, pady=5, sticky=E+W)

    remember_melb = Label(login_window, text='Remember Me')
    remember_melb.grid(row=4, column=2, sticky=W, padx=28)

    remember_mecheck = Checkbutton(login_window, variable=remember_mecheck_var, command=lambda: print(remember_mecheck_var.get()))
    remember_mecheck.grid(row=4, column=2, sticky=W)

    sign_inlb = Button(login_window, text='Sign In', command=signin)
    sign_inlb.grid(row=5, column=2, sticky=W, ipadx=10, pady=10, padx=30)

    sign_uplb = Button(login_window, text='Sign Up', command=sign_up)
    sign_uplb.grid(row=5, column=2, sticky=E, ipadx=10, pady=10, padx=30)

    login_window.geometry('400x200')
    login_window.title("account details")
    login_window.resizable(width=0, height=0)



