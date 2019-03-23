#!/usr/bin/env python3

import os
import sys

operating_system = sys.platform


def unix_setup():

    print("installing pillow module...")
    os.system("pip3 install pillow")
    print("done installing pillow")

    print("installing requests module...")
    os.system("pip3 install requests")
    print("done installing requests module")

    print("installing pygithub module...")
    os.system("pip3 install pygithub")
    print("done installing pygithub module")

    print("done all operations.\nbye")


def window_setup():

    print("installing pillow module...")
    os.system("pip install pillow")
    print("done installing pillow")

    print("installing requests module...")
    os.system("pip install requests")
    print("done installing requests module")

    print("installing pygithub module...")
    os.system("pip install pygithub")
    print("done installing pygithub module")

    print("done all operations.\nbye")


if operating_system == 'linux' or 'darwin':
    print("running unix setup...")
    unix_setup()

elif operating_system == 'win32' or "cygwin":
    print("running windows setup...")
    window_setup()
