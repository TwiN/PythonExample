'''
Lets add a little bit of inheritence
The parent class is Vehicule because every class below is a vehicule
The child classes are: Airplane, Car, Truck, Bike, Boat

Total Classes lines: 75 lines
'''

class Vehicule:
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        
    def toggleEngine(self):
        print self.model+"'s engine has been " + ("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning
    
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"


    
class Airplane(Vehicule):
    def __init__(self, model, topSpeed):
         Vehicule.__init__(self, model, topSpeed)

    def fly(self):
        print "I am a "+str(self.model)+" and I am flown"



class Car(Vehicule): 
    def __init__(self, model, topSpeed):
        Vehicule.__init__(self, model, topSpeed)
        self.numberOfWheels = 4 # No need to pass it as a parameter, it's obvious

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
      
    def drive(self):
        print "I am a "+str(self.model)+" and I am driven"
        
    def drift(self): # couldn't find a better unique action
        print "This is an special action that only the car can do"



class Truck(Vehicule):
    def __init__(self, model, topSpeed):
        Vehicule.__init__(self, model, topSpeed)
        self.numberOfWheels = 12 # let's assume they're all 12-wheelers

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
       
    def drive(self):
        print "I am a "+str(self.model)+" and I am driven"

    def dumpCargo(self):
        print "This is an special action that only trucks can do"


class Bike(Vehicule):
    def __init__(self, model, topSpeed):
        Vehicule.__init__(self, model, topSpeed)
        self.numberOfWheels = 2 # Let's assume there's no hideous 3 wheel bikes

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
       
    def drive(self):
        print "I am a "+str(self.model)+" and I am driven"
        
    def doAWheelie(self): 
        print "Bikes can do wheelies"



class Boat(Vehicule):
    def __init__(self, model, topSpeed):
        Vehicule.__init__(self, model, topSpeed)
    
    def sail(self):
        print "I am a "+str(self.model)+" and I am sailed"



# create the objects
airplane01 = Airplane("Blackbird", 700)
car01 = Car("Lamborgini V12", 320)
truck01 = Truck("Kenworth Dumper", 140) 
bike01 = Bike("Kawasaki Ninja ZX-10R", 260)
boat01 = Boat("Lancia Powerboat", 120)

# those are all vehicules, and they all have a top speed because they can
# all move. Instead of writing the method getTopSpeed() in every single,
# child class you just have to put it in the Parent class! Don't forget 
# that the MAIN GOAL OF INHERITANCE IS TO WRITE LESS CODE. Less useless 
# code means easier to read code.
airplane01.getTopSpeed()
car01.getTopSpeed()
truck01.getTopSpeed()
bike01.getTopSpeed()
boat01.getTopSpeed()

# Some stuffs only applies to certain classes, like wheels.
# (For the sake of simplicity, let's assume airplanes don't have wheels
# and they only have wings)
car01.getNumberOfWheels()
truck01.getNumberOfWheels()
bike01.getNumberOfWheels()


# Even though these are all vehicule, the airplane can fly but the cars cannot
# fly, so they have independant methods to do their own things.
airplane01.fly()
car01.drive()
truck01.drive()
bike01.drive()
boat01.sail()
car01.drift()
truck01.dumpCargo()
bike01.doAWheelie()
