package main

import (
	"context"
	"fmt"
	"os"

	"github.com/google/go-github/github"
)

type Package struct {
	FullName      string
	Description   string
	StarsCount    int
	ForksCount    int
	LastUpdatedBy string
}

/*
func patch_file(patch string, file string) {
	cmd := exec.Command("patch", file, "<", patch)

	err := cmd.Run()

	if err != nil {
		log.Fatal(err)
	}
}
*/

/*
func get_version(repo string) string {

}
*/

func main() {
	context := context.Background()
	client := github.NewClient(nil)

	repo, _, err := client.Repositories.Get(context, "OpenCompile", "CompileWorker")

	if err != nil {
		fmt.Printf("Problem in getting repository information %v\n", err)
		os.Exit(1)
	}

	pack := &Package{
		FullName:   *repo.FullName,
		ForksCount: *repo.ForksCount,
		StarsCount: *repo.StargazersCount,
	}

	fmt.Printf("%+v\n", pack)
}
