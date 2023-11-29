# Single Responsibility Principle / Separation of Concerns
# Anti-pattern -> God object (opposite, should be avoided)

class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return '\n'.join(self.entries)
    

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    @staticmethod
    def load_file(filename):
        print("From file")
        with open(filename) as fh:
            print(fh.read())

    def delete_file(self, filename):
        pass
    
from enum import Enum

class TestEnum(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

print(TestEnum.LARGE)
print(TestEnum.LARGE.name)
print(TestEnum.LARGE.value)
print(TestEnum(2).name)
print(TestEnum['MEDIUM'].value)

for size in TestEnum:
    print(size.name, " -- ", size.value)

j = Journal()
j.add_entry('I was depressed today')
j.add_entry('Hence I started to study')
print(f'Journal Entries : \n{j}')

filename = r'C:\raghav_personal\Programming\System Design\journal.txt'
PersistenceManager.save_to_file(j, filename)
PersistenceManager.load_file(filename)
        
        
