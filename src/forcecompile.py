from srcmanage import SourceApp
from subprocess import call
import requests
import json
"""
    I2PD
    building script
"""

l = json.loads(open("BuildScripts/list.json", "r").read())

xmrig = SourceApp(l["xmrig"])

xmrig.response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
xmrig.response = xmrig.response.json()["name"]

response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
call(f"BuildScripts/xmrig/xmrig/build.sh", shell=True)
call(f"cp Repos/xmrig/xmrig/build/xmrig.tar.gz TarRepo/xmrig/xmrig/xmrig{xmrig.response}.tar.gz", shell=True)
call(f"sha256sum TarRepo/xmrig/xmrig/xmrig{xmrig.response}.tar.gz >> TarRepo/xmrig/xmrig/SHA256SUMS.txt", shell=True)
call(f'cd TarRepo && git add . && git commit -m "Updating xmrig to {xmrig.response}" && git push origin main', shell=True)
