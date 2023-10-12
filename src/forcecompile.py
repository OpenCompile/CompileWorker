from srcmanage import SourceApp
from subprocess import call


"""
    I2PD
    building script
"""
call(f"bash BuildScripts/PurpleI2P/i2pd/build.sh", shell=True)
call(f"patch Repos/PurpleI2P/i2pd/debian/control < control.patch", shell=True)
