# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Good:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_sum(self):
        total_sum = self.price * self.quantity
        return total_sum

    def __str__(self):
        return f"{self.name:<20} {self.price:>7.2f}*{self.quantity:>3} = {self.get_sum():<5.2f}"

class DiscountedGood:
    def __init__(self,  name, price, quantity=1, discount = 0):
        super().__init__(name, price, quantity=1)
        self.discount = discount

    def get_sum(self):
        return super().get_sum()((100-self.discount)/100)

    def __str__(self):
        return super().__str__() + f"(-{self.discount}%)"

good = Good("Bread", 17, 3)
print(good)
discounted_good = DiscountedGood("Milk", 500, 1, 10)
print(discounted_good)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
