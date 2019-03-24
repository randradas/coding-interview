#!/usr/bin/env python3

import os


def get_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    return files


def main():
    files = get_files("/home/robertoandradas")
    hasht = {}

    for file in files:
        for c in file:
            if c in hasht.keys():
                hasht[c] += 1
            else:
                hasht[c] = 1

    print(hasht)


if __name__ == "__main__":
    main()
