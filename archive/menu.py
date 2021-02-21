import os
import sys
# import morse
import argparse
import baseDecode
from morse import decrypt

def menuOption():    
    parser = argparse.ArgumentParser(description="A CTF multi-tool")
    parser.add_argument("-b", "--base", help="Enter the base encoded string", dest="base", type=str, required=False)
    parser.add_argument("-m", "--morse", help="Decode a string of morse code", dest="morse", type=str, required=False)
    args =  parser.parse_args()

    baseDecode.decodeBase64(args)
    decrypt(args)
# def help_menu():
#     print(f'This is the help page... I am here to help you because you can not read! ')
# help_menu()