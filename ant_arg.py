#!/bin/env python3

import sys
import argparse
from pprint import pprint

def ant_arg(argv):
    parser = argparse.ArgumentParser(description = 'Programm fileants')
    parser.add_argument('-v', '--verbose', help='verbose logging',
                        action='store_true')
    parser.add_argument('-d', '--head-sz',help = 'head size 64-..-1K-..-1M-..-512M (2**n)',
                        type=str, default = "1M")
    parser.add_argument('-1', '--l1', help='run level 1',
                        action='store_true')
    parser.add_argument('-2', '--l2', help='run level 2',
                        action='store_true')
    parser.add_argument('path', type=str, help='path')
    return parser.parse_args(argv)


if __name__ == '__main__':
    # ./ant_arg.py --arg-str "My string" --arg-int 128 x.txt y.txt z.txt
    argv0 = ['./ant_arg.py',
            '-v',
            '-d', '1K',
            '-1',
            'test_data/hill1'
            ]

    print(argv0);

    argv = argv0[1:]

    print(argv)

    args = ant_arg(argv)

    print(args)
# print(args.indir)
