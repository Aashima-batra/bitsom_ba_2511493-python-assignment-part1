# -------------------- TASK 3: CLASS PERFORMANCE SUMMARY --------------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\n--- TASK 3: CLASS REPORT ---")

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_avg_sum = 0

for student in class_data:
    name = student[0]
    marks = student[1]

    # calculating average marks
    avg = sum(marks) / len(marks)
    avg = round(avg, 2)

    # checking pass/fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # printing row in table format
    print(f"{name:<18} | {avg:^7} | {status}")

    # finding topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # adding for class average
    total_avg_sum += avg


# calculating class average
class_avg = total_avg_sum / len(class_data)

print("\nPassed :", pass_count)
print("Failed :", fail_count)

print("Topper :", topper_name, "-", topper_avg)

print("Class Average :", round(class_avg, 2))