class Person:
    # class variable
    __id = 1

    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.id = Person.__id
        Person.__id += 1

    def print_info(self):
        info = f"""
        #ID: {self.id}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info 
    
    def update_info(self):
        print(f"""Update info: 
              1 - Name
              2 - Last Name
              3 - Address
              """)
        choice = int(input("What would you like to update? "))

        match choice:
            case 1:
                self.name = input("New name --> ")
            case 2:
                self.last_name = input("New last name --> ")
            case 3:
                self.address = input("New address --> ")
            case _:
                print("Invalid choice. Input must be between 1 and 3")

class Student(Person):
    # class variable
    profile = "Student"

    def __init__(self, name, last_name, address, course):
        super().__init__(name, last_name, address)
        self.course = course

    def print_info(self):
        info = f"""
        Profile: {Student.profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_course(self,new_course):
        self.course = new_course
        print("Course Updated")
    

class Teacher(Person):
    # class variable
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area):
        super().__init__(name, last_name, address)
        self.subject_area = subject_area

    def print_info(self):
        info = f"""
        Profile: {Teacher.profile}
        Teaching area: {self.subject_area}
        """
        return super().print_info() + info
    
    def update_subjects(self, new_subjects):
                new_list = []
                for i in new_subjects:
                    new_list.append(i)
                self.subject_area = new_list
                print(f"Subjects added")
                
    
studente1 = Student("Danilo","Lannocca","Melbourne", "coding")
teacher1 = Teacher("Hugfel", "Professor", "Sydney","matematica")

# print(studente1.print_info())
# print(teacher1.print_info())

#studente1.update_info()
#print(studente1.print_info())

teacher1.update_subjects(["filosofia","matematica","fisica"])
print(teacher1.print_info())