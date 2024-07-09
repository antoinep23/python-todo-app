# from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'It is {now}!')

while True:
    user_action = input('Type add, show, edit, complete or exit ').strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{i + 1}-{item}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo

            functions.write_todos('todos.txt', todos)

        except ValueError:
            print('Command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos('todos.txt', todos)

            print(f'Todo {todo_to_remove} was removed from the list ✅')

        except IndexError:
            print('There is no task with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('Bye!')
