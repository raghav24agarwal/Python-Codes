# Class and Static Methods

class Animal:
    zebra = "blab&white"
    @classmethod
    def info(Animal):
        return Animal.zebra
    @staticmethod
    def staticmethod():
        print("This is a satic method")
print(Animal.info())
Animal.staticmethod()