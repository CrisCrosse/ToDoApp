import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to do below:")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos_list'
                      , enable_events = True, size=(45, 10))
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
#list of lists, each list is a new row

window = sg.Window("My To Do App",
                   layout=layout,
                   font=('Helvetica', 20))
# displays window

while True:
    event, values = window.read()
    # interpreter stops here until a button is pressed
    print("Event", event)
    print("Values: ", values)
    # dict_name["key"][0] removes object from list where value is a list
    print("Selected list item: ", values['todos_list'][0])
    #window.read returns a tuple with the
    # button pressed first and then a dictionary of what is
    # contained within input boxes and what is clicked on
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos_list'][0]

            todos = functions.get_todos()
            todos.remove(todo_to_complete)

            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            break



        case 'todos_list':
            window['todo'].update(value=values['todos_list'][0])

        case sg.WIN_CLOSED:
            break


window.close()

