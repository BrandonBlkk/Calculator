import CalculatorFunction as cal

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {round(cal.add(num1, num2), 2):,}")
        elif choice == '2':
            print(f"{num1} + {num2} = {round(cal.add(num1, num2), 2):,}")
        elif choice == '3':
            print(f"{num1} + {num2} = {round(cal.add(num1, num2), 2):,}")
        elif choice == '4':
            print(f"{num1} + {num2} = {round(cal.add(num1, num2), 2):,}")

        next_calculation = input("Let's do next calculation? (yes/no):")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input.")