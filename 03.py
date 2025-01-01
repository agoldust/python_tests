age = input("what is your age? ")

if len(age) == 0:
    age = 0
else:
    age = int(age)

if age == 18 or age > 90:
    print("you are on the line so you are strange!")
elif age > 18:
    print("you are an adult!".lower())
else:
    print(f"you are a kid! ({age})".capitalize())