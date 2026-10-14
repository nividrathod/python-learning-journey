def check_for_word():
    word = "learning"
    with open("06 File Handling/Practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
          print("Found")
        else:
            print("Not Found")

#check_for_word()

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("06 File Handling/Practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()