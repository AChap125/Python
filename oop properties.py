class Pet:
    vet_name = "Happy Paws Veterinary Clinic"
    
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value
    
    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value
    
    def set_pet_type(self, value):
        self.__pet_type = value
    
    def display_pet_info(self):
        print("\nPet Information:")
        print(f"Veterinary Clinic: {Pet.vet_name}")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")

def check_property(pet_obj, property_name):
    mangled_name = f"_Pet__{property_name}"
    exists = hasattr(pet_obj, mangled_name)
    print(f"Does {pet_obj.get_pet_name()} have property '{property_name}'? {exists}")
    return exists

def main():
    pet1 = Pet("John", "Doe", "PET001", "Buddy", "Dog")
    pet2 = Pet("Jane", "Smith", "PET002", "Whiskers", "Cat")
    pet3 = Pet("Robert", "Johnson", "PET003", "Tweety") 
    
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()
    
    print("\nChanging pet1's type from Dog to Golden Retriever...")
    pet1.set_pet_type("Golden Retriever")
    pet1.display_pet_info()
    
    print("\nChanging pet3's owner last name from Johnson to Williams...")
    pet3.set_owner_last_name("Williams")
    pet3.display_pet_info()
    
    print("\nChecking property existence:")
    check_property(pet1, "pet_name")     
    check_property(pet2, "owner_first_name")  
    check_property(pet3, "age")          
    check_property(pet1, "vet_name")      
    
    print("\nVeterinary Clinic Name (class variable):", Pet.vet_name)
    
    try:
        print("\nAttempting to access private variable directly...")
        print(pet1.__pet_name)
    except AttributeError as e:
        print(f"Error: {e}")
        print("This demonstrates that private variables can't be accessed directly.")
    
    print("\nAccessing through name mangling (not recommended):")
    print(f"pet1's name (via mangling): {pet1._Pet__pet_name}")

if __name__ == "__main__":
    main()