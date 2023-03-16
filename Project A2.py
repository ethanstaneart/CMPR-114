def get_personal_info():
    # Get the user's last name.
    last_name = input("Enter your last name: ")

    # Get the user's first name.
    first_name = input("Enter your first name: ")

    # Get the user's address.
    address = input("Enter your address: ")

    # Get the user's city.
    city = input("Enter your city: ")

    # Get the user's state.
    state = input("Enter your state: ")

    # Get the user's zip code.
    zip_code = input("Enter your zip code: ")

    # Return the user's personal information as a dictionary.
    return {
        "last_name": last_name,
        "first_name": first_name,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zip_code
    }


# Call the function to get the user's personal information.
personal_info = get_personal_info()

# Print the user's personal information.
print("Your personal information:")
print(f"Last name: {personal_info['last_name']}")
print(f"First name: {personal_info['first_name']}")
print(f"Address: {personal_info['address']}")
print(f"City: {personal_info['city']}")
print(f"State: {personal_info['state']}")
print(f"Zip code: {personal_info['zip_code']}")
