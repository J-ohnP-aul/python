def greet_user(name):
    """display a simple greeting"""
    print("Hello " + name + " how do you do")
    
greet_user('johnPaul')
greet_user("noble")

def describe_person(name, skill, job="developer"):
    '''display about personel'''
    print("\nHe goes by the name "+ name + " specialised in "+ skill + "\nthat makes him a "+ job)

describe_person('johnPaul', 'software development', 'SENIOR DEVELOPER')
# key argument method same to the first one
describe_person(name='johnPaul', skill='software development', job='SENIOR DEVELOPER')

# default values
describe_person("noble",'hacking', 'hacker')

# return of afunction
def formated_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

developer = formated_name('john', 'paul')
print(developer)

# making a function with adefault value
def format_name(first_name, last_name, midle_name=''):
    if midle_name:
        full_name = first_name + " " + midle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
coder = format_name('john','okoth', 'paul')
print(coder)

# functions returning dictionaries
def build_person(name, skill):
    '''return a dictionary of infomation '''
    person = {'name':name, 'skill':skill}
    return person

blackhat = build_person('tony','hacking')
print(blackhat)

# while True:
#     fname = input("enter first name: ")
#     lname = input('\nenter last name: ')
#     fullname = fname +" "+ lname
#     print('hello '+ fullname.title() + " hope you are doing great")
def name_fomater(fname, lname):
    flname = fname+' '+lname
    return flname.title()

# while True:
#     print('\nEnter your name')
#     print('enter q to quit')
    
#     fname = input("enter first name: ")
#     if fname.lower() == 'q':
#         break
    
#     lname = input('enter last name: ')
#     if lname.lower() == 'q':
#         break
    
#     namefomat = name_fomater(fname,lname)
#     print('Hello '+ namefomat + '!')

#passing list to functions
def greet_progremmers(maninja):
    maninja.pop(-1)
    for ninja in maninja:
        print("\nhello "+ ninja +' Wellcome to the club')
        
coders = ['10Xdev','soendev','programmer','hacker','coder']
# to avoid modifying the original list you can pass a copy of the funct
greet_progremmers(coders[:])
print(coders)