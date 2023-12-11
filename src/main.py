import os
import json
from subprocess import call
from srcmanage import SourceApp
import platform
from git import Repo
import requests

f = json.load(open("config.json"))

def main():
    arch = f["arch"]

    MKFLAGS = f"CC={["gcc"]} CXX={["g++"]} CORES={["cores"]} ARCH={arch}"

    if os.path.exists("BuildScripts"):
        # Xmrig Compile
        call(f"make -f BuildScripts/Makefile.xmrig {MKFLAGS}", shell=True)

    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()