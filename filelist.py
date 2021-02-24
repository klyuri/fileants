#!/bin/env python3

import os

def hill_elems(hill_dir):
    for base_dir,dirs,files in os.walk(hill_dir):
        for file_name in files:
            if exclude_hidden and file_name[0] == '.':
                continue
            yield (base_dir,file_name)

def print_hill(start_dir):
    print(f"HILL '{start_dir}' :")
    for base_dir, file_name in hill_elems(start_dir):
        name = os.path.join(base_dir,file_name)
        print(f"'{base_dir}' '{file_name}' = '{name}'")

if __name__ == '__main__':

    exclude_hidden=True
    start_dir="test_data/hill1"
    print_hill(start_dir)

#Run:
#  ./filelist.py
