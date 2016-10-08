'''
Lets start with the basic: OOP with no inheritence at all.
The classes are: Airplane, Car, Truck, Bike, Boat
'''

class Airplane:
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        self.engineRunning = False # Engine is off by default

    def toggleEngine(self):
        print self.model+"'s engine has been " + ("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning
    
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"
    
    def fly(self):
        print "I am an airplane and I am flown"



class Car: 
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        self.numberOfWheels = 4 # No need to pass it as a parameter, it's obvious
        self.engineRunning = False # Engine is off by default

    def toggleEngine(self):
        print self.model+"'s engine has been " + ("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
        
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"
      
    def drive(self):
        print "I am a car and I am driven"



class Truck:
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        self.numberOfWheels = 12 # let's assume they're all 12-wheelers
        self.engineRunning = False # Engine is off by default

    def toggleEngine(self):
        print self.model+"'s engine has been "+("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
        
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"
       
    def drive(self):
        print "I am a truck and I am driven"



class Bike:
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        self.numberOfWheels = 2 # Let's assume there's no hideous 3 wheel bikes
        self.engineRunning = False # Engine is off by default

    def toggleEngine(self):
        print self.model+"'s engine has been " + ("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning

    def getNumberOfWheels(self):
        print str(self.model)+" has "+str(self.numberOfWheels)+" wheels."
    
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"
       
    def drive(self):
        print "I am a bike and I am driven"



class Boat:
    def __init__(self, model, topSpeed):
        self.model = model
        self.topSpeed = topSpeed
        self.engineRunning = False # Engine is off by default

    def toggleEngine(self):
        print self.model+"'s engine has been " + ("stopped" if self.engineRunning else "started")
        self.engineRunning = not self.engineRunning
    
    def getTopSpeed(self):
        print "I am a "+str(self.model)+" and my top speed is "+str(self.topSpeed)+" km/h"
    
    def sail(self):
        print "I am a boat and I am sailed"



# create the objects
airplane01 = Airplane("Blackbird", 700)
car01 = Car("Lamborgini V12", 320)
truck01 = Truck("Kenworth Dumper", 140) 
bike01 = Bike("Kawasaki Ninja ZX-10R", 260)
boat01 = Boat("Lancia Powerboat", 120)

# shows their top speed
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
# fly, so they have independant methods to do their own things. Same for boats.
airplane01.fly()
car01.drive()
truck01.drive()
bike01.drive()
boat01.sail()
