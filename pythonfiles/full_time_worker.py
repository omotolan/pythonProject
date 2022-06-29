from pythonfiles.employee import Employee


class FullTimeWorker(Employee):

    def __init__(self, name, id_number, age, phone_number, office_location):
        super().__init__(name, id_number, age, phone_number)
        self.office_location = office_location


full_time_employee1 = FullTimeWorker("akinsola tolani", 33434, 12, "08182769505", "sabo")
print(full_time_employee1.__dict__)