def get_todos(filepath="todos.txt"):
    """returns a list of the todos created from the stored
    text file with a new item on each line"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Creates a file or overwrites a file, writes a list item onto each line
    from the list input"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return