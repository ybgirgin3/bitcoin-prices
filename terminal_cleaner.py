# -*- coding: utf8 -*-
# Filename terminal_cleaner.py

"""
this module cleans termianl
"""


import platform as plt
import os

# terminal screen cleaner
def clear_terminal():
    if plt.system() == "Windows":
        os.system("cls")      # for windows
    else:
        os.system("clear")    # for linux and macos

# end file
