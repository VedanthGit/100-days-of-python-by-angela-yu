# Calculator App

def plus(num1,num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multi(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def remainder(num1, num2):
    result = num1 % num2
    return result

operations = {
    "+": plus,
    "-": subtract,
    "*": multi,
    "/": divide,
    "%": remainder
}
def calculator():
    more_numbers = True

    num1 = float(input("What is the first number: "))

    while more_numbers:

        for symbols in operations:
            print(symbols)

        operation = input("What operation would you like to operate on : ")

        num2 = float(input("What is the next number: "))

        answer = operations[operation](num1,num2)
        print(answer)
        
        continue_more = input("Whether are there any more numbers you wanna operate on: Type 'Yes' or 'No': ").lower()
        if continue_more == "yes":
            num1 = answer
        elif continue_more == "no":
            more_numbers = False
            calculator()
            
            
calculator()
        