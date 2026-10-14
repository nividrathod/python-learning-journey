num = [20,10,30]

num.append(40)     # Adds one element at the end
print(num)

num.sort()      # Sorts in ascending order [10,20,30]
print(num)

num.sort(reverse=True)  # Sorts in descending order
print(num)

num.reverse()   # Reverses List
print(num)

num.insert(1,50)    # Insert element at index
print(num)

num1 = [111,222,333,222,555]    

num1.remove(222)   # Removes first occurrence of element
print(num1)

num1.pop(1)     #Removes element at index
print(num1)