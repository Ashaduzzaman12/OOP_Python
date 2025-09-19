class person:
    def __init__(self,name ,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    
    def eat (self):
        print('vat mangsho polao')
    
    def exercise(self):
        raise NotImplementedError



class cricketer(person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)
    def eat(self):
        print('salad khay')

    def exercise(self):
        print('gym a giye gham jhorai')
    
    def __add__(self,other):
        return self.age+other.age
    
    def __mult__(self,other):
        return self.age * other.age

    def __len__(self):
        self.height

liton=cricketer('litu',32,67,80,'bd')
liton.eat()
shanto=cricketer('lord',29,67,80,'bd')

print(liton+shanto)