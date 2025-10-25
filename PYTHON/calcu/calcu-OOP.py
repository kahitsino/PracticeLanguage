historyList = []
answer = 'Answer: '
class BasicCalculator:
    def __init__(self):
        pass
    def Addition(self, number_1, number_2):
        history = CalculatorUI()
        result = number_1 + number_2
        print(answer, result)
        history.AddHistory("Addition", number_1, number_2, result)
    def Subtraction(self, number_1, number_2):
        history = CalculatorUI()
        result = number_1 - number_2
        print(answer, result)
        history.AddHistory('Subtraction', number_1, number_2, result)
    def Multiplication(self, number_1, number_2):
        history = CalculatorUI()
        result = number_1 * number_2
        print(answer, result)
        history.AddHistory('Multiplication', number_1, number_2, result)
    def Division(self, number_1, number_2):
        history = CalculatorUI()
        result = number_1 / number_2
        if number_2 == 0:
            print('System: ', number_1, " can't divide in ", number_2)
        else:
            print(answer, result)
            history.AddHistory('Division', number_1, number_2, result)
class CalculatorUI:
    def __init__(self):
        pass
    def Choices(self):
        print("1. Addition")
        print("6. Exit")
    def UserInput(self):
        while True:
            try:
                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))
                return number_1, number_2
            except ValueError:
                print("System: Invalid input. Please enter numeric values.")
    def AddHistory(self, operations, number_1, number_2, result):
        history = {
            'Operations': operations,
            'Numbers': (number_1, number_2),
            'Result': result
        }
        historyList.append(history)
    def ShowHistory(self):
        print(historyList)
def main():
    while True:
        ui = CalculatorUI()
        bCalculator = BasicCalculator()
        ui.Choices()
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("System: Invalid input. Please enter a numeric choice.")
            continue
        if choice == 1:
            number_1, number_2 = ui.UserInput()
            bCalculator.Addition(number_1, number_2)
        elif choice == 2:
            number_1, number_2 = ui.UserInput()
            bCalculator.Subtraction(number_1, number_2)
        elif choice == 3:
            number_1, number_2 = ui.UserInput()
            bCalculator.Multiplication(number_1, number_2)
        elif choice == 4:
            number_1, number_2 = ui.UserInput()
            bCalculator.Division(number_1, number_2)
        elif choice == 5:
            ui.ShowHistory()
        elif choice == 6:
            print('System: Exited!')
            break
        else:
            continue
if __name__ == "__main__":
    main()