#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#contructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100
    #default contructor

    def __init__(self,a,b):
        print("I am called automatically when object is created")
        self.firstnumber= a
        self.secondnumber= b

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num

obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())