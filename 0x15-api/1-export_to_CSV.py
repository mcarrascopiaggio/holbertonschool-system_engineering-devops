#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Hago dos requests: una para devolver el nombre del empleado unicamente
y otra para tener toda la información de task.
extend your Python script to export data in the CSV format.
https://www.programiz.com/python-programming/writing-csv-files
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_TODO = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    response_todo = requests.get(url_TODO).json()
    response_user = requests.get(url).json()

    with open('{}.csv'.format(id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in response_todo:
            y = [id, response_user.get('username'),
                 task.get('completed'),
                 task.get('title')]
            y = [str(value) for value in y]
            writer.writerow(y)
