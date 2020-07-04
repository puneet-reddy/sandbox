#!/usr/bin/env python

'''
Useful little script to get the size of a directory
It's faster than the windows `properties` size lookup.
'''

import os
import sys


def get_directory_size(directory, verbose=False):
    """Returns the `directory` size as an int in bytes."""
    total = 0
    try:
        if verbose:
            print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path, verbose=verbose)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        total = os.path.getsize(directory)
    except PermissionError:
        if verbose:
            print("[-] Could not access", directory)
        total = 0
    return total


def human_readable(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python {} <directory path>".format(__file__))
        sys.exit(0)

    print(human_readable(get_directory_size(sys.argv[1])))
