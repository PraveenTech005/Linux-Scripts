#!/bin/env

import subprocess

subprocess.call("if [ ! -e lastupdated.txt ]; then touch lastupdated.txt; echo '0000000' > lastupdated.txt; fi", shell=True) 

file=subprocess.getoutput("cat lastupdated.txt")
date=int(subprocess.getoutput("date +%d"))
month=subprocess.getoutput("date +%m")

if date in (1, 7, 14, 21, 28) or date - int(file) >= 7:
    if (date != file):
        print("Initializing Automatic Update & Upgrade ...")
        subprocess.call("date +%d > lastupdated.txt", shell=True)
        subprocess.call("sudo apt update && sudo apt upgrade", shell=True)

subprocess.call("clear", shell=True)
subprocess.call("neofetch", shell=True)
print(f"Distro Updated And Upgraded at {file}/{month}",  end="\n")
