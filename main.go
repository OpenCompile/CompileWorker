package main

import (
	"io"
	"log"
	"net/http"
	"os/exec"

	"github.com/tidwall/gjson"
)

func patch_file(patch string, file string) {
	cmd := exec.Command("patch", file, "<", patch)

	err := cmd.Run()

	if err != nil {
		log.Fatal(err)
	}
}

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

	return value.String()
}

func main() {
	println(get_version("xmrig/xmrig"))
}
