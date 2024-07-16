#Create a dictionary
details_dict = {
    "name":"Shivani",
  "subject": "Coding",
  "favcolor": "Red",
  "city": "Mumbai",

}

# Accessing values in a dictionary
print(details_dict["name"])
print(details_dict)

# Get the list of keys
print(details_dict.keys())

# Get the list of values
print(details_dict.values())

# Change a value in the dictionary
details_dict["city"] = "Nashik"
print(details_dict)

# Create a list with the same information to show the difference between list and a dictionary
details_list = ["Shivani", "Coding","Red", "Mumbai"]
print(details_list[0])