first_num = int(input("Enter the first number:"))
sec_num = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")



if operation == "+":
    result = first_num + sec_num
    print(f"The result is {result}.")
elif operation == "-":
    result = first_num - sec_num
    print(f"The result is {result}.")
elif operation == "*":
    result = first_num * sec_num
    print(f"The result is {result}.")
elif operation == "/":
    if sec_num == 0 or first_num == 0:
        print("Cannot divide by zero.")
    else:
        result = first_num / sec_num
        print(f"The result is {result}.")
