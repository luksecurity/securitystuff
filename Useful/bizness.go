package main

import (
	"crypto/sha1"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"strings"
)

func hashPassword(salt string, password []byte) string {
	hash := sha1.New()
	hash.Write([]byte(salt))
	hash.Write(password)
	hashedBytes := hash.Sum(nil)
	return fmt.Sprintf("$SHA1$%s$%s", salt, base64.URLEncoding.EncodeToString(hashedBytes))
}

func searchPassword(search, wordlistPath string) {
	wordlist, err := ioutil.ReadFile(wordlistPath)
	if err != nil {
		fmt.Println("Error reading wordlist:", err)
		return
	}

	lines := strings.Split(string(wordlist), "\n")
	for _, password := range lines {
		password = strings.TrimSpace(password) // Supprimer les espaces autour du mot de passe

		if password == "" {
			continue // Ignorer les lignes vides
		}

		hashedPassword := hashPassword("d", []byte(password))

		if hashedPassword == search {
			fmt.Printf("Found Password: %s, hash: %s\n", password, hashedPassword)
			return
		}
	}
	fmt.Println("Password not found.")
}

func main() {
	search := "$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I="
	wordlistPath := "./rockyou.txt"

	searchPassword(search, wordlistPath)
}
