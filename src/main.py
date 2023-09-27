import os
import json
import github_conn
import requests
from subprocess import call

def main():
    e = call("pwd", shell=True)
    print(e)

if __name__ == "__main__":
    main()