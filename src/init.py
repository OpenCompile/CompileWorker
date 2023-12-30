from subprocess import call
from git import Repo
import json
import os

if os.path.isfile("config.json"):
    fi = json.load(open("config.json"))
else:
    print("Using default config")
    call("cp config.template.json config.json", shell=True)
    fi = json.load(open("config.json"))

scriptrepo = fi["scriptsrepo"]

#call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
try:
    Repo.clone_from(f"https://github.com/{scriptrepo}.git", "BuildScripts")
except:
    print("Somthing happed skipping..")

#call("git clone git@github.com:OpenCompile/TarRepo.git", shell=True)
try:
    Repo.clone_from(f"https://github.com/{fi['finalrepo']}", "TarRepo")
except:
    repo = Repo("TarRepo")
    o = repo.remotes.origin.pull()
    print("Repo already exists pulling changes...")

try:
    Repo.clone_from("https://github.com/xmrig/xmrig.git", "Repos/xmrig/xmrig")
except:
    Repo("Repos/xmrig/xmrig").remotes.origin.pull()

try:
    Repo.clone_from("https://github.com/mirror/busybox.git", "Repos/busybox")
except:
    Repo("Repos/busybox").remotes.origin.pull()