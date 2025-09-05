# creaton of the class
class class_name:
    class_attribute="value"
    class_attribute2="value2"

    def __init__(self): #constructor
        print(f"hello {self.class_attribute} and {self.class_attribute}")

    def class_method(self,parameter1,parameter2): #class method with parameters 
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        print("first paramerter",self.parameter1)
        print("second paramerter",self.parameter2)
    def class_method2(self):
        square=self.parameter1
        print(square)
obj=class_name() #creating the object of class (the constructor(__init__ method) is automatically called when the object is created)
obj.name="vineet" #object attribute (if the object attribute and class attribute is of same name then the object attribute is given preference)
print(obj.name,obj.class_attribute,obj.class_attribute2) #accessing the class attribute by object of the class
obj.class_method("sonipat","nangal kalan") #using the class method
obj.class_method2() #using the class method

