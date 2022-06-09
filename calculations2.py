from colorama import Fore, Back, Style

check_num_error = Fore.BLACK + Back.RED + Style.BRIGHT
calc_answer = Fore.BLACK + Back.GREEN + Style.BRIGHT
answer = "The answer to your problem is: "


class Calculations2:

    def calculate_power(self):
        try:
            base = input("What is base number? ")
            pwr = input("What is exponent? ")
            result = (pow(float(base), float(pwr)))
            print(calc_answer + answer + str(result))
        except ValueError:
            print(check_num_error + "You have not entered valid numbers.")

    def calculate_addition(self):
        try:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            result = float(num1) + float(num2)
            print(calc_answer + answer + str(result))
        except ValueError:
            print(check_num_error + "You have not entered valid numbers.")

    def calculate_subtraction(self):
        try:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            result = float(num1) - float(num2)
            print(calc_answer + answer + str(result))
        except ValueError:
            print(check_num_error + "You have not entered valid numbers.")

    def calculate_multiplication(self):
        try:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            result = float(num1) * float(num2)
            print(calc_answer + answer + str(result))
        except ValueError:
            print(check_num_error + "You have not entered valid numbers.")

    def calculate_division(self):
        try:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            result = float(num1) / float(num2)
            print(calc_answer + answer + str(result))
        except ValueError:
            print(check_num_error + "You have not entered valid numbers.")
        except ZeroDivisionError:
            print(check_num_error + "You cannot divide by zero.")
