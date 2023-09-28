import os
import json
from subprocess import call
from srcmanage import SourceApp

def main():

    sowner = "OpenCompile"
    srepo = "BuildScripts"

    if os.path.exists("BuildScripts"):
        l = json.loads(open("BuildScripts/list.json", "r").read())

        # I2Pd
        i2pd = SourceApp(l["i2pd"])
        i2pd.repo_exists(i2pd.repo)
        i2pd.checkver(i2pd.repo)
    else:
        call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
        
if __name__ == "__main__":
    main()