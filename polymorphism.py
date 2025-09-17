class animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print("animal is making sound ")


class cat(animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('mewo mewo')

class dog(animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('ghew ghew')

class goat(animal):
    def __init__(self, name):
        super().__init__(name)

don=cat('real don')
don.make_sound()

jon=dog('tommy')
jon.make_sound()

animals=[don,jon]