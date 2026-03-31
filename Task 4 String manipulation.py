# -------------------- TASK 4: STRING MANIPULATION --------------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

print("\n--- TASK 4: STRING OPERATIONS ---")

# removing extra spaces from start and end
clean_essay = essay.strip()
print("\nClean Essay:")
print(clean_essay)

# converting to title case
title_essay = clean_essay.title()
print("\nTitle Case:")
print(title_essay)

# counting how many times 'python' appears
count_python = clean_essay.count("python")
print("\nCount of 'python':", count_python)

# replacing 'python' with 'Python 🐍'
replaced_essay = clean_essay.replace("python", "Python 🐍 ")
print("\nAfter Replacement:")
print(replaced_essay)

# splitting essay into sentences
sentences = clean_essay.split(". ")
print("\nSentences List:")
print(sentences)

# printing each sentence with numbering
print("\nNumbered Sentences:")
for i in range(len(sentences)):
    line = sentences[i]

    # adding '.' if missing at the end
    if not line.endswith("."):
        line = line + "."

    print(f"{i+1}. {line}")