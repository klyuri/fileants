#!/bin/env python3

import os
import hashlib

import ant_list
import ant_idx
from   ant_opt import *

ants_db={}

def add_hill(hill_name, hill_path):
    ants_db[hill_name]=({},hill_path)

def hill_add_ant(hill_name, ant_size, ant_h_sz, ant_h_idx, ant_a_idx, ant_name):
    if is_verbose:
        hss = head_size_to_str(ant_h_sz)
        print(f"{ant_size:12} {hss:>4} {ant_h_idx} {ant_a_idx} {ant_name}")

    if not ant_size in ants_db[hill_name][0]:
        ants_db[hill_name][0][ant_size]=[]
    ants_db[hill_name][0][ant_size].append((ant_h_sz,ant_h_idx,ant_a_idx,ant_name))

from pprint import pprint

def ants_view():
    pprint(ants_db)

if __name__ == '__main__':

    start_dir = "test_data/hill1"
    #head_size = head_size_to_int("512")
    head_size = head_size_to_int("1K")
    #head_size = head_size_to_int("64K")
    #head_size = head_size_to_int("1M")
    #head_size = head_size_to_int("8M")
    #head_size = head_size_to_int("256M")
    is_verbose=True

    add_hill("hill1",start_dir)

    for base_dir, file_name in ant_list.hill_elems(start_dir):
        sz,h,a = ant_idx.create_ant_idx(base_dir,file_name,is_head=True,head_size=head_size,is_all=True)
        # hss = head_size_to_str(head_size)
        # print(f"{sz:12} {hss:>4} {h} {a} {base_dir}/{file_name}")
        hill_add_ant("hill1",sz,head_size,h,a,base_dir+"/"+file_name)

    ants_view()
