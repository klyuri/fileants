#!/bin/env python3

import os
import hashlib

import ant_list
import ant_idx
from   ant_opt import *

if __name__ == '__main__':

    start_dir = "test_data/hill1"
    #head_size = head_size_to_int("512")
    #head_size = head_size_to_int("1K")
    #head_size = head_size_to_int("64K")
    head_size = head_size_to_int("1M")
    #head_size = head_size_to_int("8M")
    #head_size = head_size_to_int("256M")

    for base_dir, file_name in ant_list.hill_elems(start_dir):
        sz,h,a = ant_idx.create_ant_idx(base_dir,file_name,is_head=True,head_size=head_size,is_all=True)
        hss = head_size_to_str(head_size)
        print(f"{sz:12} {hss:>4} {h} {a} {base_dir}/{file_name}")
