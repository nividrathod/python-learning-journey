num = {1,2,3,4,5}
print(type(num))
print(num)

num.add(10)     # Adds an element
print(num)

num.remove(5)   # Removes the element
print(num)

num.clear()     # Empties the set
print(num)

num = {1,2,3,4,5} 
print(num)  

remove = num.pop()       # Removes a random value and returns removed value
print("Removed Num:",remove)
print(num)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
new1 = set1.union(set2)     # Combines both set value & returns new
print(new1)

new2 = set1.intersection(set2)  # Combines common values & returns new
print(new2)