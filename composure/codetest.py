import unittest
from names import greetUser

class NameTest(unittest.TestCase):
    '''test names.py func'''
    def test_fist_last(self):# the test func must start eith test_S
        '''do names like john Paul work'''
        fommatname = greetUser('john','paul')
        self.assertEqual(fommatname, 'John Paul')
    def test_fst_last_midlename(self):
        '''do tripple name work'''
        fommatname = greetUser("john",'Okoth','paul')
        self.assertEqual(fommatname, 'John Paul Okoth')
unittest.main()

class AnonymousQuery():
    '''collect anonymous answers for suverys'''
    def __init__(self,question):
        self.question = question
        self.response = []

    def showQuery(self):
        '''show the survey question'''
        print(question)
    
    def storeResponse(self, newresponse):
        '''store all the response to be given'''
        self.response.append(newresponse)
        
    def showResults(self):
        '''show all the responses that have been given'''
        print('Survey results')
        for response in response:
            print("- "+ response)
    
    

print("Enter 'q' to exit >")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Please Enter your last name : ")
    if last == 'q':
        break
    
    fommatedName = greetUser(first, last)
    print("\tNeatly formated name: "+ fommatedName + '.')
    