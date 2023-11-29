class Employee:
    def __init__(self):
        self._age = 0
    @property
    def age(self):
        print("getter method")  # Getter
        return self._age
    @age.setter
    def age(self, x):
        print("Setter method")   # Setter
        self._age = x
e = Employee()
e.age = 40
print(e.age)