#!/bin/bash
# script that sends JSON POST request to URL passed as the first argument, and displays the body of response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
