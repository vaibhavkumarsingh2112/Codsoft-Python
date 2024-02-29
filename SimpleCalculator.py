def divide(x, y):
  if y == 0:
    return "Error! Division by zero."
  else:
    return x / y


print("Select operation:(+,-,*,/)")

choice = input("Enter choice (+,-,*,/) : ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
  print(num1, "+", num2, "=", num1 + num2)
elif choice == '-':
  print(num1, "-", num2, "=", num1 - num2)
elif choice == '*':
  print(num1, "*", num2, "=", num1 * num2)
elif choice == '/':
  print(num1, "/", num2, "=", divide(num1, num2))
else:
  print("Invalid input")
