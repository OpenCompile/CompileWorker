import os
import json
from sync import Scripts
from conn import SourceApp
from subprocess import call

def main():
    s = Scripts("OpenCompile", "BuildScripts")

    if os.path.exists("BuildScripts"):
        pass
    else:
        call(f"git clone https://github.com/{s.owner}/{s.repo}.git", shell=True)
        
if __name__ == "__main__":
    main()