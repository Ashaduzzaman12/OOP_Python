class user:
    def __init__(self,name,age,money):
        self._name=name
        self._age=age
        self.__money=money
    #getter without any setter is read only attribute 
    @property
    def age(self):
        return self._age
    @property #change method to attribute 
    def salary(self):
        return self.__money
    

    #setter
    @salary.setter
    def salary(self,val):
        if val<0:
            print('salary cant be negative')
        self.__money=val

    
fagun=user('fax',21,12000)

#print(fagun.__money)
print(fagun.age)
fagun.salary=17000
print(fagun.salary)