# lettig user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print('\n' + message)
# using flag
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
        
prompt = 'Wide is the earth we are livung in self'
prompt += "\n(enter 'quit' when you are finished : )"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("in future I will live in "+ city.title() + "!")