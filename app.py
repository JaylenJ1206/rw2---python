#prin(hello world)
#exercise
weight = int(input("weight: "))
unit = input("(k)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + converted)
else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))    


# strings
course = 'python for beginners'
print(course.replace('for', '4'))

#Type Conversation
birth_year=input("enter you birth year: ")
age = 2025 - int(birth_year)
print(age)

first = input("first: ")
second = input("second: ")
sum = float(first) + float(second)
print("sum: " + str(sum))

# Reciving Input
name = input("what is your name? ")
