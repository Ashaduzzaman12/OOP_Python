class Gari:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def move(self):
        pass

    def __repr__(self):
        return f'{self.name} {self.price} '

class bus(Gari):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)
    
    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()
       

class truck(Gari):
    def __init__(self, name, price,capacity):
        self.capacity=capacity
        super().__init__(name, price)

class pickup(truck):
    def __init__(self, name, price, capacity):
        super().__init__(name, price, capacity)


class Acbus(bus):
    def __init__(self, name, price, seat,temp):
        self.temp=temp
        super().__init__(name, price, seat)

    def __repr__(self):
        return super().__repr__()


green_line=Acbus('green',50000,22,15)
print(green_line)