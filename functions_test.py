
# Read the list of todos from text file
def get_todos(filepath='todos.txt'):
    """ Read the list of todos from text file >> when you call help(get_todos)
    this line will be shown, it's called doc strings
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Update the todos text file
def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None

