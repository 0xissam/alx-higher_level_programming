#!/usr/bin/python3
"""
script that takes a URL sends request to the URL and displays the
body of response (decoded with utf-8).
managing urllib.error.HTTPError exceptions and
print: Error code: followed by HTTP stat code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
