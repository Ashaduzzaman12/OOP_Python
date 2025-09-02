class bank :
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name #public
        self._branch='banani' #protected
        self.__balance=initial_deposit #private
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance

    
my_ac=bank('ashad',100000)
print(my_ac.get_balance())



