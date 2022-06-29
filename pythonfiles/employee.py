class Employee:
    company = "semicolon"

    def __init__(self, name, id_number, age, phone_number):
        self.name = name
        self.id = id_number
        self.age = age
        self.phone_number = phone_number

    @classmethod
    def name_of_organization(cls):
        print(f"")
