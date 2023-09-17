# Example for encapsulation, pri vate and public variables

class Computer:

    def __init__(self):
        self.__maxprice = 900   # Private attribute
        self._discount = 0.1    # Protected attribute
        self.public_var = "I'm public!"  # Public attribute

    def sell(self):
        print(f"Selling Price: ${self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

    def applyDiscount(self):
        discounted_price = self.__maxprice - (self.__maxprice * self._discount)
        return discounted_price


class Laptop(Computer):
    def applyDiscount(self):
        discounted_price = super().applyDiscount()
        return discounted_price - 50


c = Computer()

# Accessing public attribute
print(c.public_var)

# Trying to access protected and private attributes
print(c._discount)       # Accessing protected attribute (not recommended)
# print(c.__maxprice)    # Accessing private attribute directly (not possible due to name mangling)

c.sell()

# Using setter function
c.setMaxPrice(1000)
c.sell()

# Applying discount
discounted_price = c.applyDiscount()
print(f"Discounted Price: ${discounted_price}")

laptop = Laptop()
laptop.sell()
laptop_discounted_price = laptop.applyDiscount()
print(f"Discounted Laptop Price: ${laptop_discounted_price}")