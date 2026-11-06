

name = input("Enter student name: ")

math_marks = float(input("Enter Math marks: "))
english_marks = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

if not (0 <= math_marks <= 100 and
        0 <= english_marks <= 100 and
        0 <= python_marks <= 100):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    average = (math_marks + english_marks + python_marks) / 3

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
