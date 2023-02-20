import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to do below:")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
# displays window

while True:
    event, values = window.read()
    # interpreter stops here until a button is pressed
    print(event)
    print(values)
    #window.read returns a tuple with the
    # button pressed first and then the input box value
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

