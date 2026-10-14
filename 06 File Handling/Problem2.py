with open("06 File Handling/Practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("06 File Handling/Practice.txt","w") as f:
    f.write(new_data)