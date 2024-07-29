#!/usr/bin/python3#!/usr/bin/python3
'''
1. Export to CSV
'''

import csv
import requests
import sys

URL = "https://jsonplaceholder.typicode.com/users"


def export_to_csv(employee_id, user_name, todos_data):
    """Export the todo data to a CSV file."""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        user_url = f'{URL}/{employee_id}'
        todos_url = f'{URL}/{employee_id}/todos'
        user_resp = requests.get(user_url)
        todos_resp = requests.get(todos_url)

        user_name = user_resp.json().get('name')
        todos_data = todos_resp.json()
        filename = f'{employee_id}.csv'
        with open(filename, 'w') as file:
            for task in todos_data:
                completed = task.get('completed')
                title = task.get('title')
                file.write('"{}","{}","{}","{}"\n'.format(
                    employee_id, user_name, completed, title))
