from register import register_user
from login import login, admin_login
from profile import view_profile
from update import update_profile
from quiz import start_quiz
from logout import logout
from forgot_password import forgot_password

def user_menu(enrollment):
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Attempt Quiz")
        print("4. Logout")

        ch = input("Enter your choice: ").strip()

        if ch == "1":
            view_profile(enrollment)
        elif ch == "2":
            update_profile(enrollment)
        elif ch == "3":
            start_quiz(enrollment)
        elif ch == "4":
            logout(enrollment)
            break
        else:
            print("Invalid choice!")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register")
        print("2. Login (User)")
        print("3. Login (Admin)")
        print("4. Forgot Password")
        print("5. Exit")

        ch = input("Enter choice: ").strip()

        if ch == "1":
            register_user()
        elif ch == "2":
            enrollment = login()
            if enrollment:
                user_menu(enrollment)
        elif ch == "3":
            if admin_login():
                print("\nAdmin logged in successfully!")
        elif ch == "4":
            forgot_password()
        elif ch == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
