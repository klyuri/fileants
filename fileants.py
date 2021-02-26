#!/bin/env python3

import os

import ant_list
import ant_idx
import ants_db
import ant_opt

if __name__ == '__main__':

    example_hill=("hill1","test_data/hill1")

    #head_size = ant_opt.head_size_to_int("512")
    head_size = ant_opt.head_size_to_int("1K")
    #head_size = ant_opt.head_size_to_int("64K")
    #head_size = ant_opt.head_size_to_int("1M")
    #head_size = ant_opt.head_size_to_int("8M")
    #head_size = ant_opt.head_size_to_int("256M")
    ant_opt.set_verbose(False)

    hill_name,hill_path = example_hill

    ants_db.add_hill(hill_name,hill_path)

    for base_dir, file_name in ant_list.hill_elems(hill_path):
        sz,h,a = ant_idx.create_ant_idx(base_dir,file_name,is_head=True,head_size=head_size,is_all=True)
        # hss = head_size_to_str(head_size)
        # print(f"{sz:12} {hss:>4} {h} {a} {base_dir}/{file_name}")
        ants_db.hill_add_ant(hill_name,sz,head_size,h,a,base_dir+"/"+file_name)

    ants_db.ants_view()
