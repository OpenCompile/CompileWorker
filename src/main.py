import os
import json
from sync import Scripts
from conn import SourceApp
from subprocess import call
import requests

def main():
    s = Scripts("OpenCompile", "BuildScripts")

    if os.path.exists("BuildScripts"):
        
        response = requests.get("https://api.github.com/repos/PurpleI2P/i2pd/releases/latest")
        print(response.json()["name"])
    else:
        call(f"git clone https://github.com/{s.owner}/{s.repo}.git", shell=True)
        
if __name__ == "__main__":
    main()