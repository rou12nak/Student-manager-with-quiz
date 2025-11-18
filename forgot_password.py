from data_manager import load_users, save_users

def forgot_password():
    users = load_users()
    enrollment = input("Enter Enrollment Number: ").strip()
    email = input("Enter Registered Email: ").strip()

    for u in users:
        if u["enrollment"] == enrollment and u["email"] == email:
            new_pass = input("Enter New Password: ").strip()
            u["password"] = new_pass
            save_users(users)
            print("\nPassword updated successfully!")
            return
    print("Invalid enrollment or email.")
