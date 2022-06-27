class Students:
    school = "semicolon"
    def __init__(self, first_name, last_name, age, student_class, best_subject):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_class = student_class
        self.best_subject = best_subject

    def best_food(self, food):
        print(f"my best food is {food}")



# instances objects
student1 = Students("tolani", "akinsola", 18, "jss3", "maths")

print(student1.best_subject)
student1.best_food("amala")

print(student1.school)
print(Students.school)