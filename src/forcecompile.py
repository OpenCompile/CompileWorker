from srcmanage import SourceApp
from subprocess import call
import requests

"""
    I2PD
    building script
"""
response = requests.get(f"https://api.github.com/repos/xmrig/xmrig/releases/latest")
call(f"BuildScripts/xmrig/xmrig/build.sh", shell=True)
