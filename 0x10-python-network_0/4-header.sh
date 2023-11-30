#!/bin/bash
# script that takes in URL as an argument, sends GET request to the URL, and displays the body of response
curl -s "$1" -H "X-School-User-Id: 98"
