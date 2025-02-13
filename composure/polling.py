responses = {}
polling_active = True

while polling_active:
    name  = input("enter your name :")
    response = input('which life do you have: ')
    
    # store
    responses[name] = response
    # find out if the loop still go on
    repeat = input('would you like to continue adding people (yes / No)')
    if repeat.title() == "No":
        polling_active = False
    
#showing results
print("\n-------polling results-------")
for name,response in responses.items():
    print(name + " lives a " + response + "'s life" )