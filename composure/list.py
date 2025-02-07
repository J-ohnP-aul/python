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