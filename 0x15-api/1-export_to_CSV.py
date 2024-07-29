#!/usr/bin/python3#!/usr/bin/python3
"""
1. Export to CSV
"""
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    user_res = requests.get(user_url)
    user_name = user_res.json().get('username')
    task_url = user_url + '/todos'
    task_res = requests.get(task_url)
    tasks = task_res.json()
    file_name = '{}.csv'.format(employee_id)
    with open(file_name, 'w') as file:
        for task in tasks:
            complete = task.get('completed')
            title = task.get('title')
            file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, user_name, complete, title))
