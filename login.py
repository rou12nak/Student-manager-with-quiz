from data_manager import load_users

def login():
    users = load_users()
    if not users:
        print("No registered users found. Please register first.")
        return None

    enrollment = input("Enter your Enrollment Number: ").strip()
    password = input("Enter your Password: ").strip()

    for user in users:
        if user["enrollment"] == enrollment and user["password"] == password:
            print(f"\nLogin successful! Welcome, {user['name']} ({user['enrollment']})")
            return user["enrollment"]

    print("Invalid enrollment number or password.")
    return None


def admin_login():
    admin_user = "admin"
    admin_pass = "admin123"

    user = input("Enter Admin Username: ").strip()
    pwd = input("Enter Admin Password: ").strip()

    if user == admin_user and pwd == admin_pass:
        print("\nAdmin login successful!")
        return True
    else:
        print("Invalid admin credentials.")
        return False
