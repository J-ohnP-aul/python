cars = ['subaru', 'BMW', 'mercedies', 'toyota', 'tesla']

for car in cars:
    if car == 'tesla':
        print(car.upper())
    else:
        print(car.title())

# to confirm individual item in a list use the word -in it returns a boolean value
print('tesla' in cars)

# to confirm if an item is not in a list you can use the keyword -not in
print('tesl' not in cars)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print('\n' + user.title() + ", you can post a response if you wish.")

age = 20
#you combine mutiple conditions using the-AND word also the -or word
if age<=20 and age>18:
    print('\nWe ni myouthe!')

# use mutple if statements to test all conditions