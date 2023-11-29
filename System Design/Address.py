class Address:

    def __init__(self, pincode, street, city, state, country):
        self.pincode = pincode
        self.street = street
        self.city = city
        self.state = state
        self.country = country

    
    def __str__(self) -> str:
        return f'Pincode is {self.pincode}'
    

class CashDispenser:

    def __init__(self, inputcash : int) -> None:
        CashDispenser.cash = inputcash
        print(type(CashDispenser.cash))

    def __str__(self) -> str:
        return f'Value of {CashDispenser.cash}'
    

cashd = CashDispenser("20000")
print(cashd)
