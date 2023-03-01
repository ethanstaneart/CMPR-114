total_bugs = 0

for day in range(1, 6):
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected

print(f"\nTotal bugs collected over 5 days: {total_bugs}")
