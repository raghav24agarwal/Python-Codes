class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        toppings = ", ".join(self.toppings)
        return f"Dough: {self.dough}, Sauce: {self.sauce}, Toppings: {toppings}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self, dough):
        self.pizza.set_dough(dough)

    def build_sauce(self, sauce):
        self.pizza.set_sauce(sauce)

    def build_toppings(self, toppings):
        for topping in toppings:
            self.pizza.add_topping(topping)

    def get_pizza(self):
        return self.pizza


# Usage
builder = PizzaBuilder()

builder.build_dough("Thin Crust")
builder.build_sauce("Tomato")
builder.build_toppings(["Mushrooms", "Onions", "Peppers"])

pizza = builder.get_pizza()
print(pizza)  # Output: Dough: Thin Crust, Sauce: Tomato, Toppings: Mushrooms, Onions, Peppers
