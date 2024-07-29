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
    with open('{}.csv'.format(employee_id), 'w') as csvfile:
        for task in todos_data:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                employee_id, user_name, completed, title_task))


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    res = requests.get(url_user)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    todos_data = res.json()
    export_to_csv(employee_id, user_name, todos_data)
