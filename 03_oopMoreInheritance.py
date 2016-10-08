'''
Lets add a even more inheritence
Vehicule
|__GroundVehicule
|.....|__Car
|.....|__Truck
|.....|__Bike
|__Airplane
|__Boat

Total Classes lines: 67 lines
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

        

class GroundVehicule(Vehicule):
    def __init__(self, model, topSpeed, numberOfWheels):
        Vehicule.__init__(self, model, topSpeed)
        self.numberOfWheels = numberOfWheels
    
    def getNumberOfWheels(self): # all ground vehicule have wheels
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
        
    def drive(self): # all ground vehicules are driven on the ground
        print "I am a "+str(self.model)+" and I am driven"


    
class Airplane(Vehicule):
    def __init__(self, model, topSpeed):
         Vehicule.__init__(self, model, topSpeed)

    def fly(self):
        print "I am a "+str(self.model)+" and I am flown"

    

class Car(GroundVehicule): 
    def __init__(self, model, topSpeed):
        GroundVehicule.__init__(self, model, topSpeed, 4)

    def drift(self): # couldn't find a better unique action
        print "This is an special action that only the car can do"


class Truck(GroundVehicule):
    def __init__(self, model, topSpeed):
        GroundVehicule.__init__(self, model, topSpeed, 12)

    def dumpCargo(self):
        print "This is an special action that only trucks can do"



class Bike(GroundVehicule):
    def __init__(self, model, topSpeed):
        GroundVehicule.__init__(self, model, topSpeed, 2)

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

# show their top speed
airplane01.getTopSpeed()
car01.getTopSpeed()
truck01.getTopSpeed()
bike01.getTopSpeed()
boat01.getTopSpeed()

# Some stuffs only applies to certain classes, like wheels.
# (For the sake of simplicity, let's assume airplanes don't have wheels
# and they only have wings). They all inherit Groun
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
