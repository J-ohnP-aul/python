import os
# with open('file.txt') as file_object:
    # this prints all file contents
    # content = file_object.read()
    # print(content.rstrip()

file_name = 'file.txt'

with open(file_name) as file_objct:
    # for line in file_objct:
    #     print(line.rstrip())
    lines = file_objct.readlines()
for line in lines:
    print(line.strip())
    
pi_string =""
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

with open("write.txt",'r+') as fileW:
    fileW.write('no reason for why not \nI guess this is my only option')
    
with open("write.txt") as file_obj:
    for line in file_obj.readlines():
        print(line.strip())
        
with open('codelit.txt', 'w') as file_objct:
    file_objct.write('within line by line lies reasoning\n')
    file_objct.write('on the left hand lies solutions\nI love coding far more than Johnsmith')
    
with open('codelit.txt') as objct:
    for line in objct.readlines():
        print(line.strip())
os.system("open codelit.txt")