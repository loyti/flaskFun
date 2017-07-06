class Patient(object):
    patID = 0
    patQueue = []
    def __init__(self):
        self.patID = self.__class__.patID
        self.__class__.patID += 1
    	
        

    def newPat(self,patName,patPhone,bedNumber,allergies):
        self.patQueue = self.__class__.patQueue
        self.__class__.patQueue.append(patName)
    	self.patName = patName
        self.patPhone = patPhone
        self.bedNumber = bedNumber
        self.allergies = allergies
        return self

    def displayPat(self):
        print self.pID,self.patName,self.patPhone,self.bedNumber,self.allergies
    	if len(self.callQueue) == 1:
                print len(self.callQueue), "Patient in the queue", self.callQueue
                return self
        else:
            print len(self.callQueue), "Patients in the queue", self.callQueue
            return self
        return self

randomPat1 = Patient()
randomPat1.newPat("Brice", 7145555555, 1700, "Pizza")
randomPat1.displayPat()

randomPat2 = Patient()
randomPat2.newPat("Niko", 6265555555,800, "oddly matched colors")
randomPat2.displayPat()

randomPat3 = Patient()
randomPat3.newPat("Mark", 2135555555, 1200, "Lunch")
randomPat3.displayPat()

randomPat4 = Patient()
randomPat4.newPat("Oli",3105555555,1000,"Films")
randomPat4.displayPat()
