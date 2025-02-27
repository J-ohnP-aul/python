def greetUser(fist,last,middle=''):
    '''generate a neatly formated full name'''
    if middle:
        fullName = fist + ' ' + middle + " " + last
    else:
        fullName = fist + " "+ last
    return fullName.title()