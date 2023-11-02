#creating a obhject
# class Dog:
#    def __init__(self,name):
#      self.name = name

# dog1=Dog("bruno")
# print(dog1.name)


# class Dog:
#     def _init_(self,name):
#        self.name = name
    
# dog1=Dog("buddy")
# print(dog1.name)


class car:
    def __init__(self,model,make):
        self.make=make
        self.model = model
        
car1=car("toyota","carry")
car2=car("mercedes","benz")
print(car1.make,car1.model)  
print(car2.make,car2.model)      


class Bankaccount:
  def __init__(self,account_number,balance):
    self._account_number=account_number #protected number 
    self.__balance=balance #private number
  def get_balance(self):
    return self.__balance
account1 = Bankaccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())



