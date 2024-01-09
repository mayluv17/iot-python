# person.py
class Person:
    first_name:str
    last_name:str
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(full_name)
        return None
