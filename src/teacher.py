from person import Person

class Teacher(Person):
    # class const
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area):
        super().__init__(name, last_name, address)
        self.subject_area = subject_area
        self.profile = Teacher.profile
        self.__id = Person.get_id()

    def get_id(self):
        return self.__id

    def print_info(self):
        info = f"""
        Profile: {self.profile}
        Teaching subject: {self.subject_area}
        """
        return super().print_info() + info
    
    def update_teacher(self):
            super().update_info()
            self.subject_area = input("New teaching subject --> ").capitalize()