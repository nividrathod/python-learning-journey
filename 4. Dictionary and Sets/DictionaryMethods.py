states = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

#print(states.keys())            # Returns all keys

#print(states.values)            # Returns all values

#print(states.items())           # Returns all (key, value) pairs as tuples

#print(states.get("Madhya Pradesh")) # Returns the value by providing key
#print(states["Madhya Pradeshhh"])   # This returns - ERROR
#print(states.get("Madhya Pradeshhh")) # This returns - NONE

# Adding key and pairs into dictionary

myself = {
    "name" : "Nivid Rathod",
    "age" : 22,
}
print(myself)

myself["city"] = "Indore"       # Directly assigning new key - value
print(myself)

myself.update({"Favourite Movie" : "Bahubali"})     # Assigning using update()
print(myself)

new_dict = {"College" : "MIT","State" : "Madhya Pardesh"}
myself.update(new_dict)
print(myself)