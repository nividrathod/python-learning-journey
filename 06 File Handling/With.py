with open("06 File Handling/sample.txt","r") as f:      # no need to close (Automatically Happens)
    data = f.read()
    print(data)