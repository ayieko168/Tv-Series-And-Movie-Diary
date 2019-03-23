#!/usr/bin/env python3

import os
import sys
from time import sleep

operating_system = sys.platform


print(operating_system)

def unix_setup():

    print("installing pillow module...")
    sleep(0.1)
    os.system("pip3 install pillow")
    print("done installing pillow\n\n")

    print("installing requests module...")
    sleep(0.1)
    os.system("pip3 install requests")
    print("done installing requests module\n\n")

    print("installing pygithub module...")
    sleep(0.1)
    os.system("pip3 install pygithub")
    print("done installing pygithub module\n\n")

    print("installing pynput module...")
    sleep(0.1)
    os.system("pip3 install pynput")
    print("done installing pynput module\n\n")

    print("done all operations.\nbye\n\n")


def window_setup():

    print("installing pillow module...")
    sleep(0.1)
    os.system("pip install pillow")
    print("done installing pillow\n\n")

    print("installing requests module...")
    sleep(0.1)
    os.system("pip install requests")
    print("done installing requests module\n\n")

    print("installing pygithub module...")
    sleep(0.1)
    os.system("pip install pygithub")
    print("done installing pygithub module\n\n")

    print("installing pynput module...")
    sleep(0.1)
    os.system("pip install pynput")
    print("done installing pynput module\n\n")

    print("done all operations.\nbye\n\n")


if operating_system == ('linux' or 'darwin'):
    print("running unix setup...")
    unix_setup()
elif operating_system == ('win32' or "cygwin"):
    print("running windows setup...")
    window_setup()

ex = input("Press any key to exit...")
