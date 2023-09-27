from subprocess import call
import os

class Scripts:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
    def sync_scripts(self, owner, repo):
        urlstr = f"https://{owner}/{repo}"
        command = f"git clone {urlstr}.git"
        try:
            if os.path.exists("scripts"):
                call(f"rm -rf {repo}", shell=True)
            else:
                call(command, shell=True)
        except:
            raise SystemError("Syncing build scripts failed...")