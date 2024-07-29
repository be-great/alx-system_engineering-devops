#!/usr/bin/python3
"""
1. Export to CSV
"""

import csv
import re
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
    user_name = user_data.get('name')
    export_to_csv(employee_id, user_name, todos_data)


def export_to_csv(employee_id, user_name, todos_data):
    """Export the todo data to a CSV file."""
    filename = f'{employee_id}.csv'
    with open(filename, mode='w') as file:
        for task in todos_data:
            complete = task.get('completed')
            title = task.get('title')
            file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, user_name, complete, title))


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
