#!/usr/bin/python3
"""
Script that exports all employees' TODO list data to a JSON file.
Uses https://jsonplaceholder.typicode.com.
"""

import json
import requests


def fetch_all_employee_todos():
    """
    Fetch and export the TODO list data for all employees to a JSON file.

    Returns:
        None
    """
    try:
        # Base URL for the API
        url = "https://jsonplaceholder.typicode.com/"

        # Fetch all users
        users_response = requests.get(url + "users")
        users_list = users_response.json()

        # Dictionary to hold all employee tasks
        all_employees_data = {}

        for user in users_list:
            user_id = user['id']
            username = user['username']

            # Fetch the user's TODO list
            todos_response = requests.get(url + f"todos?userId={user_id}")
            todos_list = todos_response.json()

            # Prepare the list of tasks for this user
            tasks_data = [{
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            } for task in todos_list]

            # Add to the main dictionary under the user's ID
            all_employees_data[str(user_id)] = tasks_data

        # Export to JSON
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(all_employees_data, json_file, indent=4)
        print(f"Data exported to {json_filename}")

    except Exception as e:
        # Handle any errors that occur during the API requests
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Fetch and export all employees' TODO data
    fetch_all_employee_todos()
