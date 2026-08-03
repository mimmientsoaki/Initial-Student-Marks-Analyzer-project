students = {
    "John": 78,
    "Mary": 92,
    "Peter": 65,
    "Sarah": 38,
    "James": 71
    }

print("Student Marks:")
for student, mark in students.items():
    print(f"{student}: {mark}")

average = sum(students.values()) / len(students)
print(f"\nAverage Mark: {average:.2f}")

highest_student = max(students, key=students.get)
print(f"Highest Mark: {highest_student} with {students[highest_student]}")

lowest_student = min(students, key=students.get)
print(f"Lowest Mark: {lowest_student} with {students[lowest_student]}") 

print("\nResults")
for student, mark in students.items():
    if mark >= 80:
        result = "Pass Distinction"
    elif 70 <= mark < 80:
        result = "Pass Merit"
    elif 50 <= mark < 70:
        result = "Pass"
    else:
        result = "Fail"
    print(f"{student}: {mark} -> {result}")