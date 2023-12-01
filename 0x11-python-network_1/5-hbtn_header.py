#!/usr/bin/python3
"""
script that takes a URL, sends request to URL and displays
the value of the X-Request-Id variable found in the header of response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)
