class Person:
    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address

    def print_info(self):
        info = f"""
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
    profile = "Student"
    def __init__(self, name, last_name, address, course):
        super().__init__(self, name, last_name, address)
        self.course - course
    

class Teacher(Person):
    profile = "Teacher"
    def __init__(self, name, last_name, address, subject_area = None):
        super().__init__(self, name, last_name, address)
        if subject_area is None:
            self.subject_area = []
        else:
            self.subject_area = subject_area


studente1 = Student("Danilo","Lannocca","Melbourne")
teacher1 = Teacher("Hugfel", "Professor", "Sydney")

print(studente1.print_info())
print(teacher1.print_info())

studente1.update_info()