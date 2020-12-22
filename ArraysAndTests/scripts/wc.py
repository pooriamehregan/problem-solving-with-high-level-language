#!/usr/bin/env python3

from sys import argv
import os


def main():
    """ This function checks if any command line args were given and handles 3 separate cases.
    '*': if arg is asterisk, calls another function to print char, word and line of each file in current dir.
    '*...' : if called with some extension like *.py, calls another function to only print num of char, word and lines
        of files in current dir which end with this extension.
    'file name' : if a a spesific file name was given, then only that file will be processed
    """
    if len(argv) > 1:
        arg_1 = argv[1]
        if arg_1 == '*':
            # print word in afile in current dir
            dir_list = os.listdir()
            for file_name in dir_list:
                print_wc(file_name)
        elif arg_1.startswith('*'):
            ext = arg_1[1:]
            dir_list = os.listdir()
            for file_name in dir_list:
                if file_name.endswith(ext):
                    print_wc(file_name)
        else:
            print_wc(arg_1)


def print_wc(file_name):
    """
    Args:
        file_name:
            is the name of the file that we want to open and read.
    Returns:
        this function prints number of lines, words, chars and file name of the given file in the mentioned order.
    """
    if os.path.exists(file_name):
        with open(file_name) as file:
            try:
                lines = file.readlines()
                lineNum = len(lines)
                wordNum = 0
                charNum = 0

                for line in lines:
                    words = line.strip().split(" ")
                    wordNum += len(words)
                    for word in words:
                        charNum += len(word)

                print('{:04d}  {:04d}  {:04d}  {:}'.format(lineNum, wordNum, charNum, file_name))
            except:
                print("Error: Something went wrong!")


def h(*c):
    u = tuple(c)
    print(u[0])


if __name__ == '__main__':
    main()
