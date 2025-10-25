persons = []

for person in range(3):
    person = {}
    person['Name'] = input('Name: ')
    person['Age'] = int(input('Age: '))
    persons.append(person)
    print(persons)