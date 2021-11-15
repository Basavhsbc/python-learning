# List cheat sheet in the python
bikes=['trek','redline','giant']
first_bike=bikes[0]
last_bike=bikes[-1]
# To add items in the list..
bikes.append("bajaj")
print(f"{first_bike} and {last_bike} ")
# To iterate over list using below loop
for bike in bikes:
    print(bike)

# To print numerial list
squares=[]
for x in range(1,11):
    squares.append(x**2)

print(squares)