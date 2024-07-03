from models import Person

class Student(Person):
    # class const
    profile = "Student"
    def __init__(self, name, last_name, address, course):
        super().__init__(name, last_name, address)
        self.course = course
        self.profile = Student.profile
        self.__id = Person.get_id()

    def get_id(self):
        return self.__id

    def print_info(self):
        info = f"""
        Profile: {self.profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_student(self):
        super().update_info()
        self.course = input("New course --> ").strip().capitalize()