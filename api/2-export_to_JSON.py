#!/usr/bin/python3
"""
This module provides a script to fetch and export the TODO list progress
of an employee from the JSONPlaceholder API into a JSON file.
"""
import json
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


def export_to_json(user, todos):
    """Exports the TODO list of the user to a JSON file."""
    user_tasks = []
    for todo in todos:
        user_tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        })

    tasks_dict = {str(user['id']): user_tasks}

    with open(f"{user['id']}.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        try:
            user, todos = fetch_todo_list(employee_id)
            export_to_json(user, todos)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
