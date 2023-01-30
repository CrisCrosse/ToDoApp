import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to do below:")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window("My To Do App", layout=[[label], [input_box, add_button]])
# displays window
window.read()
# interpreter stops here until a button is pressed
window.close()

