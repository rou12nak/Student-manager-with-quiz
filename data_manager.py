import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.txt")
SCORES_FILE = os.path.join(DATA_DIR, "scores.txt")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_user(user_data):
    with open(USERS_FILE, "a") as f:
        f.write("|".join(user_data) + "\n")

def load_users():
    users = []
    if not os.path.exists(USERS_FILE):
        return users

    with open(USERS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 10:
                users.append({
                    "enrollment": parts[0],
                    "name": parts[1],
                    "email": parts[2],
                    "password": parts[3],
                    "branch": parts[4],
                    "year": parts[5],
                    "contact": parts[6],
                    "dob": parts[7],
                    "gender": parts[8],
                    "address": parts[9]
                })
    return users

def save_users(users):
    with open(USERS_FILE, "w") as f:
        for u in users:
            f.write("|".join([
                u["enrollment"], u["name"], u["email"], u["password"],
                u["branch"], u["year"], u["contact"], u["dob"],
                u["gender"], u["address"]
            ]) + "\n")

def save_score(enrollment, category, score, total, datetime_str):
    with open(SCORES_FILE, "a") as f:
        f.write(f"{enrollment} | {category} | {score}/{total} | {datetime_str}\n")

def load_scores():
    scores = []
    if not os.path.exists(SCORES_FILE):
        return scores

    with open(SCORES_FILE, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split("|")]
            if len(parts) == 4:
                scores.append({
                    "enrollment": parts[0],
                    "category": parts[1],
                    "score": parts[2],
                    "datetime": parts[3]
                })
    return scores
