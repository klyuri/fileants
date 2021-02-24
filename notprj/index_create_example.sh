#!/bin/bash

if [ X"$1" == "X" ]
then
    echo "Not args"
    exit 1
fi

opt_l1=N
opt_l2=N
size_head=1K

name_f=""
sz_f=0
md5_f="--------------------------------"
sha1_f="----------------------------------------"

for_all()
{
    while read name_f ; do $1; done
}

mk_sz()
{
    sz_f=$(stat -c "%s" "$name_f")
}

mk_md5()
{
    md5_f="--------------------------------"
    if [ "$opt_l1" == "N" ] ; then return;  fi
    md5_f=$(dd if="$name_f" bs=${size_head} count=1 2>/dev/null | md5sum -b | awk '{print $1}')
}

mk_sha1()
{
    sha1_f="----------------------------------------"
    if [ "$opt_l2" == "N" ] ; then return; fi
    sha1_f=$(sha1sum "$name_f" | awk '{print $1}')
}

mk_index()
{
    #echo "file: '$1'"
    mk_sz
    mk_md5
    mk_sha1
    printf "%12d %04s %s %s %s\n" $sz_f $size_head $md5_f $sha1_f "$name_f"
}

while [ "X$1" != "X" ]
do
    case "$1" in
        "--l1")
            opt_l1=Y
            shift
        ;;
        "--l2")
            opt_l2=Y
            shift
        ;;
        *)
            find "$1" -type f -printf %p\\n | for_all mk_index
            shift
        ;;
    esac
done    
