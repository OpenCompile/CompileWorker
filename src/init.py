from subprocess import call
from git import Repo
import json

f = open("config.json")
f = json.load(f)

#call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
try:
    Repo.clone_from(f"https://github.com/{f[scriptrepo]}", srepo)
except:
    print("Somthing happed skipping..")
#call("git clone git@github.com:openssl/openssl.git Repos/openssl", shell=True)
try:
    Repo.clone_from(f"https://github.com/{f['openssl']['repo']}", "Repos/openssl", branch=f["openssl"]["branch"])
    call("bash src/buildssl.sh", shell=True)
except:
    print("Something happend skipping...")
#call("git clone git@github.com:OpenCompile/TarRepo.git", shell=True)
try:
    Repo.clone_from(f"git@github.com:{f['finalrepo']}", "TarRepo")
except:
    repo = Repo("TarRepo")
    o = repo.remotes.origin.pull()
    print("Repo already exists pulling changes...")