# -------------------- TASK 1: DATA PARSING & PROFILE CLEANING --------------------

# raw student data 
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

print("\n--- TASK 1: STUDENT PROFILES ---")

for student in raw_students:
    # removing extra spaces and fixing name format
    name = student["name"].strip().title()

    # converting roll number from string to integer
    roll = int(student["roll"])

    # converting marks string into list of integers
    marks = []
    for m in student["marks_str"].split(","):
        marks.append(int(m.strip()))

    # checking if name contains only alphabets
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    # printing student details
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")

    if valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    print("=" * 32)

    # special case for roll 103
    if roll == 103:
        print(name.upper())
        print(name.lower())



        
