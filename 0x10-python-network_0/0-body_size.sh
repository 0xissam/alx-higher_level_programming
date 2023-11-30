#!/bin/bash
# script that takes in a URL, sends request to that URL, and displays size of the body of the response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
