#!/usr/bin/python3
"""
script that returns info about employee TODO progress
Implemented using recursion
Using https://jsonplaceholder.typicode.com
"""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Fetch employee information
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)

    # Check if the employee exists
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee = employee_response.json()
    employee_name = employee['name']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Could not fetch TODO list for employee ID {employee_id}.")
        return

    todos = todos_response.json()

    # Calculate the number of completed and total tasks
    done_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)

    # Print the progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
