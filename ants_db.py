#!/bin/env python3

import ant_opt

ants_db={}

def add_hill(hill_name, hill_path):
    ants_db[hill_name]=({},hill_path)

def hill_add_ant(hill_name, ant_size, ant_h_sz, ant_h_idx, ant_a_idx, ant_name):
    if ant_opt.is_verbose():
        hss = ant_opt.head_size_to_str(ant_h_sz)
        print(f"{ant_size:12} {hss:>4} {ant_h_idx} {ant_a_idx} {ant_name}")

    if not ant_size in ants_db[hill_name][0]:
        ants_db[hill_name][0][ant_size]=[]
    ants_db[hill_name][0][ant_size].append((ant_h_sz,ant_h_idx,ant_a_idx,ant_name))

def ants_view(hill_name):
    if ant_opt.is_verbose():
        print(f"HILL={hill_name}")
    hill = ants_db[hill_name][0]
    for sz in sorted(hill):
        g = hill[sz]
        for e in g:
            hsz,h,a,name = e
            hss = ant_opt.head_size_to_str(hsz)
            print(f"{sz:12} {hss:>4} {h} {a} {name}")

from pprint import pprint
def ants_pprint():
    pprint(ants_db)

if __name__ == '__main__':
    add_hill("h","basepath")
    hill_add_ant("h",8,1024,"----","++++","c_file")
    hill_add_ant("h",0,1024,"----","++++","b_file")
    hill_add_ant("h",0,1024,"----","++++","a_file")
    ants_view("h")
    ants_pprint()
