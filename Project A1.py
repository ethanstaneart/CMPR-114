# This program demonstrates two functions that
# have local variables with the same name.

def main():
    # Get the number of birds in Texas from the user.
    texas_birds = int(input("Enter the number of birds in Texas: "))

    # Get the number of birds in California from the user.
    california_birds = int(input("Enter the number of birds in California: "))

    # Call the texas function with the number of birds in Texas.
    texas(texas_birds)

    # Call the california function with the number of birds in California.
    california(california_birds)


# Definition of the texas function. It creates
# a local variable named birds.
def texas(birds):
    print(f"Texas has {birds} birds.")


# Definition of the california function. It also
# creates a local variable named birds.
def california(birds):
    print(f"California has {birds} birds.")


# Call the main function.
main()
