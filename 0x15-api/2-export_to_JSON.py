#!/usr/bin/python3
"""
 2. Export to JSON 
"""

import json
import requests
import sys

URL = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    """Fetch employee and todo data from API."""
    user_url = f'{URL}/users/{employee_id}'
    todos_url = f'{URL}/users/{employee_id}/todos'

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)
    user_data = user_resp.json()
    todos_data = todos_resp.json()
    user_name = user_data.get('username')
    export_to_json(employee_id, user_name, todos_data)


def export_to_json(employee_id, user_name, todos_data):
    """Export the todo data to a json file."""
    data = {employee_id: []}
    filename = f'{employee_id}.json'
    for task in todos_data:
        complete = task.get('completed')
        title = task.get('title')
        d = {"task": title, "completed": complete, "username": user_name}
        data[employee_id].append(d)
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
