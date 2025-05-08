information = {}

def read_inf():
    name = input("Write the student's name: ")
    age = input("Write the student's age: ")
    course = input("Write the student's course: ")
    return (name, age, course)

name, age, course = read_inf()
information[name] = (age, course) 