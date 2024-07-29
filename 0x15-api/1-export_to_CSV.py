#!/usr/bin/python3#!/usr/bin/python3
'''
1. Export to CSV
'''

import csv
import re
import requests
import sys

URL = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    """Fetch employee and todo data from API."""
    user_url = f'{URL}/users/{employee_id}'
    todos_url = f'{URL}/todos?userId={employee_id}'

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)

    if user_resp.status_code != 200 or todos_resp.status_code != 200:
        return None

    user_data = user_resp.json()
    todos_data = todos_resp.json()
    user_name = user_data.get('name')
    export_to_csv(employee_id, user_name, todos_data)


def export_to_csv(employee_id, user_name, todos_data):
    """Export the todo data to a CSV file."""
    filename = f'{employee_id}.csv'
    with open(filename, 'w') as file:
        for task in todos_data:
            completed = task.get('completed')
            title = task.get('title')
            file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, user_name, completed, title))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    if not re.fullmatch(r'\d+', sys.argv[1]):
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
