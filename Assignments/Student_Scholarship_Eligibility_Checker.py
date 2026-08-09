# Student Eligibility checker

# Write a program that asks the user for:
# •	Full Name
# •	Age
# •	Score (0–100)
# •	Attendance Percentage
# •	Whether the student has disciplinary issues (yes or no)
# The program should determine scholarship eligibility using these rules:
# •	Age must be 18 or older
# •	Score must be 75 or above
# •	Attendance must be 80% or above
# •	Student must NOT have disciplinary issues
# All four conditions must be true for the student to be eligible.


full_name = input("Enter your Full Name: ")
age = input("Enter your Age: ")
score = input("Enter your score (0-100): ")
attendace_percentage = input("Enter your Attendance Percentage: ")
disciplinary_issues = input("Do you have disciplinary issues? (Yes / No): ")

# Checking for scholarship eligibility

if (
    age >= 18
    and score >= 75
    and attendace_percentage >= 80
    and disciplinary_issues == "No"
):
    results = "ELIGIBLE"
    print("================== Scholarship Result ==================")
    print()
    print(f"Student: {full_name}")
    print()
    print(f"Status: {results}")
    print()

    print("Reason:")
    print("✔ Age requirement met.")
    print("✔ Score requirement met.")
    print("✔ Attendance requirement met.")
    print("✔ No disciplinary issues.")

elif (
    age >= 18
    and score >= 75
    and attendace_percentage >= 80
    and disciplinary_issues == "Yes"
):
    results = "NOT ELIGIBLE"
    print("================== Scholarship Result ==================")
    print()
    print(f"Student: {full_name}")
    print()
    print(f"Status: {results}")
    print()

    print("Reason:")
    print("✔ Age requirement met.")
    print("✔ Score requirement met.")
    print("✔ Attendance requirement met.")
    print("✘ Has disciplinary issues.")

elif (
    age >= 18
    and score >= 75
    and attendace_percentage < 80
    and disciplinary_issues == "No"
):
    results = "NOT ELIGIBLE"
    print("================== Scholarship Result ==================")
    print()
    print(f"Student: {full_name}")
    print()
    print(f"Status: {results}")
    print()

    print("Reason:")
    print("✔ Age requirement met.")
    print("✔ Score requirement met.")
    print("✘  Attendance below required minimum.")
    print("✔ No disciplinary issues.")

elif (
    age >= 18
    and score < 75
    and attendace_percentage >= 80
    and disciplinary_issues == "Yes"
):
    results = "NOT ELIGIBLE"
    print("================== Scholarship Result ==================")
    print()
    print(f"Student: {full_name}")
    print()
    print(f"Status: {results}")
    print()

    print("Reason:")
    print("✔ Age requirement met.")
    print("✘  Score below required minimum.")
    print("✔ Attendance requirement met.")
    print("✔ Has disciplinary issues.")

elif (
    age < 18
    and score >= 75
    and attendace_percentage >= 80
    and disciplinary_issues == "Yes"
):
    results = "NOT ELIGIBLE"
    print("================== Scholarship Result ==================")
    print()
    print(f"Student: {full_name}")
    print()
    print(f"Status: {results}")
    print()

    print("Reason:")
    print("✘ Age below the required minimum.")
    print("✔ Score requirement met.")
    print("✔ Attendance requirement met.")
    print("✔ Has disciplinary issues.")
