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
        call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
        call("git clone git@github.com:openssl/openssl.git Repos/openssl", shell=True)
        call("bash src/buildssl.sh", shell=True)
        
if __name__ == "__main__":
    main()
