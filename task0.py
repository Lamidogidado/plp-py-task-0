name = input("What is your name? ")
age = int(input("How old are you? "))  # Convert input to integer
location = input("Where do you live? ")

# Personalized message using f-strings for formatted string literals
message = f"Hello {name}, you are {age} years old and live in {location}."

print(message)
