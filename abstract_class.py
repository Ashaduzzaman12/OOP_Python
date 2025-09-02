from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass

class monkey(animal):
    def __init__(self,name):
        self.name=monkey
        super().__init__()
    def eat(self):
        print("hey nana,i am eating abnanana")
    def move(self):
        print('hanging on the brunches')

liar=monkey('milo')
liar.eat()
liar.move()

