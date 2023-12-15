import os
import json
from subprocess import call
from srcmanage import SourceApp
import platform
from git import Repo
import requests

fi = json.load(open("config.json"))
C = fi["gcc"]
Cx = fi["g++"]
cores = fi["cores"]


#Versions of github projects

xmrig_ver = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest").json()['tag_name']

def main():
    arch = fi["arch"]

    MKFLAGS = f"CC={C} CXX={Cx} CORES={cores} ARCH={arch}"

    if os.path.exists("BuildScripts"):
        # Xmrig
        call("make -f BuildScripts/Makefile.xmrig pull", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig {MKFLAGS}", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig package VERSION={xmrig_ver}", shell=True)
        

    else:
       print("First run 'python3 src/init.py'")
       exit()
if __name__ == "__main__":
    main()