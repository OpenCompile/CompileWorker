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


def push_code(package, ver):
    repo = Repo("TarRepo")
    repo.index.add('**')
    repo.index.commit(f"Updating {package} to {ver}")
    repo.remotes.origin.push()


#Versions of github projects

xmrig_ver = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest").json()['tag_name']

def main():

    try:
        Repo.clone_from("https://github.com/xmrig/xmrig.git", "Repos/xmrig/xmrig")
    except:
        Repo("Repos/xmrig/xmrig").remotes.origin.pull()
    arch = fi["arch"]

    if fi["isalpine"]:
        MKFLAGS = f"CC={C} CXX={Cx} CORES={cores} ARCH={arch} SYS=alpine"
    else:
        MKFLAGS = f"CC={C} CXX={Cx} CORES={cores} ARCH={arch}"

    if os.path.exists("BuildScripts"):
        # Xmrig
        call("make -f BuildScripts/Makefile.xmrig pull", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig {MKFLAGS}", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig package VERSION={xmrig_ver}", shell=True)
        push_code("xmrig", xmrig_ver)
        

    else:
       print("First run 'python3 src/init.py'")
       exit()
if __name__ == "__main__":
    main()