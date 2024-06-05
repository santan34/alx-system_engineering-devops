#!/usr/bin/python3
"""export"""
import json
from requests import get
from sys import argv


def jsonWrite(user):
    """writes to json"""
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    usr = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('userusr')
    
    ordered = []
    for line in data:
        ordered.append({"task": line.get('title'), "completed":
                        line.get('completed'), "userusr": usr})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: ordered}, f)


if __name__ == "__main__":
    jsonWrite(int(argv[1]))