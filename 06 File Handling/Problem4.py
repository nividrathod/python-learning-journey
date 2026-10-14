count = 0
with open("06 File Handling/Number.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count+=1

print("Count of even numbers:",count)