

from tkinter import *
from time import sleep
from tkinter import ttk

def login_UI():

    login_window = Tk()

    # bind functions
    
    def showpass():
        
        if password_showbut.cget('text') == 'show':

            passwordent.config(show='')
            password_showbut.config(text='hide')
            
        elif password_showbut.cget('text') == 'hide':

            passwordent.config(show='*')
            password_showbut.config(text='show')

    def signin():

        if len(user_nameent.get()) and len(passwordent.get()) >= 1:

            user_nameent_var = user_nameent.get()
            passwordent_var = passwordent.get()

            print(user_nameent_var)
            print(passwordent_var)

        elif len(user_nameent.get()) and len(passwordent.get()) <= 1:

            print('None')

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

    remember_mecheck = Checkbutton(login_window)
    remember_mecheck.grid(row=4, column=2, sticky=W)

    sign_inlb = Button(login_window, text='Sign In', command=signin)
    sign_inlb.grid(row=5, column=2, sticky=W, ipadx=10, pady=10, padx=30)

    sign_uplb = Button(login_window, text='Sign Up')
    sign_uplb.grid(row=5, column=2, sticky=E, ipadx=10, pady=10, padx=30)


    login_window.geometry('400x200')



login_UI()
