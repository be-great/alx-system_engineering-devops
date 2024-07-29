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

    return user_data, todos_data


def display_todo_progress(employee_id):
    """Display the todo progress of the employee."""
    data = get_employee_data(employee_id)
    if data is None:
        return

    user_data, todos_data = data
    user_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
    export_to_csv(employee_id, user_name, todos_data)


def export_to_csv(employee_id, user_name, todo_data):
    """export to csv"""
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
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
    display_todo_progress(employee_id)
