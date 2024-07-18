import os
import json

mode = input('Which mode: (i/v/d/c) ')

json_path = os.path.join('/media/tinktonk/CODING/todo.json')


def save():
    savetodo = list()
    savetodo.append(str(newtodo))
    with open(json_path, 'w') as file:
        json.dump(savetodo, file)
    print()


def view():
    with open(json_path, 'r') as file:
        todos = json.load(file)
    for i, todo in enumerate(todos, start=1):
        print(f'{i}. {todo}')


def delete():
    with open(json_path, 'w') as file:
        json.dump([], file)  # erases


def complete():
    with open(json_path, 'r') as file:
        todos = json.load(file)
    todo_number = int(input('Which todo is completed? '))
    if 1 <= todo_number <= len(todos):
        todos[todo_number - 1] = f'{todos[todo_number - 1]} (completed)'
        with open(json_path, 'w') as file:
            json.dump(todos, file)
    else:
        print('Invalid todo number.')


match mode:
    case 'i':
        newtodo = input()
        save()
    case 'v':
        view()
    case 'd':
        certain = input('Are you sure you want to erase all? (y/n): ')
        if certain == 'y':
            delete()
    case 'c':
        complete()
    case _:
        print('Invalid mode.')
        print('Available modes: i (insert), v (view), d (delete entire file), c (completed todo).')
