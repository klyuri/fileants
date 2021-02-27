#!/bin/env python3

import os
import sys

import ant_list
import ant_idx
import ants_db
import ant_opt
import ant_arg

if __name__ == '__main__':

    argv0 = ['./ant_arg.py',
            #'-v',
            #'-d', '512',
            '-d', '1K',
            #'-d', '64K',
            #'-d', '1M',
            '-1',
            '-2',
            'test_data/hill1'
            ]

    mydebug = True
    mydebug = False

    if mydebug:
        argv = argv0[1:]
    else:
        argv = sys.argv[1:]

    args = ant_arg.ant_arg(argv)
    #print (args)

    example_hill=("hill1",args.path)

    head_size = ant_opt.head_size_to_int(args.head_sz)
    ant_opt.set_verbose(args.verbose)

    hill_name,hill_path = example_hill

    ants_db.add_hill(hill_name,hill_path)

    for base_dir, file_name in ant_list.hill_elems(hill_path):
        sz,h,a = ant_idx.create_ant_idx(base_dir,file_name,is_head=args.l1,head_size=head_size,is_all=args.l2)
        # hss = head_size_to_str(head_size)
        # print(f"{sz:12} {hss:>4} {h} {a} {base_dir}/{file_name}")
        ants_db.hill_add_ant(hill_name,sz,head_size,h,a,base_dir+"/"+file_name)

    ants_db.ants_view(hill_name)
    if(ant_opt.is_verbose()):
        ants_db.ants_pprint()
