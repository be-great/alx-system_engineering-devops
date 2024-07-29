#!/usr/bin/python3
'''
 0. Gather data from an API
'''

import re
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            URL = "https://jsonplaceholder.typicode.com/"
            employee_id = int(sys.argv[1])
            user_url = f'{URL}users/{employee_id}'
            todo_url = f'{URL}todos?userId={employee_id}'
            user_data = requests.get(user_url).json()
            todo_data = requests.get(todo_url).json()
            name = user_data.get('name')
            tasks = list(filter(lambda x: x.get('userId') == employee_id,
                                todo_data))
            done_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name,
                    len(done_tasks),
                    len(tasks),
                )
            )

            if len(done_tasks) > 0:
                for task in done_tasks:
                    print('\t {}'.format(task.get('title')))
