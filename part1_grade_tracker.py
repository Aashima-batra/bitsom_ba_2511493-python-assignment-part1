# ---------------- TASK 1: DATA CLEANING ----------------

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:
    # cleaning name
    name = student["name"].strip().title()

    # converting roll to int
    roll = int(student["roll"])

    # converting marks string to list
    marks = list(map(int, student["marks_str"].split(",")))

    # checking name validity
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    # printing profile
    print("="*32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")

    if valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")
    print("="*32)

    # special case for roll 103
    if roll == 103:
        print(name.upper())
        print(name.lower())


# ---------------- TASK 2: MARKS ANALYSIS ----------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\n--- Subject Wise Grades ---")

for i in range(len(subjects)):
    m = marks[i]

    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], "-", m, "-", grade)

# total and average
total = sum(marks)
avg = round(total / len(marks), 2)

print("Total:", total)
print("Average:", avg)

# highest and lowest
max_marks = max(marks)
min_marks = min(marks)

print("Highest:", subjects[marks.index(max_marks)], max_marks)
print("Lowest:", subjects[marks.index(min_marks)], min_marks)

# while loop for adding subjects
count = 0

while True:
    sub = input("Enter subject (or done): ")

    if sub.lower() == "done":
        break

    try:
        m = int(input("Enter marks: "))

        if m < 0 or m > 100:
            print("Invalid marks")
            continue

        subjects.append(sub)
        marks.append(m)
        count += 1

    except:
        print("Enter valid number")

print("New subjects added:", count)
print("Updated Average:", round(sum(marks)/len(marks), 2))


# ---------------- TASK 3: CLASS SUMMARY ----------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []

for name, marks in class_data:
    avg = round(sum(marks)/len(marks), 2)
    averages.append(avg)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    print(f"{name:<18} | {avg:^7} | {status}")

print("\nPassed:", pass_count)
print("Failed:", fail_count)

topper_index = averages.index(max(averages))
print("Topper:", class_data[topper_index][0], max(averages))

print("Class Average:", round(sum(averages)/len(averages), 2))


# ---------------- TASK 4: STRING MANIPULATION ----------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1
clean_essay = essay.strip()
print("\nClean Essay:", clean_essay)

# step 2
print("\nTitle Case:", clean_essay.title())

# step 3
print("\nCount of python:", clean_essay.count("python"))

# step 4
print("\nReplaced:", clean_essay.replace("python", "Python 🐍"))

# step 5
sentences = clean_essay.split(". ")
print("\nSentences List:", sentences)

# step 6
print("\nNumbered Sentences:")
for i in range(len(sentences)):
    s = sentences[i]
    if not s.endswith("."):
        s += "."
    print(i+1, s)