#!/bin/bash 
# script that sends request to URL passed as an argument, and displays only the status code of response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
