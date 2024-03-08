# The cartesian product, essentially a for loop inside another one, you can use it as perms with replacement.
from itertools import product

# Prompt the user for the number of pieces of information
num_info = int(input("Enter the number of pieces of information: "))

# Specify the maximum password length (Min is not important as modifying that makes it loop passwords unnecessarily).
max_password_length = int(input("Enter the maximum password length: "))

# Touch an empty list to store the information.
info = []

# Ask the user for information based on the number they provided.
for i in range(num_info):
    user_input = input(f"Enter piece of information {i + 1}: ")
    info.append(user_input)

# Specify the file name (you can change it as needed).
output_file_name = "output.txt"

# Open the file in write mode and generate/write all possible permutations with replacement and individual pieces.
with open(output_file_name, "w") as output_file:
    # Write individual pieces of information and limit the passwords by the amount of characters to smooth the process.
    for piece in info:
        output_file.write(piece[:max_password_length].ljust(max_password_length) + "\n")

    # Write all possible permutations with replacement within the specified length range above.
    for k in range(2, max_password_length + 1):
        for permutation in product(info, repeat=k):
            password = "".join(permutation)[:max_password_length].ljust(max_password_length)
            output_file.write(password + "\n")
# Pretty self-explanatory :)
print(f"All possible permutations with replacement and individual pieces written to {output_file_name}")
