import csv

# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

class Descriptor():
    def __init__(self, fio):
        self._fio = fio
        self.count = 0
        self.check = 0
    def __set__(self, instance, value):
        self.count = sum(1 for ch in value if ch.isupper())
        self.check = sum(1 for ch in value if not ch.isalpha())
        if self.check != 0:
            raise ValueError("Посторонние символы при вводе ФИО!") 
        if self.count < 1:
            print(f"\nОтсутствует заглавная буква!")
        elif self.count > 1:
            print(f"\nЗаглавных букв слишком много!")
        self.value = value
    def __str__(self):
        return self.value

class Student():
    namsurfam = Descriptor('')
    def __init__(self):
        self.cardline = ''
        self.marks = 0
        mco = 0
        with open("repcard.csv", 'r', encoding='utf-8') as rifle:
            pawn = csv.reader(rifle, delimiter = ",")
            for line in pawn:
                self.tests = 0
                tco = 0
                for word in range(len(line)):
                    self.cardline += line[word] + ' '
                    if word > 1 and line[word].isdigit():
                        tco += 1
                        self.tests += int(line[word])
                    elif word == 1 and line[word].isdigit():
                        mco += 1
                        self.marks += int(line[word])
                if line[0] != 'Subject':
                    print(f'Средний балл тестов по {line[0]}: {round(self.tests / tco, 2)}')
                self.cardline += '\n'
            print(f'\nСредняя оценка студента: {round(self.marks / mco, 2)}')
    def readcard(self):
        return self.cardline
    def __str__(self):
        return f'\nВаш табель, {self.namsurfam}:\n{self.readcard()}'

fio = input("2. Здравствуйте. Введите, пожалуйста, свои Фамилию Имя Отчество через пробел\n: ")
fio = fio.split()
# fio = 'Marks Bewin Webber'.split()
work = Student()
for i in range(len(fio)):
    work.namsurfam = fio[i-1]
print(work)
