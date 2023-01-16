class mobile:
    def __init__(self, name):
        self.name=name

class mobilestore:
    def __init__(self) :
        self.mobiles = []

    def add_mobile(self,newMob):
        if isinstance(newMob,mobile):
            self.mobiles.append(newMob)
        else:
            raise TypeError('new mobile should be object of mobile class')
            
onePlus=mobile('one plus6')       
