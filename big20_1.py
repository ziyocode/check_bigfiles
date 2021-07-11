#!/usr/bin/env python
import os
import pwd
import time
import argparse
from stat import S_ISREG

count = 20  # default count = 20

file_list = []


def find_bigfiles(sdir, count):
    for (path, dir, files) in os.walk(sdir):
        for filename in files:
            fullname = path + "/" + filename
            try:
                filestat = os.stat(fullname)
                _mode = filestat.st_mode
                if S_ISREG(_mode):
                    _size = filestat.st_size / 1024 / 1024
                    t_file = (fullname, _size)
                    file_list.append(t_file)
                else:
                    continue
            except (FileNotFoundError, PermissionError):
                pass

    sort_files = sorted(file_list, key=lambda x: (-x[1]))
    big_files = sort_files[:count]

    for fn, sz in big_files:
        _fstat = os.stat(fn)
        _time = time.localtime(_fstat.st_mtime)
        _mtime = time.strftime("%Y/%m/%d-%H:%M", _time)
        _user = pwd.getpwuid(filestat.st_uid).pw_name
        _perm = oct(_fstat.st_mode)[-3:]
        print(
            "{0:50s} {1:17s} Perm:{2:4s} User:{3:^10s} Size:{4:.3f} Mbyte".format(
                fn, _mtime, _perm, _user, sz
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sdir", type=str, help="Directory")
    parser.add_argument("-n", "--count", type=int, help="Count")
    args = parser.parse_args()

    if args.sdir is None or type(args.count) != int:
        print("Usage: python big20.py -s {dir} -n {count}")
    else:
        find_bigfiles(args.sdir, args.count)
