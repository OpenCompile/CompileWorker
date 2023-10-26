import os
import json
from subprocess import call
from srcmanage import SourceApp
import platform
from git import Repo
import requests

def main():

    sowner = "OpenCompile"
    srepo = "BuildScripts"
    arch = platform.machine()

    if os.path.exists("BuildScripts"):
        l = json.loads(open("BuildScripts/list.json", "r").read())

        # xmrig
        xmrig = SourceApp(l["xmrig"])
        xmrig.repo_exists(xmrig.repo)
        xmrig.checkver(xmrig.repo)
        response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
        response = response.json()['tag_name']
        call(f"mkdir -p TarRepo/xmrig/xmrig/{response}/", shell=True)
        call(f"cp Repos/xmrig/xmrig/build/xmrig TarRepo/xmrig/xmrig/{response}/xmrig && pwd && cd TarRepo/xmrig/xmrig/{response} && sha256sum xmrig > SHA256SUMS.txt && cd ../../../", shell=True)
        repo = Repo("TarRepo")
        repo.index.add('**')
        repo.index.commit(f"Updating xmrig to {response}")
        repo.remotes.origin.push()
        call(f"rm -rf TarRepo/tmp", shell=True)
    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()
