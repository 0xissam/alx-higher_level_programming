#!/usr/bin/python3
"""script that takes my GitHub credentials (username and password) and
uses the GitHub API to display my id.
The first argument will be my username.
The second argument will be my password (or access token as password).
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
