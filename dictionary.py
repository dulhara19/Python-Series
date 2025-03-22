d={ "tom":732, "sue":285, "joe":882 }
print(d["sue"])

d.update({"jim": 678})
print(d)


"""
by using clear() method we can remove all the elements from the dictionary
"""

# d.clear()
# print(d)

x=d.get("tom")
print(x)

d.pop("tom")
print(d)