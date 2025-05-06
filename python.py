age = int(input("How old are you? ")) # Prompt the user for their age

if age >= 18: # Check if the user is 18 or older
    print("Congratulations! You are eligible to vote. Go make a difference!") # Print a congratulatory message
else: # If the user is younger than 18
    years_left = 18 - age  # Calculate the remaining years
    print("Oops! You're not eligible to vote yet. But hey, only " + str(years_left) + " more years to go!") 
    # Print a message indicating how many years are left until they can vote
