#!/usr/bin/python3
"""
Script that returns info about an employee's TODO list progress
and exports the data to a CSV file.
Uses https://jsonplaceholder.typicode.com.
"""

import csv
import requests
from sys import argv


def get_employee_todos_progress(employee_id):
    """
    Fetch and display the TODO list progress of an employee.
    Also, export the data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        # Base URL for the API
        url = "https://jsonplaceholder.typicode.com/"

        # Fetch user information
        user_response = requests.get(url + f"users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data['username']

        # Fetch employee's TODO list
        todos_response = requests.get(url + f"todos?userId={employee_id}")
        todos_list = todos_response.json()

        # Calculate total tasks and completed tasks
        total_tasks = len(todos_list)
        completed_tasks = [task for task in todos_list if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display the progress
        print(f"Employee {employee_name} is done with tasks("
              f"{num_completed_tasks}/{total_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task['title']}")

        # Export to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_list:
                writer.writerow([
                    employee_id,
                    employee_name,
                    task['completed'],
                    task['title']
                ])
        print(f"Data exported to {csv_filename}")
    except Exception as e:
        # Handle any errors that occur during the API requests
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Ensure the script is called with the correct number of arguments
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        # Pass the employee ID to the function
        get_employee_todos_progress(int(argv[1]))
