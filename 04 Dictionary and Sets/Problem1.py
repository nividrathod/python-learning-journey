subjects = {}
for i in range (1,4):
    subname = input(f"Enter subject {i} name: ")
    subjectmarks = input(f"Enter subject {i} marks: ")
    subjects[subname] = subjectmarks

print(subjects)