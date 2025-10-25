calculationHistory = []
answer = 'Answer: '
def choices():
    print('=== CALCULATOR ===')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. History')
    print('6. Exit')
def addition(UserInput_1, UserInput_2):
    result = UserInput_1 + UserInput_2
    print(answer, result)
    addHistory("Addition", UserInput_1, UserInput_2, result)
def subtraction(UserInput_1, UserInput_2):
    result = UserInput_1 - UserInput_2
    print(answer, result)
    addHistory("Subtraction", UserInput_1, UserInput_2, result)
def multiplication(UserInput_1, UserInput_2):
    result = UserInput_1 * UserInput_2
    print(answer, result)
    addHistory("Multiplication", UserInput_1, UserInput_2, result)
def division(UserInput_1, UserInput_2):
    if UserInput_2 == 0:
        print('System: ', UserInput_1, 'by', UserInput_2, 'is not allowed.')
        return
    result = UserInput_1 / UserInput_2
    print(answer, result)
    addHistory("Division", UserInput_1, UserInput_2, result)
def historyList():
    print(calculationHistory)
def addHistory(operations, UserInput_1, UserInput_2, result): # Calling the values from operation functions input parameters
    calcuHistory = {
        "Operations": operations,
        "Numbers": (UserInput_1, UserInput_2),
        "Result": result
    } # Output: [{'operations': 'operation_name', 'Numbers:'(number_1, number_2), 'Result': result}]'}]
    calculationHistory.append(calcuHistory)
    if len(calculationHistory) > 5:
        calculationHistory.pop(0)
    else:
        pass
def UserInputOperators():
    while True:
        try:
            UserInput_1 = int(input('Enter a first number: '))
            UserInput_2 = int(input('Enter a second number: '))
            return UserInput_1, UserInput_2
        except ValueError:
            print("System: Please enter numeric values.")
def main():
    while True:
        choices()
        try:
            UserInput = int(input('Enter a choices: '))
        except ValueError:
            print("System: Please enter a valid choice.")
            continue # choose between continue or UserInput = None
        if UserInput == 1:
            UserInput_1, UserInput_2 = UserInputOperators()
            addition(UserInput_1, UserInput_2)
        elif UserInput == 2:
            UserInput_1, UserInput_2 = UserInputOperators()
            subtraction(UserInput_1, UserInput_2)
        elif UserInput == 3:
            UserInput_1, UserInput_2 = UserInputOperators()
            multiplication(UserInput_1, UserInput_2)
        elif UserInput == 4:
            UserInput_1, UserInput_2 = UserInputOperators()
            division(UserInput_1, UserInput_2)
        elif UserInput == 5:
            historyList()
        elif UserInput == 6:
            break
        else:
            continue
main()
