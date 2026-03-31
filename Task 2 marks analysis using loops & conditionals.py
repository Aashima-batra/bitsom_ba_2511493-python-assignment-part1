# -------------------- TASK 2: MARKS ANALYSIS --------------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\n--- TASK 2: MARKS ANALYSIS ---")

# printing subject, marks and grade
for i in range(len(subjects)):
    m = marks[i]

    # assigning grade based on marks
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

    print(f"{subjects[i]} : {m} ({grade})")

# calculating total and average
total = sum(marks)
avg = total / len(marks)

print("\nTotal Marks :", total)
print("Average Marks :", round(avg, 2))

# finding highest and lowest marks
max_marks = max(marks)
min_marks = min(marks)

# getting subject names for highest and lowest
max_sub = subjects[marks.index(max_marks)]
min_sub = subjects[marks.index(min_marks)]

print("Highest :", max_sub, "-", max_marks)
print("Lowest  :", min_sub, "-", min_marks)


# -------------------- ADD NEW SUBJECTS --------------------

print("\nEnter new subjects (type 'done' to stop)")

new_count = 0

while True:
    # asking subject name
    sub = input("Enter subject name: ")

    if sub.lower() == "done":
        break

    # asking marks
    m_input = input("Enter marks: ")

    # checking if marks is valid number
    if not m_input.isdigit():
        print("Invalid input, enter a number")
        continue

    m = int(m_input)

    # checking range
    if m < 0 or m > 100:
        print("Marks should be between 0 and 100")
        continue

    # adding valid data
    subjects.append(sub)
    marks.append(m)
    new_count += 1


# final updated average
new_total = sum(marks)
new_avg = new_total / len(marks)

print("\nNew subjects added :", new_count)
print("Updated Average :", round(new_avg, 2))