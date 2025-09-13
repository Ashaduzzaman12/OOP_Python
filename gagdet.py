class laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.color=color
        self.memory=memory
        self.price=price

    def run(self):
        return f'Running laptop: {self.brand}'

    def coding(self):
        return f'learning'
    
class phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.sim=dual_sim
        
    
    def phone_call(self,number,text):
        return f'sending message to {number} :{text}'
    
class camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel

    def run(self):
        pass
    def change_lens(self):
        pass

