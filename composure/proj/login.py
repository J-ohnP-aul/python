import os
import color as paint
filename = '/home/noble/Desktop/python/composure/proj/data.txt'
with open(filename) as filedtb:
    data_lines = filedtb.readlines()
userdata = []
for line in data_lines:
    for word in line.split():
        userdata.append(word.strip())

os.system('clear')
def displayMenu():
    print(paint.Colors.COLOR_RED)
    print('\t>>>>login menu <<<<<<\n1.\tlogin\n2.\tsign in')
    try:
        option = int(input("\n  Enter an option __:"))
    except ValueError:
        print('invalid input!!')
        
    else:
        return option

opt = displayMenu()
if opt == 1:    
# print(userdata)
    userName = input("Enter your user name pliz: ")
    for name in userdata:
        if name.title() == userName.title():
            password = input('Enter your password: ')
            if password == userdata[int(userdata.index(name)) + 2]:
                print("\n>>>> welcomeback "+ userName + " !") 
            else:
                print("invalid password")  
        else:
            continue
            
else:
    name = input('enter your name: ')
    id = input('enter your d NO: ')
    pass1 = input('enter your password: ')
    os.system('clear')
    pass2 = input('reenter your password for comfirmation: ')
    if pass1 == pass2:
        os.system('clear')
        print('password confirmed!!')
        with open(filename, 'a') as fapend:
            fapend.write('\n'+name +' '+ id + ' '+ pass1)
    else:
        print('invalid password!!')
        

        
