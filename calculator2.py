from colorama import Fore, Back, Style

from calculations2 import Calculations2

myCalculations2 = Calculations2()
calc_error = Fore.BLACK + Back.RED + Style.BRIGHT

calc = input("What calculation do you wish to perform? (Ex: add, subtract, multiply, divide, power): ")

if calc == "power":
    myCalculations2.calculate_power()

elif calc == "add":
    myCalculations2.calculate_addition()

elif calc == "subtract":
    myCalculations2.calculate_subtraction()

elif calc == "multiply":
    myCalculations2.calculate_multiplication()

elif calc == "divide":
    myCalculations2.calculate_division()

else:
    print(calc_error + "You have not entered a valid calculation.")
