#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Hago dos requests: una para devolver el nombre del empleado unicamente
y otra para tener toda la información de task.
Luego debo sumar la cantidad de completed = true
Para eso recorro todas las task
cuando las recorro ya las cuento porque necesito el total tb.
Guardo cada tarea en una lista para detallarlas luego
https://jsonplaceholder.typicode.com/users/1/todos
https://jsonplaceholder.typicode.com/users/2
Salida: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
"""
import requests
import json
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_TODO = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    response_todo = requests.get(url_TODO).json()
    response_user = requests.get(url).json()

    total = 0
    completed = 0
    completed_task = []

    for task in response_todo:
        total = total + 1
        if task.get('completed') is True:
            completed = completed + 1
            completed_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(response_user.get('name'), completed, total))
    for c in completed_task:
        print("\t {}".format(c))
