dict = {
    "name" : "Nivid",
    "age" : 22,
    "city" : "Indore",
    "subjects" : ["Python","C","C++"],
}

print(type(dict))               # Type - Dict (Dictionary)
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["city"])

dict["name"] = "Tanishk"        # Assigning new value
print(dict)

info = {}                       # Empty Dictionary
info["Car"] = "Honda"           # Assigning Key - Value
print(info)

# Nested Dictionary

student = {
    "name" : "Nivid Rathod",
    "subjects" : {
        "Physics" : 97,
        "Chemistry" : 98,
        "Maths" : 87,
        "English" : 84,
        "Hindi" : 75
    }
}

print(student)
print(student["name"]," = ",student["subjects"])
print(student["name"]," = ",student["subjects"]["Chemistry"])
