class item:
    def __init__(self, name, price, quantity):

        assert isinstance(name, str), "name must be a string"
        assert isinstance(price, int), "price must be an integer"   
        assert price > 0, "price must be a positive integer"

        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity



item1 = item("apple", 12000, 2)
print(item1.calculate_total_price())
# item1.name = "apple"
# item1.price = 12000
# item1.quantity = 2
#print(item1.calculate_total_price(item1.name,item1.price,item1.quantity))

item2 = item("samsung", 15000, 3)
# item2.name = "samsung"
# item2.price = 15000
# item2.quantity = 3
#print(item2.calculate_total_price(item2.name,item2.price,item2.quantity))


