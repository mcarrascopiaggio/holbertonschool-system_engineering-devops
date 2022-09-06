#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Hago dos requests: una para devolver el nombre del empleado unicamente
y otra para tener toda la información de task.
extend your Python script to export data in the JSON format
ormat must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
"USERNAME"}, ... ]}
https://realpython.com/python-json/
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_TODO = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    response_todo = requests.get(url_TODO).json()
    response_user = requests.get(url).json()

    with open('{}.json'.format(id), 'w') as jsonfile:
        task = []
        for respod in response_todo:
            task.append({'task': respod.get('title'),
                         'completed': respod.get('completed'),
                         'username': response_user.get('username')})
        info = {"{}".format(id): task}
        json.dump(info, jsonfile)
