import time
answer = 'Answer: '
def choices():
    print('=== CALCULATOR ===')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
def addition(UserInput_1, UserInput_2):
    print(answer, UserInput_1 + UserInput_2)
def subtraction(UserInput_1, UserInput_2):
    print(answer, UserInput_1 - UserInput_2)
def multiplication(UserInput_1, UserInput_2):
    print(answer, UserInput_1 * UserInput_2)
def division(UserInput_1, UserInput_2):
    if UserInput_2 == 0:
        print(UserInput_1, " can't divide in ", UserInput_2)
    else:
        print(answer, UserInput_1 / UserInput_2)
def UserInputOperators():
    while True:
        try:
            UserInput_1 = int(input('Enter a first number: '))
            UserInput_2 = int(input('Enter a second number: '))
            return UserInput_1, UserInput_2
        except ValueError:
            print('System: Invalid number!')
        
def main():
    while True:
        choices()
        try:
            UserInput = int(input('Enter a choices: '))
        except ValueError:
            print('System: Invalid choices!')
            UserInput = None
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
            time.sleep(2)
            print('System: Exited!')
            break
        else:
            continue
main()