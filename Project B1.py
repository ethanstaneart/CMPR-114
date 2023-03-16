def convert_to_miles(kilometers):
    # Convert kilometers to miles.
    miles = kilometers * 0.6214

    # Return the miles.
    return miles


# Ask the user for input.
kilometers = float(input("Enter the distance in kilometers: "))

# Call the convert_to_miles function and pass in the kilometers as an argument.
miles = convert_to_miles(kilometers)

# Print the result.
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
