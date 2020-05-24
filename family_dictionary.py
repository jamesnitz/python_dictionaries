
my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# print(my_family["sister"]["name"])

for (key, value) in my_family.items():
  name = value["name"]
  age = value["age"]
  print(f"{name} is my {key} age: {age} ")
  