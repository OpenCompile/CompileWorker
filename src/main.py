import os
import json
from subprocess import call
from srcmanage import SourceApp
import platform

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
        call(f"mkdir -p TarRepo/xmrig/xmrig && cp Repos/xmrig/xmrig/build/xmrig.tar.gz TarRepo/xmrig/xmrig/xmrig{xmrig.response}-{arch}.tar.gz", shell=True)
        call(f"sha256sum TarRepo/xmrig/xmrig/xmrig{xmrig.response}-{arch}.tar.gz >> TarRepo/xmrig/xmrig/SHA256SUMS.txt", shell=True)
        call(f'cd TarRepo && git pull origin main && git add . && git commit -m "Updating xmrig to {xmrig.response}" && git push origin main', shell=True)
        call(f"rm -rf TarRepo/tmp", shell=True)
    else:
       print("First run 'make init'")
       exit()
if __name__ == "__main__":
    main()
