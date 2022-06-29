
students = [["tola", 234], ["bunmi", 343], ["alakija", 343]]

for i in students[0][0]:
    print(i)

students.pop(1)

print(students)
students.sort()
print(students)

print(students.__contains__(["tola", 234]))
