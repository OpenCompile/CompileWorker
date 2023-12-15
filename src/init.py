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
    Repo.clone_from(f"git@github.com:{scriptrepo}.git", "BuildScripts")
except:
    print("Somthing happed skipping..")

#call("git clone git@github.com:OpenCompile/TarRepo.git", shell=True)
try:
    Repo.clone_from(f"git@github.com:{fi['finalrepo']}", "TarRepo")
except:
    repo = Repo("TarRepo")
    o = repo.remotes.origin.pull()
    print("Repo already exists pulling changes...")