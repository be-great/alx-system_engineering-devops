#!/usr/bin/python3
""" 0. Gather data from an API """
import sys
import requests


def get_employee_data(employee_id):
    """Get employee data."""
    s0 = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    s1 = 'https://jsonplaceholder.typicode.com/'
    s2 = s1 + f'todos?userId={employee_id}'
    user_url = s0
    todos_url = s2
    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)

    if user_resp.status_code != 200 or todos_resp.status_code != 200:
        return None

    user_data = user_resp.json()
    todos_data = todos_resp.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    """Display the data."""
    data = get_employee_data(employee_id)
    if data is None:
        return

    user_data, todos_data = data
    user_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print('Employee {} is done with tasks({}/{})'
          .format(user_name,
                  number_of_done_tasks,
                  total_tasks))
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    """The starting point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as employee ID")
        sys.exit(1)

    display_todo_progress(employee_id)
