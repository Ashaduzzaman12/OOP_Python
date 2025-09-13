#base/parent class or common attribute +functionality class 

class Gadget:
    def __init__(self,brand ,price,color):
        self.brand=brand
        self.price=price
        self.color=color
       
    def run(self):
        return f'Running laptop: {self.brand}'

class laptop:
    def __init__(self,memory):
        
        self.memory=memory


    def coding(self):
        return f'learning'
    
class phone(Gadget):
    def __init__(self,brand,price,color,dual_sim):
        self.sim=dual_sim
        super().__init__(brand,price,color)
        
    
    def phone_call(self,number,text):
        return f'sending message to {number} :{text}'
    
    def __repr__(self):
        return f'phone :{self.brand} {self.price} {self.sim}'
    
class camera:
    def __init__(self,pixel):
        
        self.pixel=pixel


    def change_lens(self):
        pass



#inheritance

my_phone=phone('iphone',990,'black',True)
print(my_phone)
