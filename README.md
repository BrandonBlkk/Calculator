## Calculator Project

This simple Python project is a command-line calculator that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The project uses a modular approach, with the main script interacting with a separate module named `CalculatorFunction` containing the actual mathematical functions.

### How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BrandonBlkk/Calculator.git
   cd Calculator
   ```

2. **Run the Calculator:**
   ```bash
   python Calculator.py
   ```

3. **Follow the Instructions:**
   - Select the desired operation by entering the corresponding number (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).
   - Enter the first and second numbers when prompted.
   - The result of the operation will be displayed.

4. **Repeat or Exit:**
   - After each calculation, you will be prompted to perform another calculation. Enter "yes" to continue or "no" to exit.

### Project Structure

- **calculator.py:** The main script that handles user input and calls functions from the `CalculatorFunction` module.
- **CalculatorFunction.py:** Module containing the mathematical functions (addition, subtraction, multiplication, division).
  
### Operations
- **1. Add:** Addition of two numbers.
- **2. Subtract:** Subtraction of the second number from the first.
- **3. Multiply:** Multiplication of two numbers.
- **4. Divide:** Division of the first number by the second.

### Example

```plaintext
Select operation.
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 1
Enter first number: 5
Enter second number: 3
5.0 + 3.0 = 8.0
Let's do the next calculation? (yes/no): yes
Enter choice (1/2/3/4): 3
Enter first number: 4
Enter second number: 2
4.0 * 2.0 = 8.0
Let's do the next calculation? (yes/no): no
```

### Functions

- **add(x, y):** Adds two numbers and returns the result.
- **sub(x, y):** Subtracts the second number from the first and returns the result.
- **multi(x, y):** Multiplies two numbers and returns the result.
- **div(x, y):** Divides the first number by the second and returns the result.

### Why this project is useful

This project serves as a basic example of a modular Python application, demonstrating how to organize code into separate files and functions. It also provides a simple and interactive command-line calculator that users can run locally.

Feel free to explore and modify the code to suit your needs!
