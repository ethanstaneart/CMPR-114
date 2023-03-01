# This program asks the user for their lap times and displays
# the fastest, slowest, and average lap times.

# Prompt the user to enter the number of laps they ran.
num_laps = int(input("Enter the number of laps you ran: "))

# Initialize an empty list to store the lap times.
lap_times = []

# Loop over the number of laps entered by the user.
for i in range(num_laps):
    # Prompt the user to enter the lap time for each lap.
    lap_time = float(input(f"Enter the time for lap {i + 1}: "))

    # Add the lap time to the lap_times list.
    lap_times.append(lap_time)

# Find the fastest, slowest, and average lap times.
fastest_lap = min(lap_times)
slowest_lap = max(lap_times)
average_lap = sum(lap_times) / num_laps

# Display the results to the user.
print(f"Fastest lap: {fastest_lap:.2f}")
print(f"Slowest lap: {slowest_lap:.2f}")
print(f"Average lap: {average_lap:.2f}")
