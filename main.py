import requests
import pprint


def task_1():
    parameters = {
        'q': 'language:html'
    }

    response = requests.get('https://api.github.com/search/repositories', params=parameters)
    print(response.status_code)

    if response.ok:
        pprint.pprint(response.json())
    else:
        print("Беда")

def task_2():
    parameters = {
        'userId': 1
    }

    response = requests.get('https://jsonplaceholder.typicode.com/posts', params=parameters)
    print(response.status_code)

    if response.ok:
        pprint.pprint(response.json())
    else:
        print("Беда")


def task_3():
    send_dict = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    response = requests.post('https://jsonplaceholder.typicode.com/posts', data=send_dict)
    print(response.status_code)

    if response.ok:
        pprint.pprint(response.json())
    else:
        print("Беда")


task_3()

