class Versions():
    def __init__(self, name, skill):
        """a simple class containing diferent version of me \nwith my default characters in all my version"""
        self.name = name
        self.skill = skill
    def code(self):
        
        print(self.name.title() + " chukua lapi msee ucord your way out\n\n")
    def learn(self):
        print("the pdf's are densly filled\nbut not for  " + self.name.title() + ",\nhe takes it all\ncomposure is a skill he adhears!!"
              + "\nfor within "+ self.skill + " is where thy heart lies")
noble = Versions('JP',"coding")
print("hello "+ noble.name + " you love " + noble.skill)
noble.code()
noble.learn()

class Car():
    '''simple car class'''
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_info(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name
    def read_odometer(self):
        '''the statement showing the cars millage'''
        print("she has "+ str(self.odometer_reading) + " miles on it.")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_peng = Car('mercedies','latest','2028')
print(my_peng.get_info())
my_peng.odometer_reading = 23
my_peng.increment_odometer(7)
my_peng.read_odometer()

# inheritance
class Electric_car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        '''initialize attributes of the parent class'''
        super().__init__(make, model, year)
        
my_tesla = Electric_car('tesla13','700pw','2030')
print(my_tesla.get_info())

# adding diferent featureas to the chikd class made from paro
class burkinafaso_model(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batery = 70
    def batery_descr(self):
        '''batery statement'''
        print('the car has a baterry of '+ str(self.batery)+ '-kwh')
        
afri_tesla = burkinafaso_model('Atesla', 'africa_1','2026')
afri_tesla.batery_descr()