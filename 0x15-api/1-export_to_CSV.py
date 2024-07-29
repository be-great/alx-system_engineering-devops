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
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id,
                             user_name,
                             task['completed'],
                             task['title']])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    if not re.fullmatch(r'\d+', sys.argv[1]):
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
