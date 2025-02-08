friends = ['Gore', 'Cryptic', 'Tony', 'Dj', 'Ngare', 'Lucky', 'Zero', 'Lewis', 'Batson', 'Justin']
message = "one of a friend in tech is " + friends[1].title() + " ." 
print(message)
friends[0] = "Senior"
friends.append("Gore")
friends.insert(0, 'mwangi')
friends.remove("Ngare")
del friends[4]
# friends.sort()
friends.reverse()
friends.reverse()
print(len(friends))
motorcycles = ['honda', 'yamaha', 'suzuki']
popedMoto = motorcycles.pop(0)
print(motorcycles)
print(popedMoto)

for friend in friends:
    print(friend.title() + " You are among the friends I have never had")

print("\nThank you, everyone. That was a great magic show!")

dreams = ['pilot', 'senior Dev', 'leader', 'billionair', 'rugby', 'noble', 'Hacker'] 
for me in dreams:
    print("hello "+ me.title())

print("a well defined potential for far more beyond this")

numbers = list(range(1,20,2))
print(numbers)
#list comprehension
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(sum(squares))

squares = [value**2 for value in range(1,11)]
print(squares)