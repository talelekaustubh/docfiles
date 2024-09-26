package main

import (
    "fmt"
    "log"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello From Krishna With Go in Docker!")
}

func main() {
    http.HandleFunc("/", helloHandler)
    fmt.Println("Server is running on port 7000...")
    log.Fatal(http.ListenAndServe(":7000", nil))
    }
