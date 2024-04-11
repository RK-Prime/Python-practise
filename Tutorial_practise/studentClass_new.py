
# declaring Student class
class Student:

# declaring initialization function
    def __init__(self, name, course, branch):
        self.name = name
        self.course = course
        self.branch = branch


# declaring string representation function,
# responsible for returning a string representation of the declared object
    def __str__(self):
        return f'Student Class: Student({self.name}, {self.course}, {self.branch})'

# declaring custom functions =>

# for displaying student info
    def info(self):
        print('=>')
        print(f'Name : {self.name}')
        print(f'Course : {self.course}')
        print(f'Branch : {self.branch}')
    
# for displaying student name
    def studentName(self):
        print(f'\nStudent Name : {self.name}')
    
# for displaying student course
    def studentCourse(self):
        print(f'\nStudent Course : {self.course}')

# for displaying student branch
    def studentBranch(self):
        print(f'\nStudent Branch : {self.branch}')

# student class object creation and calling
s1 = Student('Rohan', 'BTech', 'CSE')
s2 = Student('Haris', 'BTech', 'CSE')

# print(type(s1))
# print(s1)
# print(s2)
# s1.info()
# s2.info()
#stdnt_num = int(input('Enter the number of students: '))


# declaring neccessary variables
stdnt_num, stdnt_list_obj, stdnt_varlist, stdnt_obj_dict = int(input('Enter the number of student: ')), [], [], {}



# variable prompts for initializing student class
# for storing student details
for i in range(1,stdnt_num+1):
    stdnt_name = input('\nEnter student name : ')
    stdnt_course = input('Enter student course : ')
    stdnt_branch = input('Enter student branch : ')
    stdnt_obj = Student(stdnt_name, stdnt_course, stdnt_branch)

    #stdnt_obj_varlist.append(f's{i}')
    stdnt_list_obj.append(stdnt_obj)
    stdnt_varlist.append(f'Student_{i}')



#for i in range(len(stdnt_list)):
#    stdnt_list_obj.append(stdnt_list[i])
    


# storing stdnt_list values in stdnt_varlist respectively, 
# one item by one item
for i in range(len(stdnt_list_obj)):
    stdnt_obj_dict[stdnt_varlist[i]] = stdnt_list_obj[i]


# printing student details using student.info()
for stdnt_index, stdnt_value in enumerate(stdnt_obj_dict):
    print(f'\nStudent Details for {stdnt_value}')
    #print(stdnt_dict[stdnt_value])
    stdnt_obj_dict[stdnt_value].info()


# declaring function for storing student data
def stdntStorefunc_example():
    stdnt_list_stored = []
    n = int(input('\nNumber of student to be stored : '))
    for i in range(1,n+1):

        element = globals()[f's{i}']
        stdnt_list_stored.append(element)



    # printing student object
    for obj in stdnt_list_stored:
        obj.info()
        #print(type(obj))

# calling out 'stdntStorelist_func()' function
# stdntStorefunc_example()

