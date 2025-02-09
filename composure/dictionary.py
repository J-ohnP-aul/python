alien_0 = {'color': 'green', 'points': 5}

# accessing value of a dictionary

print(alien_0['color'])
print(alien_0['points'])
newPoints = alien_0['points']
print('You just earned '+ str(newPoints) + " points!")

# adding ney key value pair in adictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# modify values in adictionary
alien_0['color'] = 'red'
print('the alien is now ' + alien_0['color'] + ' in color')
# alien_0['speed'] = 'medium'
alien_0['speed'] = 'fast'

# move alien to the right
# determine how to move the alien based on its curent speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# the new position is the prev position plus the x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("alien new xposition : " + str(alien_0['x_position']))

# storing info about many diff objects
favourite_language = {
    'ryan': 'svelteKit',
    'reagy': 'Js',
    'noble': "python",
    'johnte': 'C'
}

print("john's favoutite language is " + favourite_language['noble'].title() + ".")

# looping through all key - value pairs
for key, value in favourite_language.items():#item method retuens a list of key value pairs
    print("\nKey: " + key)
    print("Value: " + value)

for kv in favourite_language.items():
    print(kv)

for name,lng in favourite_language.items():
    print(name.title() + "'s favourite language is " + lng.title() )

friends = ['ryan','reagy']
# looping through keys
for name in favourite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + " I see your favourite lang is " +
              favourite_language[name].title() + ".") 
        
# list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien.keys())