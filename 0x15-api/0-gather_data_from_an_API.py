#!/usr/bin/python3
"""A python script to gather data from an API"""
import requests
from sys import argv

def getdata(id):
    """fetches data from a API usinf the user id"""
    name = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}").json().get('name')
    todo = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}/todos").json()
    count = 0
    tot = 0
    comp = []
    for dic in todo:
        tot += 1
        if dic.get('completed') == True:
            count += 1
            comp.append(dic.get("title"))
    if (name is not None):
        print(f"{name} is done with tasks ({count}/{tot}):")
        for i in comp:
            print(f'\t{i}')

if __name__ == "__main__":
    getdata(int(argv[1]))