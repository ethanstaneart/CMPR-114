recipe_cookies = 48

sugar_per_recipe = 1.5
butter_per_recipe = 1
flour_per_recipe = 2.75

desired_cookies = float(input("How many cookies would you like to make? "))

sugar_needed = sugar_per_recipe * desired_cookies / recipe_cookies
butter_needed = butter_per_recipe * desired_cookies / recipe_cookies
flour_needed = flour_per_recipe * desired_cookies / recipe_cookies

print("Sugar: {:.2f} cups".format(sugar_needed))
print("Butter: {:.2f} cups".format(butter_needed))
print("Flour: {:.2f} cups".format(flour_needed))

