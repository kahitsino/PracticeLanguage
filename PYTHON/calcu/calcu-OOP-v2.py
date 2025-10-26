import math
class BasicCalculator:
    def __init__(self, ui_instance):
        self.ui = ui_instance
        self.answer = 'Answer: '
    def Addition(self, number_1, number_2):
        result = number_1 + number_2
        print(self.answer, result)
        self.ui.AddHistory('Addition', number_1, number_2, result)
    def Subtraction(self, number_1, number_2):
        result = number_1 - number_2
        print(self.answer, result)
        self.ui.AddHistory('Subtraction', number_1, number_2, result)
    def Multiplication(self, number_1, number_2):
        result = number_1 * number_2
        print(self.answer, result)
        self.ui.AddHistory('Multiplication', number_1, number_2, result)
    def Division(self, number_1, number_2):
        if number_2 == 0:
            print('System: ', number_1, " can't divide in", number_2)
        else:
            result = number_1 / number_2
            print(self.answer, result)
            self.ui.AddHistory('Division', number_1, number_2, result)
class AdvancedCalculator:
    def __init__(self, ui_instance):
        self.ui = ui_instance
        self.answer = 'Answer: '
    def SquareRoot(self, SquareRootInput):
        result = math.sqrt(SquareRootInput)
        print(self.answer,result)
        self.ui.AddHistory('Square Root', SquareRootInput, None, result)
class CalculatorUI:
    def __init__(self):
        self.historylist = []
        self.system = 'System: '
    def ChoicingCalculator(self):
        print('=== CHOOOSE CALCULATOR ===')
        print('1. Basic Calculator')
        print('2. Advanced Calculator')
        print('3. Exit')
    def BasicCalculatorChoicesOperators(self):
        print('=== BASIC CALCULATOR ===')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. History')
        print('6. Return')
    def AdvancedCalculatorChoicesOperators(self):
        print('=== ADVANCED CALCULATOR ===')
        print('1. Square Root')
        print('12. History')
        print('13. Return')
    def UserInput(self):
        while True:
            try:
                UserInput = int(input('Enter a number: '))
                return UserInput
            except ValueError:
                print(self.system, 'Invalid input, please enter a numeric value.')
    def UserInputNumbers(self):
        while True:
            try:
                number_1 = int(input('Enter a first number: '))
                number_2 = int(input('Enter a second number: '))
                return number_1, number_2
            except ValueError:
                print(self.system, 'Invalid input, please enter a numeric value.')
    def UserInputSingle(self):
        UserInput = float(input('Enter a number: '))
        return UserInput
    def AddHistory(self, operations, number_1, number_2=None, result=True):
        history = {
            'Operations': operations,
            'Numbers': (number_1, number_2),
            'Result': result
        }
        self.historylist.append(history)
    def ShowHistory(self):
        if not self.historylist:
            print(self.system, 'No History!')
        else:
            for i, history in enumerate(self.historylist, 1):
                Operators = ['Addition', 'Subtraction', 'Multiplication', 'Division']
                if history['Operations'] in Operators:
                    operators_symbols = {
                        'Addition': '+',
                        'Subtraction': '-',
                        'Multiplication': '*',
                        'Division': '/'
                    }
                    symbol = operators_symbols[history['Operations']]
                    print(f'{i}. {history['Operations']}: {history['Numbers'][0]} {symbol} {history['Numbers'][1]} = {history['Result']}')
                # For Square Root
                elif history['Operations'] == 'Square Root':
                    print(f'{i}. {history['Operations']}: {history['Numbers'][0]} = {history['Result']}')
                else:
                    continue
def main():
    ui = CalculatorUI()
    bcalculator = BasicCalculator(ui)
    acalculator = AdvancedCalculator(ui)
    while True:
        ui.ChoicingCalculator()
        UserInput = ui.UserInput()
        if UserInput == 1:
            while True:
                ui.BasicCalculatorChoicesOperators()
                BasicCalculatorUserInput = ui.UserInput()
                if BasicCalculatorUserInput == 1:
                    print('=== ADDITION ===')
                    number_1, number_2 = ui.UserInputNumbers()
                    bcalculator.Addition(number_1, number_2)
                elif BasicCalculatorUserInput == 2:
                    print('=== SUBTRACTION ===')
                    number_1, number_2 = ui.UserInputNumbers()
                    bcalculator.Subtraction(number_1, number_2)
                elif BasicCalculatorUserInput == 3:
                    print('=== MULTIPLICATION ===')
                    number_1, number_2 = ui.UserInputNumbers()
                    bcalculator.Multiplication(number_1, number_2)
                elif BasicCalculatorUserInput == 4:
                    print('=== DIVISION ===')
                    number_1, number_2 = ui.UserInputNumbers()
                    bcalculator.Division(number_1, number_2)
                elif BasicCalculatorUserInput == 5:
                    print('=== HISTORY ===')
                    ui.ShowHistory()
                elif BasicCalculatorUserInput == 6:
                    break
                else:
                    print('System: Please select from 1-6.')
        elif UserInput == 2:
            while True:
                ui.AdvancedCalculatorChoicesOperators()
                AdvancedCalculatorUserInput = ui.UserInput()
                if AdvancedCalculatorUserInput == 1:
                    print('=== SQUARE ROOT ===')
                    SquareRootInput = ui.UserInputSingle()
                    acalculator.SquareRoot(SquareRootInput)
                elif AdvancedCalculatorUserInput == 12:
                    ui.ShowHistory()
                elif AdvancedCalculatorUserInput == 13:
                    break
                else:
                    print('System: Please select from 1-13.')
        elif UserInput == 3:
            break
        else:
            print('System: Please select from 1-3.')
if __name__ == "__main__":
    main()