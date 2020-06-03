#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF-8") as myFile:
        print(myFile.read())
