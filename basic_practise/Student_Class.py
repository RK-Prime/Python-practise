
class Student:
    def __init__(self, name, age, course, branch):
        self.Name = name
        self.Age = age
        self.Course = course
        self.Branch = branch

    def show(self):
        print(f"Name : {self.Name},\nAge : {self.Age},\nCourse : {self.Course},\nBranch : {self.Branch} ")


def func():
    student_list = []

    n = int(input("Number of students : "))
    for i in range(n):
        print("Enter Student details: ")
        name = input("Name : ")
        age = int(input("Age : "))
        course = input("Course : ")
        branch = input("Branch : ")

        student = Student(name, age, course, branch)
        student_list.append(student)

        with open("students", "w") as file:
            for student in student_list:
                file.write(
                    f"Name : {student.Name}\nAge : {student.Age}\nCourse : {student.Course}\nBranch : {student.Branch}\n")

    q = input("Press y/Y to see Details: ")

    if q in ['y', 'Y']:
        for student in student_list:
            student.show()


        more = input("Press y/Y to input more details : ")

        if more in ['y', 'Y']:
            func()
        else:
            print("Rerun the program.")
            exit()

    else:
        ext = input("Press e/E to exit the program : ")

        if ext in ['e', 'E']:
            exit()

        else:
            print("Rerun the program.")
            exit()

#<---------->Function_Call<---------->

func()
