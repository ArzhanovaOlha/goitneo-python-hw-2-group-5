
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError('Invalid phone number')
            
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i.value
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        name = record.name.value
        self.data.update({ name : record })

    def find(self, name):
        try:
            return self.data.get(name)
        except KeyError:
            return print(f"Contact {name} not found.")
    
    def delete(self, name):
        for item in self.data.items():
            if item[0] == name:
                self.data.popitem()
                return
            else:
                return print(f"Contact {name} not found.")
