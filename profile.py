from data_manager import load_users

def view_profile(enrollment):
    users = load_users()
    for u in users:
        if u["enrollment"] == enrollment:
            print("\n===== PROFILE DETAILS =====")
            for k, v in u.items():
                print(f"{k.capitalize()}: {v}")
            return
    print("Profile not found.")
