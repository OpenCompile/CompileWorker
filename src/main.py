import os
import json
from sync import Scripts
from conn import SourceApp
from subprocess import call

def main():
    script = Scripts("OpenCompile", "BuildScripts")

    if os.path.isfile("config/src.json"):
        pass
    else:
        print("Creating Source list...")
        
if __name__ == "__main__":
    main()