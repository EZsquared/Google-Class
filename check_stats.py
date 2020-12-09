#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage

free = check_disk_usage("/")
usage = check_cpu_usage()

print("Free Disk Space: {}".format(free))
print("Current CPU Usage: {}".format(usage))

if usage > 75 or free < 20:
    print ("Error")
else:
    print ("Everything is OK!")
