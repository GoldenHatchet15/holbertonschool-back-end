#!/usr/bin/python3
"""
This module provides a script to fetch and export the TODO list progress
of all employees from the JSONPlaceholder API into a JSON file.
"""
import json
import requests


def fetch_users():
    """Fetches all users from the JSONPlaceholder API."""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()


def fetch_todos():
    """Fetches all todo items from the JSONPlaceholder API."""
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return response.json()


def organize_tasks(users, todos):
    """
    Organizes tasks by user_id in a dictionary format.
    Each key is a user_id and the value is a list of dictionaries,
    each containing username, task title, and completion status.
    """
    user_tasks = {}
    for user in users:
        user_id = str(user['id'])
        user_tasks[user_id] = [{
            'username': user['username'],
            'task': todo['title'],
            'completed': todo['completed']
        } for todo in todos if todo['userId'] == user['id']]
    return user_tasks


def save_tasks_to_json(user_tasks):
    """Saves the organized tasks to a JSON file."""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file, indent=4)


def main():
    users = fetch_users()
    todos = fetch_todos()
    user_tasks = organize_tasks(users, todos)
    save_tasks_to_json(user_tasks)


if __name__ == "__main__":
    main()
