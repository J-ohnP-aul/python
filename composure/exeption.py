# try:
    # print(5/0)
# except ZeroDivisionError:

# print("give me two numbers and I will devide them\nEnter 'q' to exit")
# while True:
#     firstNo = input('\nEnter first number: ')
#     if firstNo == 'q':
#         break
#     secondNo = input("\nEnter second number: ")
#     if secondNo == 'q':
#         break
#     try:
#         answer = int(firstNo) / int(secondNo)
#     except ZeroDivisionError:
#         print('You cant devide by zero >> undefinate')
#     else:       
#         print(answer)
        
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = "sorry, the file "+ filename + 'does not exist!'
    print(msg)