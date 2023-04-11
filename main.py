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

class DiscountedGood(Good):
    def __init__(self,  name, price, quantity=1, discount=0):
        super().__init__(name, price, quantity)
        self.discount = discount

    def get_sum(self):
           return super().get_sum() * ((100 - self.discount) / 100)

    def __str__(self):
        return super().__str__() + f"(-{self.discount}%)"

class Cart:
    def __init__(self, goods_list):
        self.goods_list = goods_list

    def total_sum(self):
        total_sum = 0
        for good in self.goods_list:
            if isinstance(good, DiscountedGood) and good.discount > 0:
                total_sum += good.price * good.quantity - good.price / 100 * good.discount
            else:
                total_sum += good.price * good.quantity
        return total_sum

    def display_cart(self):
        print("{:<20} {:>7} {:>5} {:>10} {:6}".format("Name", "PPU", "CNT", "Price", "Disc."))
        print("======================================================================")
        for good in self.goods_list:
            print(good)
        print("======================================================================")
        print("{:<35} = {:<10.2f}".format("Total", self.total_sum()))


goods = [
    Good('Bread', 17, 3),
    Good("Water", 19, 2),
    DiscountedGood('Juice', 80, 1, 20),
    Good('Toilet Paper', 19, 10)
]
cart = Cart(goods)
cart.display_cart()

# good = Good("Bread", 17, 3)
# print(good)
# discounted_good = DiscountedGood("Milk", 500, 1, 10)
# print(discounted_good)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
