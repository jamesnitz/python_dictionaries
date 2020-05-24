# Create an empty dictionary
animals = dict()
# Add k/v pairs
animals["name"] = "Kevin"
animals["breed"] = "Bulldog!"
animals["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

# iterating dictionaries 
for (key, value) in animals.items():
    print(f"{key}: {value}")

# dictionary of words 
word_definitions = dict()
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["buff"] = "me. I'm buff"
word_definitions["hangry"] = "anger due to hunger"
print(word_definitions["hangry"])


for (key, value) in word_definitions.items():
  print(f"{key}: {value}")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
  print(f'{key}: {" ".join(value)}')