katz_deli = []

def line(list):
    """Return a string that describes who is currently in line using positional indexs"""
    if len(list) == 0:
        print('The line is currently empty.')
        return 
    
    result = 'The line is currently: '

    for name in list:
        index = list.index(name)
        result += f"{index + 1}. {name} "
    
    print(result.rstrip())

def take_a_number(line, name):
    """Append a name to the deli list and returns a string indicating current position in list"""

    # append to list
    line.append(name)

    # get index number
    index = line.index(name)

    # print message
    print(f"Welcome, {name}. You are number {index + 1} in line.")

def now_serving(list):
    """Pop the first element from the list and print message"""
    if len(list) == 0:
        print('There is nobody waiting to be served!')
        return
    serving = list.pop(0)
    print(f"Currently serving {serving}.")
    return