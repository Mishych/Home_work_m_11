from datetime import datetime
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self._name = None
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

class Phone(Field):
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_phone):
        if self.check_number(new_phone):
            self._value = new_phone
        else: 
            raise ValueError("Not correct")
            
    @staticmethod
    def check_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class Birthday(Field):
    form = '%Y-%m-%d'
    
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_bd):
        self._value = datetime.strptime(new_bd, self.form)
        
    def __str__(self):
        if self._value:
            return self._value.strftime(self.form)
        else:
            return "Birthday not setеееее"

        
class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else birthday

    def add_phone(self, phone_number):
        phone = phone_number
        self.phones.append(Phone(phone))
        
    def add_birthday(self, bd):
        self.birthday = Birthday(bd)
        return self.birthday
        
    def days_to_bd(self):
        if not self.birthday:
            return "Birthday not set"    
        
        now = datetime.now()  
        bd = self.birthday.value
        certain_year = now.year
        bd = bd.replace(year = certain_year)
        if bd < now:
            bd = bd.replace(year = certain_year + 1)
        days_to_bdd = (bd.date() - now.date()).days
        
        return days_to_bdd
        
    def printt(self):
        return self.phones
       
    def remove_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el)
                return f"Phone {phone} has been deleted"
        return f"Phone {phone} is not found"
    
    def edit_phone(self, old_phone, new_phone):
        for ind, phone in enumerate(self.phones):          
            if phone.value == old_phone:
                self.phones[ind] = Phone(new_phone)
                return f"Phone number has been updated for {self.name.value}"
        raise ValueError
    
    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return phone
        return None
    
    def find_birthday(self, bd_to_find):
        pass


    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        birthday = self.birthday if self.birthday else "not set"
        
        return f'{self.name.name} - {phone_numbers}, birthday - {birthday}'
        # return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record
         
    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            return f"{name} has been deleted from the AddressBook"
        return f"{name} is not in the AddressBook"
           
if __name__ == "__main__":

    # bd = Birthday("2010-12-12")
    # print(bd)
    # dat = datetime.now()
    # certain_year = dat.year3
    # print(dat)
    # Створення нової адресної книги
    # book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    print(john_record)
    john_record.add_birthday("2010-11-10")
    print(john_record.days_to_bd())
    print(john_record)

    # # Додавання запису John до адресної книги
    # book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # print(john)
    # john.edit_phone("1234567890", "1112223333")

    # # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555556")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
    
    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)