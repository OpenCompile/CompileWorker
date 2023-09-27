from subprocess import call
import os

class SourceApp:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
    def newcode(self, owner, repo):
        urlstr = f"https://github.com/{owner}/{repo}.git"
        command = f"git clone {urlstr}"
        try:
            if os.path.exists(f"{repo}"):
                call(f"rm -rf {repo}", shell=True)
            else:
                call(command, shell=True)
        except:
            print("Syncing failed...")

    def sync_scripts(self, owner, repo):
        urlstr = f"https://{owner}/{repo}"
        command = f"git clone {urlstr}.git"
        try:
            if os.path.exists("scripts"):
                call(f"rm -rf {repo}", shell=True)
            else:
                call(command, shell=True)
        except:
            print("Syncing build scripts failed...")