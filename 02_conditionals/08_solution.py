password = "Secure3p@ss"
password_length = len(password)

# if len(password) < 6:
#     strength = "weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

if password_length < 6:
    strength = "weak"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Password strength is : ", strength)            