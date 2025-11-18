import os
import random
from datetime import datetime
from data_manager import save_score

QUESTIONS_FILE = os.path.join("data", "questions", "all_questions.txt")

def load_all_questions():
    questions = []
    if not os.path.exists(QUESTIONS_FILE):
        print("No question file found.")
        return []

    with open(QUESTIONS_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 7:
            category, q, a, b, c, d, ans = parts
            questions.append({
                "category": category.upper(),
                "question": q,
                "options": [a, b, c, d],
                "answer": ans
            })
    return questions

def start_quiz(enrollment):
    all_questions = load_all_questions()
    if not all_questions:
        print("No questions available.")
        return

    random.shuffle(all_questions)
    selected_questions = all_questions[:10]

    print("\n--- QUIZ STARTED ---")
    total = len(selected_questions)
    score = 0
    category_scores = {"DSA": [0, 0], "DBMS": [0, 0], "PYTHON": [0, 0]}

    for i, q in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i} ({q['category']}): {q['question']}")
        for j, opt in enumerate(q['options'], start=1):
            print(f"{j}. {opt}")
        
        ans = input("Enter choice (1-4): ").strip()
        category_scores[q['category']][1] += 1

        if ans.isdigit() and 1 <= int(ans) <= 4:
            chosen = q['options'][int(ans)-1].strip().lower()
            if chosen == q['answer'].strip().lower():
                print("Correct!")
                score += 1
                category_scores[q['category']][0] += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")
        else:
            print("Invalid input.")

    print("\n--- QUIZ SUMMARY ---")
    print(f"Enrollment No : {enrollment}")
    print(f"Total Score: {score}/{total}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for cat, (correct, total_q) in category_scores.items():
        if total_q > 0:
            print(f"{cat}: {correct}/{total_q}")
            save_score(enrollment, cat, correct, total_q, now)
    print(f"\n{enrollment}")
    print(f"\nResults saved on: {now}")
    print("\nScores saved successfully.")
