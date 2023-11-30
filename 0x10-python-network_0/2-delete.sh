#!/bin/bash
# script that sends DELETE request to the URL passed as the first argument and displays the body of response
curl -s "$1" -X DELETE
