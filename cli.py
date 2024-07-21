import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now )
while True:
    user_action = input("Type add, show, edit, Complete or exit:")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos=functions.get_todos()

        todos.append(todo+"\n")
#here in the todos.append we are appending the todos to this todos=get_todos("todos.txt") already readed todos from file now it is list of todos that was readed and it ll stored inthe todos=get_todos("todos.txt") variable todos with the appendd one then only we are writing the readed todos in a file write_todos("todos.txt",todos)
        functions.write_todos(todos ,"todos.txt")


    elif 'show' in user_action:
        todos=functions.get_todos()

        # new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif 'edit' in user_action:
        try:
            number=int(user_action[5:])
            print(number)
            number=number-1

            todos=functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number ]=new_todo + '\n'

            functions.write_todos(todos, "todos.txt")
        except ValueError:
            print("Your command is not valid")
            continue
    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")

            message = f"Todo -{todo_to_remove}- was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")
print("Bye!")