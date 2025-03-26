class item:
    
    pay_rate= 0.8 # 20% discount to all items

    all= []

    def __init__(self, name, price, quantity):

        assert isinstance(name, str), "name must be a string"
        assert isinstance(price, int), "price must be an integer"   
        assert price > 0, "price must be a positive integer"

        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * item.pay_rate

    def apply_increment(self, increment_value):
        self.price = self.price + self.price * increment_value

    def set_pay_rate(self, new_pay_rate):
        self.pay_rate = new_pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"



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

print(item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(item.__dict__) # __dict__ is a dictionary that contains all the attributes of the class
print(item2.__dict__)# __dict__ is a dictionary that contains all the attributes of the instance level

item1.apply_discount()
print(item1.price)

item1.pay_rate = 0.9
print(item1.pay_rate)

item3 = item("apple", 10000, 1)
item4 = item("samsung", 15000, 2)
item5 = item("apple", 10000, 1)

print(item.all)