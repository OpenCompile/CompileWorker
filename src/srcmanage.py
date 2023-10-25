from subprocess import call
import os
import requests
from git import Repo

class SourceApp:
    def __init__(self, repo):
        self.repo = repo
    def build(self, repo):
        call(f"export PKGVER={self.response}", shell=True)
        call(f"bash BuildScripts/{repo}/build.sh", shell=True)
    def checkver(self, repo):

        f = open(f"BuildScripts/{repo}/version", "r").read()
        self.response = f # TODO
        if f != self.response:
            call(f"rm BuildScripts/{repo}/version", shell=True)

            o = open(f"BuildScripts/{repo}/version", "w")
            o.write(self.response)
            o.close()
            self.build(repo)
            if os.path.exists(f"Build/{repo}/package.sh"):
                self.package(repo)
    
    def sync_repo(self, repo):
        try:
            #call(f"git clone https://github.com/{repo}.git Repos/{repo}", shell=True)
            Repo.clone_from(f"https://github.com/{repo}.git", f"Repos/{repo}")
        except:
            raise SystemError("Something bad happened...")
    
    def repo_exists(self, repo):
        if os.path.exists(f"Repos/{repo}"):
            pass
        else:
            self.sync_repo(repo)

    def package(self, repo):
        call(f"bash BuildScripts/{repo}/package.sh {self.response}", shell=True)