#!/usr/bin/python3
"""
script that returns info about employee TODO progress
Implemented using recursion
Using https://jsonplaceholder.typicode.com
"""
import requests
import sys
import re


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_response = requests.get('{}/users/{}'.format(API, id)).json()
            todos_response = requests.get('{}/todos'.format(API)).json()
            user_name = user_response.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_response))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
