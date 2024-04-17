#!/usr/bin/python3
"""
This module provides a script to fetch and export the TODO list progress
of an employee from the JSONPlaceholder API into a CSV file.
"""
import csv
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


def export_to_csv(user, todos):
    """Exports the TODO list of the user to a CSV file."""
    with open(f"{user['id']}.csv", 'w', newline='') as csvfile:
        fieldnames = [
                        'USER_ID',
                        'USERNAME',
                        'TASK_COMPLETED_STATUS',
                        'TASK_TITLE'
                    ]
        writer = csv.DictWriter(
                                csvfile,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL
                                )

        for todo in todos:
            writer.writerow({
                'USER_ID': user['id'],
                'USERNAME': user['username'],
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            })


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        try:
            user, todos = fetch_todo_list(employee_id)
            export_to_csv(user, todos)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
