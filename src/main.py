import os
import json
from subprocess import call
from git import Repo
import requests
import io

fi = json.load(open("config.json"))

if fi["ftp"]["enabled"]:
    from ftplib import FTP
    fftp = fi["ftp"]
    ftp = FTP(fftp["host"], fftp["user"], fftp["password"], fftp["acct"])


C = fi["gcc"]
Cx = fi["g++"]
cores = fi["cores"]


def push_code(package, ver, file=False, name=False):
    if file !=False and name !=False:
        bio = io.BytesIO(open(file))
        ftp.retrbinary(f'STOR {name}', bio)
    else:
        repo = Repo("TarRepo")
        repo.index.add('**')
        repo.index.commit(f"Updating {package} to {ver}")
        repo.git.push("origin", fi["finalbranch"])

#Versions of github projects

xmrig_ver = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest").json()['tag_name']

def main():

    try:
        Repo.clone_from("https://github.com/xmrig/xmrig.git", "Repos/xmrig/xmrig")
    except:
        Repo("Repos/xmrig/xmrig").remotes.origin.pull()
    arch = fi["arch"]
    MKFLAGS = f"CC={C} CXX={Cx} CORES={cores} ARCH={arch}"

    if os.path.exists("BuildScripts"):
        # Xmrig
        call("patch Repos/xmrig/xmrig/scripts/build.openssl.sh < patches/xmrig.patch", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig {MKFLAGS}", shell=True)
        call(f"make -f BuildScripts/Makefile.xmrig package VERSION={xmrig_ver}", shell=True)
        if fi["ftp"]["enabled"]:
            push_code("xmrig", xmrig_ver, f"TarRepo/xmrig/xmrig/{xmrig_ver}", f"pub/xmrig/xmrig/{xmrig_ver}/xmrig")
        else:
            push_code("xmrig", xmrig_ver)
    else:
       print("First run 'python3 src/init.py'")
       exit()
if __name__ == "__main__":
    main()