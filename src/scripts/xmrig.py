import requests
from subprocess import call
from git import Repo
import json

arch = json.load(open("config.json"))["arch"]

def xmrig_push():
    response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
    response = response.json()['tag_name']
    call(f"mkdir -p TarRepo/xmrig/xmrig/{response}/",  shell=True)
    call(f"cp Repos/xmrig/xmrig/build/xmrig TarRepo/xmrig/xmrig/{response}/xmrig-{arch} && pwd && cd TarRepo/xmrig/xmrig/{response} && sha256sum xmrig-{arch} > SHA256SUMS.txt && cd ../../../", shell=True)
    repo = Repo("TarRepo")
    repo.index.add('**')
    repo.index.commit(f"Updating xmrig to {response}")
    repo.remotes.origin.push()