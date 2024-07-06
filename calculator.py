def get_number():
  while True:
    try:
      number = float(input("Enter a number: "))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operation():
  while True:
    operation = input("Choose operation (+, -, *, %, /): ")
    if operation in "+-*%/":
      return operation
    else:
      print("Invalid operation. Please choose +, -, *, % or /.")

def calculate(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "%":
    return num1 % num2
  else:
    # Handle division by zero
    if num2 == 0:
      print("Error: Cannot divide by zero.")
      return None
    else:
      return num1 / num2

# Main program loop
while True:
  num1 = get_number()
  num2 = get_number()
  operation = get_operation()

  result = calculate(num1, num2, operation)
  if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != "y":
    break

print("Thank you for using the calculator!")