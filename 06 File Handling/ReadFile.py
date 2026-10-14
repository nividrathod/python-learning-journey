
f = open("06 File Handling/sample.txt", "r")        # Opens File

#data = f.read()     # Reads file

#data = f.read(10)       # Reads counted characters only

# print(data)
# print(type(data))

line1 = f.readline()        # Reads line by line (One line at a time)
print(line1)

line2 = f.readline()
print(line2)

f.close()