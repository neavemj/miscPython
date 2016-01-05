#!/usr/bin/env python

# use standard unix commands in the python shell #
# Matthew J. Neave 24.12.15

import sys
import os

# executable type file list

ext = [".py", ".sl", ".sh", ".R"]

# list function

def ls():
    files = sorted(os.listdir("."))
    for i in files:
        if i.startswith("."):
            pass
        elif os.path.isdir(i):
            print("\033[0;34m" + i + "\033[0m")
        elif i.endswith(tuple(ext)):
            print("\033[0;32m" + i + "\033[0m")
        else:
            print(i)

# print present working directory

def pwd():
    print("\033[0;33m" + os.getcwd() + "\033[0m")

# change directory

def cd(path):
    os.chdir(path)

# cat open a file and print

def cat(file_name):
    file_handle = open(file_name)
    for line in file_handle:
        line = line.strip()
        print("\033[0;32m" + line + "\033[0m")

if __name__ == '__main__':
    main()
