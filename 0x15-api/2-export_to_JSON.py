#!/usr/bin/python3
"""
script that Exports to-do list information for a given employee ID to JSON format.
"""
import json
import requests
import sys
import urllib3

# Disable SSL certificate verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id), verify=False).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={
       "userId": user_id}, verify=False).json()

    tasks = []
    for t in todos:
        task = {}
        task["task"] = t.get("title")
        task["completed"] = t.get("completed")
        task["username"] = username
        tasks.append(task)

    data = {user_id: tasks}

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
