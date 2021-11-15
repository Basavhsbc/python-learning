alien={"color": "green", "point": 5}
alien["theme"]="golden"
print(alien)
## Accessing specific item by using key reference
print(f"Alien color is {alien['color']}")
## looping through all items in the dictionary
for key,value in alien.items():
    print(f"{key} has associated value {value}")

## looping through keys
for name in alien.values():
    print(f"{name}")