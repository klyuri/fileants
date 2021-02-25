#!/bin/env python3

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
    add_hill("a","basepath")
    hill_add_ant("a",0,1024,"----","++++","exmaple")
    ants_view()
