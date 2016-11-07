#!/usr/bin/env python

# script to get disk free space on windows
# Matthew J. Neave 7.11.16

import wmi

c = wmi.WMI()

# print off a header line

print("Drive\tFree\tTotal")

# go through each detected disk

for disks in c.Win32_LogicalDisk():
    # added this if statement because some disks come up with nothing
    if disks.FreeSpace != None:
        # the space is given in bytes
        # I'll convert this to Gb for easier reading
        free_gb = int(float(disks.FreeSpace) / 1000000000)
        space_gb = int(float(disks.Size) / 1000000000)
        # print everything off with tabs so that everything lines up
        print(disks.Caption, "\t", str(free_gb) + "Gb", "\t", str(space_gb) + "Gb")

