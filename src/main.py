import os
import json
from subprocess import call
from git import Repo
import requests
from time import sleep

# FTP is currently disabled.
#import io

fi = json.load(open("config.json"))

#if fi["ftp"]["enabled"]:
#    from ftplib import FTP
#    fftp = fi["ftp"]
#   ftp = FTP(fftp["host"], fftp["user"], fftp["password"], fftp["acct"])

def compile(name, version, arch, ispatched, patchfiles):
    if ispatched:
        call(f"patch {patchfiles} < patches/{name}.patch", shell=True)
    call(f"make -f BuildScripts/Makefile.xmrig", shell=True)
    call(f"make -f BuildScripts/Makefile.xmrig package VERSION={version} ARCH={arch}", shell=True)

def push_code(package, ver):
#def push_code(package, ver, file=False, name=False):
#    if file !=False and name !=False:
#        bio = io.BytesIO(open(file))
#        ftp.retrbinary(f'STOR {name}', bio)
#    else:
    repo = Repo("TarRepo")
    repo.index.add('**')
    repo.index.commit(f"Updating {package} to {ver}")
    repo.git.push("origin", fi["finalbranch"])

def send_notification(server, topic, name, version):
    if fi["ntfy"]["enabled"]:
        requests.post(f"{server}/{topic}", data=f"{name} {version} is compiled!".encode(encoding='utf-8'))

C = fi["gcc"]
Cx = fi["g++"]
cores = fi["cores"]

def main():
    
    arch = fi["arch"]

    with open('github.txt') as tok:
        token = tok.read().strip()

    headers = {'Authorization': 'token ' + token}

    if os.path.exists("BuildScripts"):
        while True:
            xmrig_ver = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest", headers=headers).json()['tag_name']
            print(xmrig_ver)
            if os.path.exists(f"TarRepo/xmrig/xmrig/{xmrig_ver}") == False:
                compile("xmrig", xmrig_ver, arch, True, "Repos/xmrig/xmrig/scripts/build.openssl.sh")
                push_code("xmrig", xmrig_ver)
                send_notification(fi["ntfy"]["server"], fi["ntfy"]["topic"], "xmrig", xmrig_ver)
            
            print("Sleeping for 1 minutes...")
            sleep(60)
    else:
       print("First run 'python3 src/init.py'")
       exit()
if __name__ == "__main__":
    main()