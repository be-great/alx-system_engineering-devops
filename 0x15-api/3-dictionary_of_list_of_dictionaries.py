#!/usr/bin/python3
"""
3. Dictionary of list of dictionaries
"""

import json
import requests

URL = "https://jsonplaceholder.typicode.com"


def save_employee_in_dict():
    """Fetch employee and todo data from API."""
    users_url = f'{URL}/users'
    users_resp = requests.get(users_url)
    users_data = users_resp.json()
    users_dict = {}
    filename = "todo_all_employees.json"

    for user in users_data:
        employee_id = user.get('id')
        username = user.get('username')
        todo_url = f"{URL}/users/{employee_id}/todos"
        todo_resp = requests.get(todo_url)
        tasks = todo_resp.json()

        users_dict[employee_id] = []
        for task in tasks:
            complete = task.get('completed')
            title = task.get('title')
            task_dict = {
                "task": title,
                "completed": complete,
                "username": username
            }
            users_dict[employee_id].append(task_dict)

    with open(filename, mode='w') as file:
        json.dump(users_dict, file)


if __name__ == '__main__':
    save_employee_in_dict()
