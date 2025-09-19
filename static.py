class shopping :
    cart=[]
    origin='china'

    def __init__(self,name,location):
        self.name='mexico'
        self.location='texas'

    def purches(self,item,price,amount ):
        remaining=amount-price

        print(f'buying :{item} for {price} and remaining :{remaining}')
    @classmethod
    def hudai_dekhi(self,item):
        print('hudai dekhi kinbo na',item)

#static method
    @staticmethod
    def multiply(a,b):
        print(a*b)
        return a*b


#shopping.purches(2,3,3)