import json

def getStoredUsername():
    '''get stored user name if available'''
    filename = 'username.json'
    try:
        with open(filename) as fobj:
            username = json.load(fobj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def getNewUsername():
    '''prompt for new user nAME'''
    username = input("what is your name : ")
    filename = 'username.json'
    with open(filename, 'w') as fw:
        json.dump(username, fw)
    return username
    
def greetUser():
    '''Greeting the user by name '''
    username = getStoredUsername()
    if username:
        print("Welcome back, " + username + "!")        
    else:
        username = getNewUsername()
        print("We'll remember you "+ username + " when you come back")  
        
greetUser()

