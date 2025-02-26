import unittest
from names import greetUser

class NameTestCase(unittest.TestCase):
    '''test for name function '''
    def testfirst_lastNmae(self):
        '''do names  like ""janis Joplin work'''
        fommatedNme = greetUser('janis','joplin')
        self.assertEqual(fommatedNme, 'Janis Joplin')
    
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
    