from subprocess import call
import os
import requests

class SourceApp:
    def __init__(self, repo):
        self.repo = repo
    def build(self, repo):
        call(f"bash BuildScripts/{repo}/build.sh", shell=True)
    def checkver(self, repo):
        response = requests.get(f"https://api.github.com/repos/{repo}/releases/latest")
        response = response.json()["name"]

        f = open(f"BuildScripts/{repo}/version", "r").read()
        if f != response:
            call(f"rm BuildScripts/{repo}/version", shell=True)

            o = open(f"BuildScripts/{repo}/version", "w")
            o.write(response)
            o.close()
            self.build(repo)
    
    def sync_repo(self, repo):
        try:
            call(f"git clone https://github.com/{repo}.git Repos/{repo}", shell=True)
        except:
            raise SystemError("Something bad happened...")
    
    def repo_exists(self, repo):
        if os.path.exists(f"Repos/{repo}"):
            pass
        else:
            self.sync_repo(repo)