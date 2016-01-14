#!/usr/bin/env python

# script to find recently modified files 
# from Beazley's python cookbook

import os, time

def modified_within(seconds):
    now = time.time()
    for path, dirs, files in os.walk("."):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print fullpath

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: {} seconds".format(sys.argv[0]))
        raise SystemExit(1)

    modified_within(float(sys.argv[1]))
