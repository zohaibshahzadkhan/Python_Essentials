# A dictionary works something like a list, but instead of a simple series of
# things, a dictionary is a series of pairs of things. Each pair contains a key and a value
customer_1 = {
  "first name" : "zohaib",
  "last name" : "shahzad"
}
# Adding a a key to dictionary
customer_1["phone"] = "03124545415"
del customer_1["last name"]
print(customer_1);
print(customer_1["first name"])

data = {
  "users" : {
    "names": ["Zohaib"," Shahzad","Khan"],
    "age": [15, 16, 17],
  },
  "admin" : {
    "names": ["Zohaib"," Shahzad","Khan"],
    "age": [26, 27, 28],
  },
}
print((data["users"])["age"])

# adding and removing key values in dicitionary
colors = {}
colors["light"] = ["yellow", "white"];
colors["dark"] = ["purple", "black"];
print(colors);
del colors["dark"];
print(colors);

# looping through dictionary

colors = {
  "light": ["yellow", "white"],
  "dark": ["black", "brown"],
}

# looping through dictionary Values
for color in colors.values():
  print(color);

# looping through dictionary Keys 
for color in colors.keys():
  print(color);

# looping through Keys and Values
for key, value in colors.items():
  print(key)
  print(value)
