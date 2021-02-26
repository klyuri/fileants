#!/bin/env python3

dict_s2i = {
     '64':        64,
    '128':       128,
    '256':       256,
    '512':       512,
     '1K':      1024,
     '2K':      2048,
     '4K':      4096,
     '8K':      8192,
    '16K':     16384,
    '32K':     32768,
    '64K':     65536,
   '128K':    131072,
   '256K':    262144,
   '512K':    524288,
     '1M':   1048576,
     '2M':   2097152,
     '4M':   4194304,
     '8M':   8388608,
    '16M':  16777216,
    '32M':  33554432,
    '64M':  67108864,
   '128M': 134217728,
   '256M': 268435456,
   '512M': 536870912
   }

dict_i2s = {
          64:   '64',
         128:  '128',
         256:  '256',
         512:  '512',
        1024:   '1K',
        2048:   '2K',
        4096:   '4K',
        8192:   '8K',
       16384:  '16K',
       32768:  '32K',
       65536:  '64K',
      131072: '128K',
      262144: '256K',
      524288: '512K',
     1048576:   '1M',
     2097152:   '2M',
     4194304:   '4M',
     8388608:   '8M',
    16777216:  '16M',
    33554432:  '32M',
    67108864:  '64M',
   134217728: '128M',
   268435456: '256M',
   536870912: '512M'
   }

def head_size_to_int(head_size):
    return dict_s2i[head_size]

def head_size_to_str(head_size):
    return dict_i2s[head_size]

#verbose_value = [False]
verbose_value = [True]

def set_verbose(value):
    verbose_value[0] = value

def is_verbose():
    return verbose_value[0]

if __name__ == '__main__':
    print(head_size_to_str(1024))
    print(head_size_to_int("2K"))
    print(is_verbose())
    set_verbose(False)
    print(is_verbose())
