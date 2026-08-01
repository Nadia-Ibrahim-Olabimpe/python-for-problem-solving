# What Your Program Should Do

# 1️⃣ Registration
# Ask the user to create an account by entering:
# - An email address
# - A password
# Store both in variables, and confirm registration was successful.

# 2️⃣ Login
# Ask the user to log in by entering their email and password again.
# - If the entered email and password match what was registered, allow them into the portal
# - If either one is wrong, print a clear error message and stop the program — they should not be
#  able to reach the grade calculator with the wrong credentials

# 3️⃣ Grade Calculation
# Once logged in successfully, ask the user to enter their exam score (0–100), and print the correct
# letter grade using the official UG scale:

# 80 – 100 ➜ A
# 75 – 79 ➜ B+
# 70 – 74 ➜ B
# 65 – 69 ➜ C+
# 60 – 64 ➜ C
# 55 – 59 ➜ D+
# 50 – 54 ➜ D
# 45 – 49 ➜ E
# 0 – 44 ➜ F

# Requirements Checklist ✅
# Your program must:
# ✅ Use clearly named variables (snake_case) for email, password, and score
# ✅ Correctly convert the score to the right data type before comparing it
# ✅ Use comparison and boolean operators to check login credentials
# ✅ Use an if / elif / else chain to determine the correct grade
# ✅ Deny access to the grade calculator if login fails — no exceptions
# ✅ Print clean, readable output at every step

# A Few Notes Before You Start 📝
# - Your program only "remembers" the registered account while it's running. Once you close and reopen it,
#  the account is gone — that's expected at this stage.
# - Test your program with both a correct and an incorrect login before submitting.
# - Test at least one score from every grade band, not just A and F — it's easy to write a grading chain with
#  a gap or overlap in the middle.

# Stretch Goal 🌟 (Optional — for those who finish early)
# Give the user 3 attempts to enter the correct login credentials before the program locks them out with "Access denied.
# " You haven't formally covered loops yet, so this is a genuine challenge — attempt it only once the core assignment is fully working

# Registration
print("=====================")
print("= Create an Account =")
print("=====================")
print()

user_email = input("Enter your email address: ")
user_password = input("Enter your password: ")
print()
print("Registration successful!")
print()
print()


# Login
print("----------------")
print("- Login Page.  -")
print("----------------")

login_email = input("Enter your email address: ")
login_password = input("Enter your password: ")

if login_email == user_email and login_password == user_password:
    print()
    print("Login successful!")
    print()

    print(" Grade Calculator")
    print("******************")
    print()

    grade = int(input("Enter your exam score: "))
    if grade >= 80 and grade <= 100:
        print(" Your grade is A")
    elif grade >= 75:
        print(" Your grade is B+")
    elif grade >= 70:
        print(" Your grade is B")
    elif grade >= 65:
        print(" Your grade is C+")
    elif grade >= 60:
        print(" Your grade is C")
    elif grade >= 55:
        print(" Your grade is D+")
    elif grade >= 50:
        print(" Your grade is D")
    elif grade >= 45:
        print(" Your grade is E")

    else:
        print(" Your grade is F")


elif login_email == user_email and login_password != user_password:
    print("Wrong Password!")

elif login_email != user_email and login_password == user_password:
    print("Email not recognized!")

else:
    print("Incorrect credentials!")
