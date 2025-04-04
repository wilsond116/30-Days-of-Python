def add(num1, num2):
    print(f"Result: {num1 + num2}")


def sub(num1, num2):
    print(f"Result: {num1 - num2}")


def mul(num1, num2):
    print(f"Result: {num1 * num2}")


def div(num1, num2):
    try:
        print(f"Result: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


def menu():
    print("\nWhich operation do you want to perform?")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Quit")


def main():
    print("Welcome to Simple Calculator")
    keep_going = True
    while keep_going:
        menu()
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                add(num1, num2)
            elif option == 2:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                sub(num1, num2)
            elif option == 3:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                mul(num1, num2)
            elif option == 4:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                div(num1, num2)
            elif option == 5:
                keep_going = False
                print("Thank you for using our calculator")
            else:
                print("Invalid option. Please choose from 1 to 5.")
        except ValueError:
            print("Please enter a valid number.")


main()
