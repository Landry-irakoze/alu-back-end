#!/usr/bin/python3
"""Export the TODO list data of all employees to a JSON file."""
import json
import requests


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base + "users").json()
    todos = requests.get(base + "todos").json()

    data = {}
    for user in users:
        uid = user.get("id")
        data[str(uid)] = [{"username": user.get("username"),
                           "task": t.get("title"),
                           "completed": t.get("completed")}
                          for t in todos if t.get("userId") == uid]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
