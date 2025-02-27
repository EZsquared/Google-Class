#!/usr/bin/env python3
import os
import sys
import shutil
import psutil
import socket

def check_reboot():
    """Returns True  if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_no_network():
    """Returns True if the root partition is full, False otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = du.free / du.total *100
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30

    if gigabytes_free < min_gb or percent_free < min_percent:
        return True

    return False


def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk='/', min_gb=2, min_percent=10)


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    if usage > 80:
        return True
    return False


def main():
    checks=[
        (check_reboot, "Reboot Required"),
        (check_cpu_usage, "CPU Usage too high!"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No Working Network"),
    ]
    everything_ok= True

    for check, msg in checks:
        if check():
            print (msg)
            everything_ok= False

    if not everything_ok:
        sys.exit(1)

    print ("Everything is OK!")
    sys.exit(0)

main()
