# To separate letter from word and store inside list as individual items..
letter=[]
for x in 'humans':
    letter.append(x)

print(letter)
# To implement same login in single line using list comprehension approach
h_letter=[ x for x in 'humans']
print(h_letter)
# Example two
square_number=[ square**2 for square in range(1,6) if square%2==0]
print(square_number)

letters1 = list(map(lambda x: x, 'human'))
print(letters1)

### List comprehension approach with conditional statement to filter list based on few conditions.
num_even=[x for x in range(30) if x%2==0]
print(num_even)

# Nested IF with List Comprehension
num_list=[y for y in range(100) if y%2==0 if y%5==0]
print(num_list)
## If else statement with list comprehension
obj=["even" if x%2==0 else "odd" for x in range(10)]
print(obj)
## set comprehension implementation
set_num={x for x in 'basavraj'}
print(set_num)
# slicing list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:]
print(first_two)