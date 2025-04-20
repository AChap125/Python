class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
        
    def get_age(self):
        return self.__age
        
    def get_phone(self):
        return self.__phone
    
    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_age(self, age):
        self.__age = age
        
    def set_phone(self, phone):
        self.__phone = phone
        
    def display_info(self):
        return f"Name: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone: {self.__phone}"

person1 = Person("John Appleberg", "122 Main St, Anytown", 55, "555-123-4866")
person2 = Person("Ryan Smith", "332 River Ave, Somewhere", 20, "555-987-8888")
person3 = Person("Robert Douglas", "528 Oak Rd, Nowhere", 40, "555-567-9622")

print("Person 1:")
print(person1.display_info())
print("\nPerson 2:")
print(person2.display_info())
print("\nPerson 3:")
print(person3.display_info())