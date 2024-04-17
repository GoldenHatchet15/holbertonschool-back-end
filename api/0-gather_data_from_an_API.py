#!/usr/bin/python3
"""
This module provides a script to fetch and display the TODO list progress
of an employee from the JSONPlaceholder API. It outputs the employee's
name, the number of completed tasks, and the total number of tasks,
followed by the titles of the completed tasks.
"""
import requests
import sys


def fetch_todo_list(employee_id):
    """Fetches TODO list for a given employee ID from JSONPlaceholder API."""
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching user details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetching TODO list for the user
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    return user, todos


def display_progress(user, todos):
    """Displays the progress of the TODO list of the user."""
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]

    # Print the employee progress
    print(
        f"Employee {user['name']} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        try:
            user, todos = fetch_todo_list(employee_id)
            display_progress(user, todos)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
