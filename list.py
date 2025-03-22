food = ["bread", "milk", "cheese"]  # List of strings
print(food[0]) 

food.append("eggs")  # Add item to list
print(food)

food.remove("milk")  # Remove item from list
print(food)

food.append("bread")
print(food)
print(food.count("bread"))  # Count number of times item appears in list

food.insert(0, "grapes")  # Insert item at index
print(food)