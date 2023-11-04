from subprocess import call
import os
import requests
from git import Repo

class SourceApp:
    def __init__(self, repo):
        self.repo = repo
    def build(self, repo):
        call(f"bash BuildScripts/{repo}/build.sh", shell=True)
    
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