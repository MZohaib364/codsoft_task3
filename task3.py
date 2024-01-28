# TASK 3
#RANDOM PASSWORD GENERATOR

import string
import random

def generate_password(length, strength):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_ch = string.punctuation
    
    # Determine the sample space
    if strength == "Weak":
        sample_space = lowercase + uppercase
    elif strength == "Moderate":    
        sample_space = lowercase + uppercase + digits
    elif strength == "Strong":
        sample_space = lowercase + uppercase + digits + special_ch
    else:
        raise ValueError("Invalid strength level.\n Please choose from 'Weak', 'Moderate', or 'Strong'.")

    password = ""

    # Generate password
    for _ in range(length):
        password += random.choice(sample_space)

    return password



try:
    password_length = int(input("Enter Length of Password: "))
    password_strength = input("Enter Complexity (Weak/Moderate/Strong): ")

    generated_password = generate_password(password_length, password_strength)
    print("Generated Password:", generated_password)

except ValueError as ve:
    print(f"Error: {ve}")
