import re
from data_manager import save_user, load_users

def register_user():
    print("\n===== STUDENT REGISTRATION =====")

    enrollment = input("Enter Enrollment Number: ").strip()
    name = input("Enter Full Name: ").strip()
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ").strip()
    branch = input("Enter Branch: ").strip()
    year = input("Enter Year: ").strip()
    contact = input("Enter Contact Number: ").strip()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
    gender = input("Enter Gender (M/F/O): ").strip()
    address = input("Enter Address: ").strip()

    users = load_users()

    for u in users:
        if u["enrollment"] == enrollment:
            print("Enrollment number already exists.")
            return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format.")
        return

    save_user([enrollment, name, email, password, branch, year, contact, dob, gender, address])
    print("\nRegistration successful!")
