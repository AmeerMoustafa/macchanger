#!/usr/bin/env python3

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Specify an Interface")
    parser.add_argument("-m","--mac",dest="new_mac",help="Specify the new mac")
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-]Please specify an Interface, use -h for more info")
    elif not args.new_mac:
        parser.error("[-]Please Specify a mac address, use -h for more info")
    return args

def change_mac(interface, new_mac):
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])
    print("[+] Changing MAC address of " + interface + " To " + new_mac)

args = get_arguments()
change_mac(args.interface, args.new_mac)