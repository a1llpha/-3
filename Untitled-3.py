from datetime import date, datetime

class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=''):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        
        
        year, month, day = map(int, birth_date_str.split('-'))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


person = Person('Yas', 'Sasha', '2005-28-01')
print(person.get_fullname())  
print(person.get_age())   







#Завдання 2


import csv

def modifier(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['fullname', 'age']
        
        rows = []
        for row in reader:
            person = Person(row['surname'], row['first_name'], row['birth_date'], row.get('nickname', ''))
            row['fullname'] = person.get_fullname()
            row['age'] = person.get_age()
            rows.append(row)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


modifier('contacts.csv')