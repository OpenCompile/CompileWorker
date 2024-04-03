# CompileWorker
Automatic build node for mirrors.


Usage: `go run main.go manifest.json`

Example Manifest:
```json
{
    "name":"xmrig"
    "checkversion":true

    "versionapi": {
        "api":"github"
        "apiversion":"https://api.github.com/repos/xmrig/xmrig/releases/latest"
    }
    "scripts":{
        "setup":"./xmrig/setup.sh"
        "build":"./xmrig/build.sh"
        "test":"./xmrig/test.sh"
        "package":"./xmrig/package.sh"
    }
}
```
