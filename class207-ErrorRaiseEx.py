class animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
       raise NotImplementedError("define this method is subclass")
class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        return 'bhow bhow'


class cat(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

doggy=dog('boony','pug')
print(doggy.sound())