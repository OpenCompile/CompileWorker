import os
import json
from subprocess import call
from srcmanage import SourceApp
import platform
from git import Repo
import requests

fi = json.load(open("config.json"))

def main():
    arch = fi["arch"]

    MKFLAGS = f"CC={fi["gcc"]} CXX={fi["g++"]} CORES={fi["cores"]} ARCH={arch}"

    if os.path.exists("BuildScripts"):
        # Xmrig Compile
        call(f"make -f BuildScripts/Makefile.xmrig {MKFLAGS}", shell=True)

    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()