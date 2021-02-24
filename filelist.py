#!/bin/env python3

import os

start_dir="test_data/hill1"

print(f"HILL '{start_dir}' :")

for base_dir,dirs,files in os.walk(start_dir):
    for file_name in files:
        name = os.path.join(base_dir,file_name)
        print(f"'{name}'")

#Run:
#  ./filelist.py
