from subprocess import call

sowner = "OpenCompile"
srepo = "BuildScripts"
call(f"git clone https://github.com/{sowner}/{srepo}.git", shell=True)
call("git clone git@github.com:openssl/openssl.git Repos/openssl", shell=True)
call("bash src/buildssl.sh", shell=True)