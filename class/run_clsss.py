#class/run_class.py

class Rerson:
    def __int__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        

def get_name(self):
    return self.name

def get_age(self):
    return self.age

def get_address(self):
    return self.address

def get_info(self):
    return {"name": self.name, "age": self.age}

name = "Kronkanok hankitticai"
age = 21
address  = "London"

person = Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info)
