import json as j

numbers = [2,3,5,7,11,13]

filename  = 'num.json'
with open(filename, 'w') as file_obj:
    j.dump(numbers, file_obj)
    
