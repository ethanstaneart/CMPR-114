# Calorie burn rate
calories_burned_per_minute = 4.2

# Calories burnt after ... Minutes
for minutes in [10, 15, 20, 25, 30]:
    calories_burned = calories_burned_per_minute * minutes
    print(f"Calories burned after {minutes} minutes: {calories_burned}")
