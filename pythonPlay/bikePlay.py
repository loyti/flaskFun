class Bike(object):
    def __init__ (price,maxSpeed,miles):
        self.price = "$Really$ Expen$ive"
        self.maxSpeed = maxSpeed
        self.miles = 0
    def displayInfo(self):
        print "A little about your Bike: $Price: {}, {} max kph & {} miles traveled".format(str(self.price), int(self.maxSpeed), str(self.miles))
        retrun self
    def ride(self):
        self.miles += 10
        print "You just went on a 10 mile journey" 
        retrun self
    def reverse(self):
        self.miles -= 5
        print "Backing up 5 miles in reverse is quite interesting You have gone {} miles ".format(self.miles)
        return self
    def noNeg(self):
        if (self.miles < 0):
            self.miles = 0
        print "You backed up off a cliff and were saved just in time but the bike is gone :( Here is a new one :)"
        return self
bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()