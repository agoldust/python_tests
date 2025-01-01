import random

min: int = 0
max: int = 100

#using random function
print(random.random())
print(random.uniform(min, max))
print(random.randint(min, max))


# list data structure
lst_names = ["Akbar", "Yegane", "Mahsa", "mina"]
lst_names.append("Dani")

print(lst_names[random.randint(0,len(lst_names)-1)])