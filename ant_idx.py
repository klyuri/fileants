#!/bin/env python3

import os
import hashlib

def ant_head_idx(ant_full_name, head_size=1024):
    head_hash = hashlib.md5()
    with open(ant_full_name, "rb") as f:
        head_hash.update(f.read(head_size))
        return head_hash.hexdigest()

def ant_all_idx(ant_full_name):
    all_hash = hashlib.sha1()
    with open(ant_full_name, "rb") as f:
        while True:
            chank = f.read(1024*1024)
            if not chank:
                break
            all_hash.update(chank)
        return all_hash.hexdigest()

def create_ant_idx(hill_name, ant_name, is_head=False, head_size=1024, is_all=False):

    elem_name = os.path.join(hill_name,ant_name)

    elem_size = os.stat(elem_name).st_size

    if is_head:
        elem_head = ant_head_idx(elem_name,head_size)
    else:
        elem_head = "--------------------------------"

    if is_all:
        elem_all = ant_all_idx(elem_name)
    else:
        elem_all = "----------------------------------------"

    return (elem_size, elem_head, elem_all)

if __name__ == '__main__':

    import ant_list
    from   ant_opt import *

    start_dir = "test_data/hill1"

    for base_dir, file_name in ant_list.hill_elems(start_dir):
        sz,h,a = create_ant_idx(base_dir, file_name, is_head=True, is_all=True)
        hss = head_size_to_str(1024)
        print(f"{sz:12} {hss:>4} {h} {a} {base_dir}/{file_name}")
