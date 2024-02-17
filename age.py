age = 18
print(age == 18)

if age < 21:
    print("You are not allowed to drink")
elif age <= 21:
    print("You are allowed to drink")
elif age > 21:
    print("You are not allowed to drink")
else:
    print("You are allowed to drink")

age_0 = 22

age_1 = 18

test = age_0 >= 21 and age_1 >= 21
print(test)

age_1 = 22
test = age_0 >= 21 and age_1 >= 21
print(test)

test = age_0 >= 21 or age_1 >= 21
print(test)