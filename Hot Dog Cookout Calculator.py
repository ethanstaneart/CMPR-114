# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Input from user
num_people = int(input("Enter the number of people attending the cookout: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculations
total_hotdogs = num_people * num_hotdogs_per_person
num_hotdog_packages = total_hotdogs // HOT_DOGS_PER_PACKAGE
hotdogs_leftover = total_hotdogs % HOT_DOGS_PER_PACKAGE

num_bun_packages = (total_hotdogs // BUNS_PER_PACKAGE) + 1
if total_hotdogs % BUNS_PER_PACKAGE == 0:
    num_bun_packages -= 1
buns_leftover = (num_bun_packages * BUNS_PER_PACKAGE) - total_hotdogs

# Output
print("Minimum # of packs of hot dogs required:", num_hotdog_packages)
print("Minimum # of bags of buns required:", num_bun_packages)
print("Hot dogs leftover:", hotdogs_leftover)
print("Hot dog buns leftover:", buns_leftover)
