class Pet:
    """A class to represent pets with kind, breed, and name attributes."""
    
    def __init__(self, kind, breed, name):
        """Initialize a Pet instance with kind, breed, and name."""
        self.__kind = kind
        self.__breed = breed
        self.__name = name
    
    def get_kind(self):
        """Return the pet's kind."""
        return self.__kind
    
    def get_breed(self):
        """Return the pet's breed."""
        return self.__breed
    
    def get_name(self):
        """Return the pet's name."""
        return self.__name
    
    def set_kind(self, kind):
        """Set the pet's kind."""
        self.__kind = kind
    
    def set_breed(self, breed):
        """Set the pet's breed."""
        self.__breed = breed
    
    def set_name(self, name):
        """Set the pet's name."""
        self.__name = name
    
    def print_details(self):
        """Print all details of the pet in a formatted way."""
        print(f"\nPet Details:")
        print(f"Name: {self.__name}")
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")

def demonstrate_special_methods(pet1, pet2, pet3):
    """Demonstrate special methods and functions with Pet instances."""
    
    print("\nDemonstrating special methods:")
    print(f"1. Class name using __name__: {Pet.__name__}")
    
    print(f"\n2. Type of pet1: {type(pet1)}")
    
    print("\n3. isinstance() checks:")
    print(f"Is pet1 a Pet? {isinstance(pet1, Pet)}")
    print(f"Is 'hello' a Pet? {isinstance('hello', Pet)}")
    
    print("\n4. getattr() demonstration:")
    print(f"pet2's name using getattr(): {getattr(pet2, '_Pet__name')}")
    
    print("\n5. __dict__ demonstration:")
    print(f"pet3's attributes: {pet3.__dict__}")
    
    print(f"\n6. Module where Pet is defined: {Pet.__module__}")
    
    print(f"\n7. Pet's base classes: {Pet.__bases__}")

def main():
    pet1 = Pet("Dog", "Golden Retriever", "Buddy")
    pet2 = Pet("Cat", "Siamese", "Whiskers")
    pet3 = Pet("Bird", "Parrot", "Polly")
    
    print("Pet Details:")
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()
    
    print("\nModifying pet1's breed...")
    pet1.set_breed("Labrador")
    pet1.print_details()
    
    demonstrate_special_methods(pet1, pet2, pet3)

if __name__ == "__main__":
    main()