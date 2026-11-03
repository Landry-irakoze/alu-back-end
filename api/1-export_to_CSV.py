#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(base + "users/{}".format(user_id)).json()
    todos = requests.get(base + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username, str(t.get("completed")),
                             t.get("title")])
