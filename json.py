book = {}

book ['book1'] = {
    "title": "The Hitchhiker's Guide to the Galaxy",    
    "author": "Douglas Adams",
    "price": 12.50}

book ['book2'] = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "price": 29.99}

print(book)
print(book["book1"])
import json
json.dumps(book)
print(json.dumps(book))
print(json.dumps(book, indent=4))