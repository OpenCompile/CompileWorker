import os
import json
from subprocess import call
from srcmanage import SourceApp

def main():

    sowner = "OpenCompile"
    srepo = "BuildScripts"

    if os.path.exists("BuildScripts"):
        l = json.loads(open("BuildScripts/list.json", "r").read())

        # xmrig
        xmrig = SourceApp(l["xmrig"])
        xmrig.repo_exists(xmrig.repo)
        xmrig.checkver(xmrig.repo)
        call(f"cp Repos/xmrig/xmrig/build/xmrig.tar.gz TarRepo/xmrig/xmrig/xmrig{xmrig.response}.tar.gz", shell=True)
        call(f"sha256sum TarRepo/xmrig/xmrig/xmrig{xmrig.response}.tar.gz >> TarRepo/xmrig/xmrig/SHA256SUMS.txt", shell=True)
    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()
