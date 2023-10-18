from srcmanage import SourceApp
from subprocess import call
import requests
import json
import platform
"""
    I2PD
    building script
"""

arch = platform.machine()

l = json.loads(open("BuildScripts/list.json", "r").read())

xmrig = SourceApp(l["xmrig"])

xmrig.response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
xmrig.response = xmrig.response.json()["name"]

response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
call(f"BuildScripts/xmrig/xmrig/build.sh", shell=True)
call(f"cp Repos/xmrig/xmrig/build/xmrig.tar.gz TarRepo/xmrig/xmrig/xmrig{xmrig.response}-{arch}.tar.gz", shell=True)
call(f"sha256sum TarRepo/xmrig/xmrig/xmrig{xmrig.response}-{arch}.tar.gz >> TarRepo/xmrig/xmrig/SHA256SUMS.txt", shell=True)
call(f'cd TarRepo && git pull origin main && git add . && git commit -m "Updating xmrig to {xmrig.response}" && git push origin main', shell=True)
