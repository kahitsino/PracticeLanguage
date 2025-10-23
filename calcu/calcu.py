first_number = 'Enter a first number: '
second_number = 'Enter a second number: '
invalid_choices = 'System: Invalid choices'
invalid_number = 'System: Invalid number'

while True:
    print('=== CALCULATOR ===')
    try:
        UserInput = int(input('Enter a number: '))
    except ValueError:
        print(invalid_choices)
        

    if UserInput == 1:
        try:
            addition1 = int(input(first_number))
            addition2 = int(input(second_number))
            print('Answer: ', addition1 + addition2)
        except ValueError:
            print(invalid_number)
    elif UserInput == 2:
        subtraction1 = int(input(first_number))
        subtraction2 = int(input(second_number))
        print('Answer: ', subtraction1 - subtraction2)
    elif UserInput == 3:
        multiplication1 = int(input(first_number))
        multiplication2 = int(input(second_number))
        print('Answer: ', multiplication1 * multiplication2)
    elif UserInput == 4:
        divition1 = int(input(first_number))
        divition2 = int(input(second_number))
        print('Answer: ', divition1 / divition2)
    elif UserInput == 5:
        print('System: Exited!')