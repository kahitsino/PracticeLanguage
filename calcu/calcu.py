first_number = 'Enter a first number: '
second_number = 'Enter a second number: '
invalid_choices = 'System: Invalid choices'
invalid_number = 'System: Invalid number'

while True:
    print('=== CALCULATOR ===')
    print('1. Addition')
    print('2. Subtration')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    try:
        UserInput = int(input('Enter a number: '))
    except ValueError:
        print(invalid_choices)
        UserInput = None

    if UserInput == 1:
        try:
            addition1 = int(input(first_number))
            addition2 = int(input(second_number))
            print('Answer: ', addition1 + addition2)
        except ValueError:
            print(invalid_number)
    elif UserInput == 2:
        try:
            subtraction1 = int(input(first_number))
            subtraction2 = int(input(second_number))
            print('Answer: ', subtraction1 - subtraction2)
        except ValueError:
            print(invalid_number)
    elif UserInput == 3:
        try:
            multiplication1 = int(input(first_number))
            multiplication2 = int(input(second_number))
            print('Answer: ', multiplication1 * multiplication2)
        except ValueError:
            print(invalid_number)
    elif UserInput == 4:
        try:
            division1 = int(input(first_number))
            division2 = int(input(second_number))
            if division2 == 0:
                print(division1, ' cant divide in ', division2)
            else:
                print('Answer: ', division1 / division2)
        except ValueError:
            print(invalid_number)
    elif UserInput == 5:
        print('System: Exited!')
        break
    else:
        pass