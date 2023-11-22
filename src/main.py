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

    if os.path.exists("BuildScripts"):
        l = json.loads(open("BuildScripts/list.json", "r").read())
        from scripts.xmrig import xmrig_push

        # xmrig
        xmrig = SourceApp(l["xmrig"])
        xmrig.repo_exists(xmrig.repo)
        xmrig.build(xmrig.repo)
        
        xmrig_push()

        call(f"rm -rf TarRepo/tmp", shell=True)
    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()