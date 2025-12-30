from datetime import datetime

# Get user input
dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

# Convert string to date
dob = datetime.strptime(dob_input, "%d-%m-%Y")

# Get today's date
today = datetime.today()

# Calculate age in years
age_years = today.year - dob.year

# Adjust if birthday hasn't happened yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age_years -= 1

print(f"You are {age_years} years old.")
