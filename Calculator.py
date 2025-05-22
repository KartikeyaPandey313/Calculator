def operation(number1: int, number2: int, operation):
    match operation:
        case '+':
            return number1+number2
        case '-':
            return number1-number2
        case '*':
            return number1*number2
        case '/':
            return number1/number2
        case _:
            return "Enter a valid operator"
    
def main():
    print("HI, WELCOME TO YOUR CALCULATOR.")
    running = True
    while running:
        try:
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number:"))
            ops = input("Enter + for Addition\nEnter - for Subtraction\nEnter * for Multiplication\nEnter / for Division\nEnter Operator: ")
            answer = operation(number1=num1, number2=num2, operation=ops)
            print(f"The result is: {answer}")

            y_or_n = input("Do you want another calculation (Y/n): ").lower()
            if y_or_n == 'n':
                running = False
        except:
            continue
        

if __name__ == '__main__':
    main()
