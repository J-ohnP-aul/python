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
    