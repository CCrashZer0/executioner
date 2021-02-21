############Executioner#####################
#      A python utitily developed to make  #
#      solving CTF challanges easier.      #
#                                          #
#       Developed by CCrashZer0            #
#                                          #
#                                          #
############################################

import argparse
from decode import decode_string
from meta import extract_data

def menu():
    parser = argparse.ArgumentParser(description="A command line tool to automatically push completed projects to github.")
    parser.add_argument("-b", "--base", type=str, help="Input a base64 encoded string", required=False)
    parser.add_argument("-i", "--image", type=str, help="Input the path to the image you want to examine", required=False)
    args = parser.parse_args()

    if args.base:
        decode_string(args)
    if args.image:
        extract_data(args)
menu()