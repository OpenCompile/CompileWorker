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
            self.build(repo)
    def sync_repo(self, repo):
        try:
            call(f"git clone https://github.com/{repo}/git", shell=True)
        except:
            raise SystemError("Something bad happened...")