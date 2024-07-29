#!/usr/bin/python3
"""
 3. Dictionary of list of dictionaries
 """

import json
import requests
import sys

URL = "https://jsonplaceholder.typicode.com"


def save_employee_in_dict(employee_id):
    """Fetch employee and todo data from API."""
    users_url = f'{URL}/users'
    users_resp = requests.get(users_url)
    users_data = users_resp.json()
    users_dict = {}
    filename = "todo_all_employees.json"
    for user in users_data:
        employee_id = user.get('id')
        username = user.get('username')
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todo_url = todo_url + '/todos/'
        todo_resp = requests.get(todo_url)
        tasks = todo_resp.json()
        users_dict[employee_id] = []
        for task in tasks:
            complete = task.get('completed')
            title = task.get('title')
            d = {"task": title, "completed": complete, "username": username}
            users_dict[employee_id].append(d)
    with open(filename, mode='w') as file:
        json.dump(users_dict, file)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    save_employee_in_dict(employee_id)
