from srcmanage import SourceApp
from subprocess import call
import requests

"""
    I2PD
    building script
"""
response = requests.get(f"https://api.github.com/repos/PurpleI2P/i2pd/releases/latest")
call(f"BuildScripts/PurpleI2P/i2pd/build.sh", shell=True)