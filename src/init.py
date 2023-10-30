from subprocess import call
from git import Repo

sowner = "OpenCompile"
srepo = "BuildScripts"
#call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
try:
    Repo.clone_from(f"https://github.com/{sowner}/{srepo}", srepo)
except:
    print("Somthing happed skipping..")
#call("git clone git@github.com:openssl/openssl.git Repos/openssl", shell=True)
try:
    Repo.clone_from(f"https://github.com/openssl/openssl.git", "Repos/openssl")
    call("bash src/buildssl.sh", shell=True)
except:
    print("Something happend skipping...")
#call("git clone git@github.com:OpenCompile/TarRepo.git", shell=True)
try:
    Repo.clone_from(f"git@github.com:OpenCompile/TarRepo.git", "TarRepo")
except:
    repo = Repo("TarRepo")
    o = repo.remotes.origin.pull()
    print("Repo already exists pulling changes...")