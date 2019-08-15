# ADAGIO Structural Analysis of Android Binaries
# Copyright (c) 2015 Hugo Gascon <hgascon@mail.de>


import sys
import os
# sys.path.insert(0, os.path.abspath("modules/androguard"))

import argparse
from adagio.core.graphs import process_dir

def print_logo():
    print("""
                _             _
               | |           (_)
       __ _  __| | __ _  __ _ _  ___
      / _` |/ _` |/ _` |/ _` | |/ _ \\
     | (_| | (_| | (_| | (_| | | (_) |
      \__,_|\__,_|\__,_|\__, |_|\___/
                         __/ |
                        |___/   
            """)


def exit():
    print_logo()
    parser.print_help()
    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Structural Analysis of\
                                                  Android Binaries')

    parser.add_argument("-c", "--conf", default="adagio/conf",
                        help="Change default directory for configuration files.\
                        If no directory is given, the files from 'adagio/conf'\
                        will be read.")

    parser.add_argument("-d", "--dir", default="",
                        help="Load APK/DEX files from this directory.")

    parser.add_argument("-o", "--out", default="",
                        help="Select output directory for generated graphs.\
                        If no directory is given, they will be written\
                        to the data/fcg or data/pdg directory.")

    fcga = parser.add_argument_group('CALL GRAPH ANALYSIS')
    fcga.add_argument("-f", "--fcgraphs", action="store_true",
                     help="Extract function call graphs from all APK/DEX files\
                     in the given directory.")

    pdga = parser.add_argument_group('PROGRAM DEPENDENCY GRAPH ANALYSIS')
    pdga.add_argument("-p", "--pdgraphs", action="store_true",
                      help="Extract program dependecy graphs from all APK/DEX\
                      files in the given directory.")

    args = parser.parse_args()
    path_conf = os.path.realpath(args.conf)

    out = args.out
    mode = ""
    if args.fcgraphs:
        if not args.out:
            out = os.path.realpath("data/fcg")
        mode='FCG'

    elif args.pdgraphs:
        if not args.out:
            out = os.path.realpath("data/pdg")
        mode ='PDG'

    if mode:
        print_logo()
        process_dir(args.dir, out, mode)

    else:
        exit()
