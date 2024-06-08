#!/usr/bin/python3
"""exports a csv"""
import csv
import requests
from sys import argv


def export_csv(id):
    usr = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}"
    ).json().get("username")
    data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    ).json()

    li = []
    for i in data:
        listng = [id, usr, i.get("completed"), i.get("title")]
        li.append(listng)

    with open(f"{id}.csv", "w", ) as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(li)


if __name__ == "__main__":
    export_csv(int(argv[1]))
