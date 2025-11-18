from data_manager import load_users, save_users

def update_profile(enrollment):
    users = load_users()
    for u in users:
        if u["enrollment"] == enrollment:
            print("\n===== UPDATE PROFILE =====")
            for key in ["name", "email", "branch", "year", "contact", "dob", "gender", "address"]:
                new_val = input(f"Enter new {key} (Leave blank to keep '{u[key]}'): ").strip()
                if new_val:
                    u[key] = new_val
            save_users(users)
            print("\nProfile updated successfully!")
            return
    print("User not found.")
