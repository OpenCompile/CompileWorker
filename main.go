package main

import (
	"io"
    "log"
    "net/http"
	"os"
    "os/exec"
    "strings"

    "github.com/tidwall/gjson"
)

func get_version(repo string) string {
	url := "https://api.github.com/repos/" + repo + "/releases/latest"

	resp, err := http.Get(url)

	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		log.Fatal(err)
	}
	value := gjson.Get(string(body), "tag_name")

	if strings.HasPrefix(value.String(), "v") {
        return value.String()[1:]
    }
    return value.String()
}

func execute(shell string) {
    cmd := exec.Command(shell)

    output, err := cmd.Output()

    if err != nil {
        println(string(output))
        log.Fatal(err)
    }

    println(string(output))
}

func execute_multi(name string, args ...string) {
    cmd := exec.Command(name, args...)

    output, err := cmd.Output()

    if err != nil {
        println(string(output))
        log.Fatal(err)
    }

    println(string(output))
}

func build(manifest string) {
	content, err := os.ReadFile(manifest)
	if err != nil {
		log.Fatal(err)
	}

    println("[INFO] Building", gjson.Get(string(content), "name").String()) // Extract package name from manifest

    var script gjson.Result
    var system string = gjson.Get(string(content), "system").String()

    if system == "none" {
        // SETUP
	    script = gjson.Get(string(content), "scripts.setup")
        if !script.Exists() {
            println("[WARNING] setup script not found in the manifest, skipping.")
        } else {
            println("[INFO] Running setup script")
            execute(script.String())
        }

        // BUILD
        script = gjson.Get(string(content), "scripts.build")
        if !script.Exists() {
            println("[WARNING] build script not found in the manifest, skipping.")
        } else {
            println("[INFO] Running build script")
            execute(script.String())
        }

        // TEST
        script = gjson.Get(string(content), "scripts.test")
        if !script.Exists() {
            println("[WARNING] test script not found in the manifest, skipping.")
        } else {
            println("[INFO] Running test script")
            execute(script.String())
        }

        // PACKAGE
        script = gjson.Get(string(content), "scripts.package")
        if !script.Exists() {
            println("[WARNING] package script not found in the manifest, skipping.")
        } else {
            println("[INFO] Running package script")
            execute(script.String())
        }
    } else if system == "alpine" {
        version := get_version(gjson.Get(string(content), "repo").String())
        println("[INFO] Building alpine manifest")
        execute_multi("./bump.sh", "APKBUILD", version)
        execute_multi("abuild", "-r")
    } else {
        println("[ERROR] Unsupported manifest system")
    }
}

func main() {

    if (len(os.Args) < 2) {
        println("[ERROR] Specify manifest name");
        os.Exit(1)
    }

	build(os.Args[1])
}
