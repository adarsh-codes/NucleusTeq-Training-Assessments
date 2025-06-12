class Person:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age     

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
            self.__age = new_age

p = Person("Adarsh", 25)
print(p.get_name())  
print(p.get_age())   

p.set_name("Ravi")
p.set_age(30)

print(p.get_name())   
print(p.get_age())    
       
