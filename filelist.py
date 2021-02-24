#!/bin/env python3

import os

def print_hill(start_dir):
    print(f"HILL '{start_dir}' :")
    for base_dir,dirs,files in os.walk(start_dir):
        for file_name in files:
            name = os.path.join(base_dir,file_name)
            print(f"'{name}'")

if __name__ == '__main__':

    start_dir="test_data/hill1"
    print_hill(start_dir)

#Run:
#  ./filelist.py
