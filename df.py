#!/usr/bin/env python

# script to get disk free space on windows
# Matthew J. Neave 7.11.16

import wmi

c = wmi.WMI()

print("Drive\tFree\tTotal")

for disks in c.Win32_LogicalDisk():
    if disks.FreeSpace != None:
        free_gb = int(float(disks.FreeSpace) / 1000000000)
        space_gb = int(float(disks.Size) / 1000000000)
        print(disks.Caption, "\t", str(free_gb) + "Gb", "\t", str(space_gb) + "Gb")

