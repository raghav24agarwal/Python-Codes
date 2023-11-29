class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating MyClass instance")

# Create an instance of MyClass
my_class = MyClass()

# Create another instance of MyClass
another_my_class = MyClass()

# Check that both instances are the same object
assert my_class is another_my_class