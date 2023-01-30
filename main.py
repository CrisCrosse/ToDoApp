import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add (todo to add), show, edit (number of todo to edit), complete (number "
                        "of todo to edit) or exit: \n ")
    user_action = user_action.strip()
# removes whitespace

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # creates a list from file with each line a new entry
        # close file once done to avoid mutation

        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        # no need to close file
         
        todos = functions.get_todos("todos.txt")

        todos.append(todo)

        # # overwrites existing todos.txt with the newly added set
        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)

        functions.write_todos(todos)

    elif 'show' in user_action:
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}. {item}")

    elif 'edit' in user_action:
        todos = functions.get_todos()

        try:
            number = int(user_action[5:])
            number = number - 1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            print("Here is how it will be ", todos)
            functions.write_todos(todos)

        except ValueError:
            print("\nInvalid number inputted after edit command \nTry again like this:edit 1")
        except IndexError:
            print("\nNumber inputted is out of current range of todo items")

    elif 'complete' in user_action:

        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            # convert to index
            todo_to_remove = todos[number].strip('\n')
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
            todos.pop(number)

            functions.write_todos(todos)

        except ValueError:
            print("\nInvalid number inputted after edit command \nTry again like this:edit 1")
        except IndexError:
            print("\nNumber inputted is out of current range of todo items")

    elif 'exit' in user_action:
        break

    else:
        print("Command not recognised")
