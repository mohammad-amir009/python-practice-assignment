
name = input("Enter your name: ")
age = int(input("Enter your age: "))


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))



addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number


print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

if second_number != 0:
    division = first_number / second_number
    print(f"Division: {division}")
else:
    print("Division: Cannot divide by zero.")
